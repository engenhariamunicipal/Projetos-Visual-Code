"""
Interface CLI para o organizador de famílias Revit.
Oferece modos --dry-run, --interactive e --batch.
"""

import click
from pathlib import Path
from tqdm import tqdm
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT_BASE = PROJECT_ROOT / "ultima_versao"

# Adicionar diretório raiz ao path
sys.path.insert(0, str(Path(__file__).parent.parent))

from scanner import RevitFileScanner
from classifier import RevitClassifier
from organizer import RevitOrganizer
from report import ReportGenerator
from version_manager import VersionManager


class OrganizadorCLI:
    """Interface CLI para organização de famílias Revit."""
    
    def __init__(self, workspace: Path, output_base: Path = None, output_name: str = "Organizador_Revit_Organizado"):
        """
        Inicializa a CLI.
        
        Args:
            workspace: Caminho da pasta Organizador_Arquivos
            output_base: Caminho base para saída (pai das versões). Se None, usa ultima_versao do projeto
            output_name: Nome base para a pasta versionada
        """
        self.workspace = Path(workspace)
        default_output_base = DEFAULT_OUTPUT_BASE
        self.output_base = Path(output_base) if output_base else default_output_base
        self.output_name = output_name
        
        # Obter próxima versão disponível
        self.output_path, self.version_number = VersionManager.get_next_version_folder(
            self.output_base, self.output_name
        )
        
        self.scanner = RevitFileScanner(str(self.workspace))
        self.classifier = RevitClassifier()
        self.organizer = RevitOrganizer(self.output_path)
        self.report = ReportGenerator()
        
        print(f"\n📦 Versão gerada: {self.output_path.name}")
        print(f"📍 Localização: {self.output_path.parent}\n")
    
    def run_dry_run(self):
        """Executa modo dry-run (visualização sem alterações)."""
        print("\n" + "="*70)
        print("MODO DRY-RUN (simulação sem alterar arquivos)")
        print("="*70 + "\n")
        
        # Varrer arquivos
        print("📂 Escaneando arquivos...")
        files = self.scanner.scan()
        stats = self.scanner.get_stats()
        
        print(f"✓ Encontrados {stats['total_files']} arquivos .rfa")
        print(f"  - Tamanho total: {stats['total_size_mb']:.2f} MB")
        print(f"  - Extensões duplas (.rfa.rfa): {stats['duplicate_ext_count']}")
        print(f"  - Com sufixo de versão (.0001-.0020): {stats['version_suffix_count']}")
        print(f"  - Duplicatas estimadas: {stats['estimated_duplicates']}\n")
        
        # Criar estrutura ISO (mesmo em dry-run, para visualização)
        print("📁 Estrutura ISO 19650 será criada em:", self.output_path)
        
        # Classificar arquivos
        print("\n🔍 Classificando arquivos (isto pode levar alguns minutos)...\n")
        
        plans = []
        low_confidence_count = 0
        
        for file_meta in tqdm(files, desc="Classificação", unit="arquivo"):
            # Verificar se é duplicata ou versão
            is_duplicate = file_meta.is_duplicate_ext
            is_version = file_meta.has_version_suffix
            
            # Classificar
            discipline, type_family, confidence = self.classifier.classify_file(file_meta.name)
            
            # Alertar sobre baixa confiança
            if confidence < 0.5 and not is_duplicate and not is_version:
                print(f"  ⚠️  {file_meta.name} - Confiança baixa: {confidence:.0%}")
                low_confidence_count += 1
            
            # Criar plano
            if discipline is not None:
                plan = self.organizer.plan_organization(
                    file_meta.path,
                    discipline,
                    type_family,
                    is_duplicate=is_duplicate,
                    is_version_suffix=is_version
                )
                plans.append(plan)
        
        # Adicionar planos ao relatório
        self.report.add_plans(plans)
        
        # Resumo
        print("\n" + "="*70)
        print("RESUMO DO DRY-RUN")
        print("="*70)
        print(f"Total de arquivos: {len(files)}")
        print(f"Serão movidos: {sum(1 for p in plans if p.action == 'move')}")
        print(f"Serão descartados (duplicatas/versões): {sum(1 for p in plans if p.action == 'skip_duplicate')}")
        if low_confidence_count > 0:
            print(f"⚠️  Arquivos com confiança baixa: {low_confidence_count} (revisar manualmente)")
        print("\n" + "="*70)
        print("\nPróximo passo: Execute com --interactive para confirmar classificações")
        print("Ou use --batch para processar automaticamente (requer --force)\n")
        
        return plans
    
    def run_interactive(self, plans):
        """
        Executa modo interativo (confirmação manual antes de mover).
        
        Args:
            plans: Lista de OrganizationPlan do dry-run
        """
        print("\n" + "="*70)
        print("MODO INTERATIVO (confirmação manual antes de mover)")
        print("="*70 + "\n")
        
        confirmed_plans = []
        skipped_plans = []
        
        for i, plan in enumerate(plans, 1):
            print(f"\n[{i}/{len(plans)}] {plan.original_name}")
            print(f"  Origem: {plan.original_path.parent.name}")
            print(f"  Destino: {plan.discipline} → {plan.type_family}")
            print(f"  Novo nome: {plan.new_name or '[Descartado]'}")
            print(f"  Ação: {plan.action}")
            
            if plan.action == "skip_duplicate":
                print(f"  Motivo: {plan.reason}")
                response = input("  Confirmar descarte? (s/n): ").lower().strip()
                if response == "s":
                    confirmed_plans.append(plan)
                else:
                    skipped_plans.append(plan)
            else:
                response = input("  Confirmar movimentação? (s/n/pular): ").lower().strip()
                if response == "s":
                    confirmed_plans.append(plan)
                elif response == "pular":
                    skipped_plans.append(plan)
        
        print("\n" + "="*70)
        print(f"Confirmados: {len(confirmed_plans)} arquivos")
        print(f"Pulados: {len(skipped_plans)} arquivos")
        print("="*70)
        
        # Executar planos confirmados
        print("\n⏳ Processando arquivos...")
        for plan in tqdm(confirmed_plans, desc="Movimentação", unit="arquivo"):
            self.organizer.execute_plan(plan, dry_run=False)
        
        # Gerar relatório CSV dentro da pasta de saída
        csv_path = self.output_path / f"relatório_{self.report.timestamp}.csv"
        self.report.generate_csv(csv_path)
        
        print(f"\n✓ Relatório salvo em: {csv_path}")
        self.report.print_summary()
    
    def run_batch(self, plans, force=False):
        """
        Executa modo batch (automático sem confirmação).
        
        Args:
            plans: Lista de OrganizationPlan do dry-run
            force: Se True, processa sem confirmar
        """
        if not force:
            print("\n⚠️  Modo --batch requer --force para processar automaticamente")
            print("Use: --batch --force")
            return
        
        print("\n" + "="*70)
        print("MODO BATCH (processamento automático)")
        print("="*70 + "\n")
        
        print("⏳ Processando arquivos...")
        for plan in tqdm(plans, desc="Movimentação", unit="arquivo"):
            self.organizer.execute_plan(plan, dry_run=False)
        
        # Gerar relatório CSV dentro da pasta de saída
        csv_path = self.output_path / f"relatório_{self.report.timestamp}.csv"
        self.report.generate_csv(csv_path)
        
        print(f"\n✓ Relatório salvo em: {csv_path}")
        self.report.print_summary()


@click.command()
@click.option(
    "--workspace",
    type=click.Path(exists=True),
    required=True,
    help="Caminho da pasta Organizador_Arquivos"
)
@click.option(
    "--output",
    type=click.Path(),
    default="Organizador_Revit_Organizado",
    help="Caminho de saída (padrão: ultima_versao/Organizador_Revit_Organizado)"
)
@click.option(
    "--dry-run",
    is_flag=True,
    help="Modo visualização (não altera arquivos)"
)
@click.option(
    "--interactive",
    is_flag=True,
    help="Modo interativo (confirmação antes de mover)"
)
@click.option(
    "--batch",
    is_flag=True,
    help="Modo automático (requer --force)"
)
@click.option(
    "--force",
    is_flag=True,
    help="Força processamento em modo batch"
)
@click.option(
    "--sample",
    type=int,
    default=0,
    help="Processar apenas N arquivos aleatórios para teste"
)
def main(workspace, output, dry_run, interactive, batch, force, sample):
    """
    Organizador de Famílias Revit - ISO 19650
    
    Exemplo:
    
        python main.py --workspace ./Organizador_Arquivos --dry-run
    """
    
    try:
        # Se output for um caminho completo, usar como base
        # Senão, usar workspace como base e output como nome da pasta
        if Path(output).parent.name:  # output tem caminho
            output_base = Path(output).parent
            output_name = Path(output).name
        else:  # output é apenas um nome
            output_base = None  # Usará workspace.parent
            output_name = output
        
        cli = OrganizadorCLI(workspace, output_base=output_base, output_name=output_name)
        
        # Modo dry-run é recomendado sempre primeiro
        if dry_run or not (interactive or batch):
            plans = cli.run_dry_run()
        else:
            plans = cli.run_dry_run()
        
        # Executar modo interativo ou batch
        if interactive:
            cli.run_interactive(plans)
        elif batch:
            cli.run_batch(plans, force=force)
        
        print("\n✓ Programa finalizado com sucesso!\n")
    
    except KeyboardInterrupt:
        print("\n\n⚠️  Operação cancelada pelo usuário\n")
    except Exception as e:
        print(f"\n❌ Erro: {e}\n")
        raise


if __name__ == "__main__":
    main()
