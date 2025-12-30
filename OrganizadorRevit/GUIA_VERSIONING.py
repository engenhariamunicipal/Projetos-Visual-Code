"""
GUIA DE USO - SISTEMA DE VERSIONING

Este arquivo explica como usar o programa com o novo sistema de versioning.
"""

# ============================================================================
# INÍCIO RÁPIDO
# ============================================================================

COMEÇAR = """
1. Abra o terminal PowerShell no diretório do projeto

2. Execute o programa:
   python main.py --workspace ./Organizador_Arquivos --dry-run

3. Na primeira execução será criado: Organizador_Revit_Organizado_R00/

4. Na segunda execução será criado: Organizador_Revit_Organizado_R01/

5. E assim sucessivamente...
"""

# ============================================================================
# MODOS DE EXECUÇÃO
# ============================================================================

MODO_DRY_RUN = """
MODO DRY-RUN (Visualização sem alterar arquivos)
================================================

Comando:
  python main.py --workspace ./Organizador_Arquivos --dry-run

O que faz:
  ✓ Varre os arquivos .rfa
  ✓ Mostra estatísticas
  ✓ Simula a reorganização
  ✗ NÃO move/copia nenhum arquivo
  ✗ NÃO cria a pasta de versão

Quando usar:
  → Primeira vez que executa o programa
  → Para revisar o que será feito
  → Para verificar confiança na classificação
"""

MODO_INTERATIVO = """
MODO INTERATIVO (Confirmação manual)
====================================

Comando:
  python main.py --workspace ./Organizador_Arquivos --interactive

O que faz:
  ✓ Varre os arquivos
  ✓ Pede confirmação para cada arquivo
  ✓ Cria a pasta de versão (ex: Organizador_Revit_Organizado_R00/)
  ✓ Move os arquivos confirmados
  ✓ Salva relatório CSV DENTRO da pasta

Quando usar:
  → Para revisar manualmente cada arquivo
  → Para maior controle
  → Quando há dúvida sobre a classificação
"""

MODO_BATCH = """
MODO BATCH (Automático)
=======================

Comando:
  python main.py --workspace ./Organizador_Arquivos --batch --force

O que faz:
  ✓ Varre os arquivos
  ✓ Processa automaticamente
  ✓ Cria a pasta de versão (ex: Organizador_Revit_Organizado_R01/)
  ✓ Move todos os arquivos
  ✓ Salva relatório CSV DENTRO da pasta

Quando usar:
  → Após testar com --dry-run e --interactive
  → Quando confia na classificação
  → Para automatizar o processo
"""

# ============================================================================
# ENTENDENDO AS VERSÕES
# ============================================================================

VERSOES = """
ENTENDENDO AS VERSÕES
====================

Cada execução do programa cria uma pasta com sufixo de versão:

R00 = Primeira execução      → Organizador_Revit_Organizado_R00/
R01 = Segunda execução       → Organizador_Revit_Organizado_R01/
R02 = Terceira execução      → Organizador_Revit_Organizado_R02/
...
R99 = Centésima execução     → Organizador_Revit_Organizado_R99/

ESTRUTURA DE CADA VERSÃO:

Organizador_Revit_Organizado_R05/
├── Arquitetura/
│   ├── Componentes_Construtivos/
│   ├── Estrutura/
│   └── ...
├── Estrutura/
│   └── ...
├── MEP/
│   └── ...
├── relatório_20250101_120000.csv  ← CSV da versão
└── ...

IMPORTANTE:
  • Cada pasta de versão é auto-contida
  • O relatório CSV fica DENTRO de cada pasta
  • As pastas anteriores não são alteradas
  • Histórico completo preservado
"""

# ============================================================================
# ESTRUTURA DE PASTAS APÓS MÚLTIPLAS EXECUÇÕES
# ============================================================================

ESTRUTURA_MULTIPLAS = """
ESTRUTURA APÓS MÚLTIPLAS EXECUÇÕES
===================================

Projeto/
├── Organizador_Arquivos/           (entrada - não alterada)
│   ├── Blocos de margens e carimbo/
│   ├── Folhas margens e carimbo/
│   └── ...
│
├── Organizador_Revit_Organizado_R00/  (1ª execução)
│   ├── Arquitetura/
│   ├── Estrutura/
│   ├── MEP/
│   └── relatório_20250101_100000.csv
│
├── Organizador_Revit_Organizado_R01/  (2ª execução)
│   ├── Arquitetura/
│   ├── Estrutura/
│   ├── MEP/
│   └── relatório_20250101_110000.csv
│
├── Organizador_Revit_Organizado_R02/  (3ª execução)
│   ├── Arquitetura/
│   ├── Estrutura/
│   ├── MEP/
│   └── relatório_20250101_120000.csv
│
└── [... mais versões ...]

VANTAGENS:
  ✓ Rastrear cada versão
  ✓ Comparar mudanças entre versões
  ✓ Reverter para versão anterior se necessário
  ✓ Auditoria completa de todos os processamentos
"""

# ============================================================================
# RELATÓRIOS
# ============================================================================

RELATORIOS = """
RELATÓRIOS
==========

Cada versão contém um arquivo CSV com:

Nome:
  relatório_YYYYMMDD_HHMMSS.csv
  Ex: relatório_20250101_143527.csv

Localização:
  DENTRO da pasta de versão
  Ex: Organizador_Revit_Organizado_R05/relatório_20250101_143527.csv

Colunas:
  • Arquivo_Original          (nome original do .rfa)
  • Caminho_Origem            (localização original)
  • Arquivo_Novo              (nome após organização)
  • Pasta_Destino             (pasta final ISO)
  • Disciplina                (ex: Arquitetura)
  • Tipo_Familia              (ex: Componentes_Construtivos)
  • Acao                      (move, skip_duplicate, etc)
  • Motivo                    (por que foi descartado, se aplicável)
  • Data_Geracao              (timestamp do processamento)

Uso:
  ✓ Verificar o que foi movido
  ✓ Identificar duplicatas descartadas
  ✓ Auditar mudanças
  ✓ Documentar processamento
"""

# ============================================================================
# SOLUÇÃO DE PROBLEMAS
# ============================================================================

SOLUCAO_PROBLEMAS = """
SOLUÇÃO DE PROBLEMAS
====================

P: Pasta não foi criada
R: Verifique que --workspace aponta para diretório válido com .rfa

P: Relatório não aparece na pasta
R: Verifique que usou --batch --force ou --interactive para criar

P: Quer limpar versões antigas
R: Delete manualmente as pastas _R## que não precisa
   (as outras não serão afetadas)

P: Quer continuar de uma versão específica
R: Simplifique apenas para testar, versões anteriores ficam intactas

P: Quer saber qual versão foi criada
R: Procure por mensagem "Versão criada" ou verifique
   folder com maior número _R##
"""

# ============================================================================
# EXIBIR GUIA
# ============================================================================

if __name__ == "__main__":
    print("=" * 75)
    print("GUIA DE USO - SISTEMA DE VERSIONING DE PASTAS")
    print("=" * 75)
    print()
    print(COMEÇAR)
    print()
    print("=" * 75)
    print(MODO_DRY_RUN)
    print()
    print("=" * 75)
    print(MODO_INTERATIVO)
    print()
    print("=" * 75)
    print(MODO_BATCH)
    print()
    print("=" * 75)
    print(VERSOES)
    print()
    print("=" * 75)
    print(ESTRUTURA_MULTIPLAS)
    print()
    print("=" * 75)
    print(RELATORIOS)
    print()
    print("=" * 75)
    print(SOLUCAO_PROBLEMAS)
    print()
    print("=" * 75)
    print("[OK] Guia carregado com sucesso!")
    print("=" * 75)
