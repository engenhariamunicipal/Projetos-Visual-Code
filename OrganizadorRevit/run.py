#!/usr/bin/env python3
"""
Script de inicialização rápida com validação de dependências
"""

import subprocess
import sys
from pathlib import Path

def check_dependencies():
    """Verifica se as dependências estão instaladas."""
    required = ['click', 'tqdm']
    missing = []
    
    for package in required:
        try:
            __import__(package)
        except ImportError:
            missing.append(package)
    
    if missing:
        print(f"❌ Pacotes não instalados: {', '.join(missing)}")
        print("\nInstalando dependências...")
        subprocess.check_call(
            [sys.executable, '-m', 'pip', 'install'] + missing
        )
        print("✓ Dependências instaladas com sucesso!\n")
    else:
        print("✓ Todas as dependências estão disponíveis\n")

if __name__ == "__main__":
    print("=" * 70)
    print("Organizador de Famílias Revit - ISO 19650")
    print("=" * 70)
    print()
    
    check_dependencies()
    
    # Importar e executar CLI
    from cli import main
    main()
