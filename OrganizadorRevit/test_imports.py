#!/usr/bin/env python3
"""
Script de teste rápido - valida imports e estrutura básica
"""

import sys
from pathlib import Path

# Adicionar raiz ao path
sys.path.insert(0, str(Path(__file__).parent))

print("=" * 70)
print("TESTE DE IMPORTS - Organizador de Famílias Revit")
print("=" * 70)

try:
    print("\n✓ Importando config.iso_structure...")
    from config.iso_structure import ISO_STRUCTURE, DISCIPLINE_CODES, TYPE_CODES
    print(f"  ✓ Estrutura ISO com {len(ISO_STRUCTURE)} disciplinas")
    
    print("\n✓ Importando config.classifier_keywords...")
    from config.classifier_keywords import CLASSIFIER_KEYWORDS, get_keywords
    print(f"  ✓ Dicionário com palavras-chave carregado")
    
    print("\n✓ Importando scanner.RevitFileScanner...")
    from scanner import RevitFileScanner
    print("  ✓ Scanner importado com sucesso")
    
    print("\n✓ Importando classifier.RevitClassifier...")
    from classifier import RevitClassifier
    print("  ✓ Classificador importado com sucesso")
    
    print("\n✓ Importando organizer.RevitOrganizer...")
    from organizer import RevitOrganizer
    print("  ✓ Organizador importado com sucesso")
    
    print("\n✓ Importando report.ReportGenerator...")
    from report import ReportGenerator
    print("  ✓ Gerador de relatório importado com sucesso")
    
    print("\n" + "=" * 70)
    print("✓ TODOS OS IMPORTS VALIDADOS COM SUCESSO!")
    print("=" * 70)
    
    # Teste básico do classificador
    print("\n" + "=" * 70)
    print("TESTE BÁSICO - Classificação")
    print("=" * 70)
    
    classifier = RevitClassifier()
    
    test_files = [
        "Cartouche - 01.rfa",
        "HI-LOA-Vaso_Cerâmica.rfa",
        "A1 01.rfa",
        "Legenda Clara.rfa",
        "Tubulação PVC Ø50.rfa",
    ]
    
    print("\nTestando classificação automática:\n")
    for filename in test_files:
        discipline, type_family, confidence = classifier.classify_file(filename)
        print(f"  • {filename}")
        if discipline:
            print(f"    → {discipline} / {type_family} ({confidence:.0%})")
        else:
            print(f"    → Sem classificação")
    
    print("\n" + "=" * 70)
    print("✓ PROGRAMA PRONTO PARA USO!")
    print("=" * 70)
    print("\nPróximos passos:")
    print("  1. python main.py --workspace ./Organizador_Arquivos --dry-run")
    print("  2. python main.py --workspace ./Organizador_Arquivos --interactive")
    print("\n")

except Exception as e:
    print(f"\n❌ ERRO: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
