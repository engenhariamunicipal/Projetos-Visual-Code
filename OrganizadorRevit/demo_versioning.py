"""
Script de demonstração do sistema de versioning de pastas.
Simula a criação de múltiplas versões executando o programa várias vezes.
"""

import sys
from pathlib import Path
from version_manager import VersionManager
import tempfile
import shutil

def demo_versioning():
    """Demonstração do sistema de versioning."""
    
    print("=" * 70)
    print("DEMONSTRACAO: SISTEMA DE VERSIONING DE PASTAS")
    print("=" * 70)
    
    # Criar um diretório temporal para a demonstração
    with tempfile.TemporaryDirectory() as tmpdir:
        demo_path = Path(tmpdir) / "demo_output"
        
        print(f"\n📁 Diretório de demonstração: {demo_path}\n")
        
        # Simular 5 execuções do programa
        for execution in range(5):
            print(f"--- Execução #{execution + 1} ---")
            
            # Obter próxima versão disponível
            output_path, version = VersionManager.get_next_version_folder(
                demo_path, 
                "Organizador_Revit_Organizado"
            )
            
            # Criar a pasta
            output_path.mkdir(parents=True, exist_ok=True)
            
            # Criar alguns arquivos simulados
            (output_path / "relatorio_20250101_001000.csv").touch()
            (output_path / "Disciplina1").mkdir(exist_ok=True)
            (output_path / "Disciplina2").mkdir(exist_ok=True)
            
            print(f"  Versão criada: {output_path.name}")
            print(f"  Número: {version}")
            print(f"  Caminho: {output_path}")
            print(f"  Status: Pronto para usar\n")
        
        # Mostrar estrutura criada
        print("--- Estrutura Final ---")
        for item in sorted(demo_path.iterdir()):
            if item.is_dir():
                # Contar arquivos
                file_count = len(list(item.rglob("*")))
                print(f"  {item.name}")
                print(f"    └─ Contém {file_count} itens")

if __name__ == "__main__":
    try:
        demo_versioning()
        print("\n[OK] Demonstracao concluida com sucesso!")
    except Exception as e:
        print(f"\n[ERRO] {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
