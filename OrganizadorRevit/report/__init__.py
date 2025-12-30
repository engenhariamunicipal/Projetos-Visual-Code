"""
Gerador de relatório de operações de reorganização.
Exporta para CSV com detalhes completos das operações.
"""

import csv
from pathlib import Path
from typing import List
from datetime import datetime
import sys

# Adicionar diretório raiz ao path
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from organizer import OrganizationPlan
except ImportError:
    # Fallback para importação direta
    from ..organizer import OrganizationPlan


class ReportGenerator:
    """Gera relatórios de operações de reorganização."""
    
    def __init__(self):
        """Inicializa o gerador de relatório."""
        self.plans: List[OrganizationPlan] = []
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def add_plan(self, plan: OrganizationPlan):
        """Adiciona um plano à lista de relatório."""
        self.plans.append(plan)
    
    def add_plans(self, plans: List[OrganizationPlan]):
        """Adiciona múltiplos planos."""
        self.plans.extend(plans)
    
    def generate_csv(self, output_path: Path) -> Path:
        """
        Gera relatório em CSV.
        
        Args:
            output_path: Caminho para salvar o CSV
        
        Returns:
            Caminho do arquivo gerado
        """
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Colunas do relatório
        fieldnames = [
            "Arquivo_Original",
            "Caminho_Origem",
            "Arquivo_Novo",
            "Pasta_Destino",
            "Disciplina",
            "Tipo_Familia",
            "Acao",
            "Motivo",
            "Data_Geracao"
        ]
        
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for plan in self.plans:
                writer.writerow({
                    "Arquivo_Original": plan.original_name,
                    "Caminho_Origem": str(plan.original_path),
                    "Arquivo_Novo": plan.new_name or "[Descartado]",
                    "Pasta_Destino": str(plan.destination_folder) if plan.destination_folder else "[N/A]",
                    "Disciplina": plan.discipline.replace("_", " "),
                    "Tipo_Familia": plan.type_family.replace("_", " "),
                    "Acao": plan.action.replace("_", " ").title(),
                    "Motivo": plan.reason,
                    "Data_Geracao": self.timestamp,
                })
        
        return output_path
    
    def print_summary(self) -> dict:
        """
        Imprime resumo das operações no console.
        
        Returns:
            Dict com estatísticas
        """
        total = len(self.plans)
        moved = sum(1 for p in self.plans if p.action == "move")
        skipped = total - moved
        
        print("\n" + "="*70)
        print("RESUMO DE OPERAÇÕES")
        print("="*70)
        print(f"Total de arquivos processados: {total}")
        print(f"  ✓ Para mover/copiar: {moved}")
        print(f"  ⊘ Descartados (duplicatas/versões): {skipped}")
        print(f"\nRelatório salvo em CSV")
        print("="*70 + "\n")
        
        return {
            "total": total,
            "moved": moved,
            "skipped": skipped,
        }
    
    def get_statistics(self) -> dict:
        """
        Retorna estatísticas detalhadas dos planos.
        
        Returns:
            Dict com várias estatísticas
        """
        stats = {
            "total": len(self.plans),
            "moved": sum(1 for p in self.plans if p.action == "move"),
            "skipped_duplicates": sum(1 for p in self.plans if p.action == "skip_duplicate"),
            "failed": sum(1 for p in self.plans if p.action == "failed"),
            "by_discipline": {},
            "by_type": {},
        }
        
        # Contar por disciplina
        for plan in self.plans:
            if plan.discipline not in stats["by_discipline"]:
                stats["by_discipline"][plan.discipline] = 0
            stats["by_discipline"][plan.discipline] += 1
            
            if plan.type_family not in stats["by_type"]:
                stats["by_type"][plan.type_family] = 0
            stats["by_type"][plan.type_family] += 1
        
        return stats
