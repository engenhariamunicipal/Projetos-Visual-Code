"""
Script de teste para verificar o funcionamento do sistema de versioning.
"""

import sys
from pathlib import Path
from version_manager import VersionManager

def test_version_manager():
    """Testa o VersionManager."""
    
    print("=" * 70)
    print("TESTE DO VERSION MANAGER")
    print("=" * 70)
    
    # Teste 1: Extrair versão
    print("\n📝 Teste 1: Extrair versão do nome")
    test_names = [
        ("Organizador_Revit_Organizado_R00", 0),
        ("Organizador_Revit_Organizado_R05", 5),
        ("Organizador_Revit_Organizado_R23", 23),
        ("Organizador_Revit_Organizado", None),
        ("Algum_outro_nome_R10", 10),
    ]
    
    for name, expected in test_names:
        result = VersionManager.extract_version_suffix(name)
        status = "✓" if result == expected else "✗"
        print(f"  {status} '{name}' → {result} (esperado: {expected})")
    
    # Teste 2: Formatar string de versão
    print("\n📝 Teste 2: Formatar string de versão")
    test_versions = [0, 1, 5, 23, 99]
    
    for version in test_versions:
        result = VersionManager.format_version_string(version)
        print(f"  ✓ {version} → '{result}'")
    
    # Teste 3: Obter próxima versão (teste com diretório temporal)
    print("\n📝 Teste 3: Obter próxima versão disponível")
    import tempfile
    
    with tempfile.TemporaryDirectory() as tmpdir:
        test_path = Path(tmpdir)
        
        # Criar algumas pastas de teste
        (test_path / "TestFolder_R00").mkdir()
        (test_path / "TestFolder_R01").mkdir()
        (test_path / "TestFolder_R02").mkdir()
        
        # Obter próxima versão
        next_path, next_version = VersionManager.get_next_version_folder(test_path, "TestFolder")
        
        print(f"  ✓ Próxima versão: {next_version} (esperado: 3)")
        print(f"  ✓ Caminho: {next_path.name}")
        
        # Verificar se é _R03
        assert next_path.name == "TestFolder_R03", "Nome da pasta incorreto!"
        assert next_version == 3, "Número de versão incorreto!"
        
        print("\n✓ Teste de versioning passou com sucesso!\n")

if __name__ == "__main__":
    try:
        test_version_manager()
        print("="*70)
        print("✓ TODOS OS TESTES PASSARAM")
        print("="*70)
    except AssertionError as e:
        print(f"\n✗ Erro no teste: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Erro inesperado: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
