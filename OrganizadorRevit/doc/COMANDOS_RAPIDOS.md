# ⚡ COMANDOS RÁPIDOS

## Windows PowerShell / CMD

### Pré-requisito: Instalar Dependências (uma vez)
```powershell
python -m pip install click tqdm
```

### Opção 1: Usar Menu Interativo (Recomendado para iniciantes)
```powershell
run.bat
```
Apresenta menu com opções 1-4. Responda interativamente.

---

## Python Direct (Recomendado)

### Opção 2: Modo DRY-RUN (sempre começar aqui!)
```powershell
python main.py --workspace "C:\Caminho\Organizador_Arquivos" --dry-run
```

**Output esperado:**
```
✓ Encontrados 300 arquivos .rfa
  - Tamanho total: 74.06 MB
  - Extensões duplas (.rfa.rfa): 64
  - Com sufixo de versão (.0001-.0020): 37
  
Total de arquivos: 300
Serão movidos: 199
Serão descartados: 101
```

---

### Opção 3: Modo INTERATIVO (confirmar tudo manualmente)
```powershell
python main.py --workspace "C:\Caminho\Organizador_Arquivos" --interactive
```

**Esperado:**
```
[1/300] A0 01.rfa
  Origem: Blocos de margens e carimbo
  Destino: 01_PADROES_EMPRESA → 01_Blocos_Margens_Carimbo
  Novo nome: AR-BLK-A0_01-v1.0-P-20250130.rfa
  Ação: move
  
  Confirmar movimentação? (s/n/pular): s
```

---

### Opção 4: Modo BATCH (automático, requer --force)
```powershell
python main.py --workspace "C:\Caminho\Organizador_Arquivos" --batch --force
```

**⚠️ NÃO use sem validar com --dry-run primeiro!**

---

## Variações Úteis

### Testar com poucos arquivos
```powershell
python main.py --workspace "C:\Caminho\Organizador_Arquivos" --dry-run --sample 10
```

### Especificar pasta de saída customizada
```powershell
python main.py --workspace "C:\Caminho\Organizador_Arquivos" --output "C:\Minha_Saida" --dry-run
```

### Executar com script de auto-verificação
```powershell
python run.py --workspace "C:\Caminho\Organizador_Arquivos" --dry-run
```

---

## Exemplos Completos (Copy-Paste)

### Exemplo 1: Testar com 10 arquivos
```powershell
python main.py --workspace "C:\Users\danie\OneDrive\Área de Trabalho\Projetos-Visual-Code\Organizador_Arquivos" --dry-run --sample 10
```

### Exemplo 2: Processo completo
```powershell
# Passo 1: Visualizar
python main.py --workspace "C:\Users\danie\OneDrive\Área de Trabalho\Projetos-Visual-Code\Organizador_Arquivos" --dry-run

# [Revisar output...]

# Passo 2: Processar interativamente
python main.py --workspace "C:\Users\danie\OneDrive\Área de Trabalho\Projetos-Visual-Code\Organizador_Arquivos" --interactive
```

### Exemplo 3: Automatizar tudo
```powershell
# Primeira execução (sempre)
python main.py --workspace "C:\Users\danie\OneDrive\Área de Trabalho\Projetos-Visual-Code\Organizador_Arquivos" --dry-run

# Se OK, executar
python main.py --workspace "C:\Users\danie\OneDrive\Área de Trabalho\Projetos-Visual-Code\Organizador_Arquivos" --batch --force
```

---

## Help / Ajuda

```powershell
python main.py --help
```

**Output:**
```
Usage: main.py [OPTIONS]

  Organizador de Famílias Revit - ISO 19650

  Exemplo:

      python main.py --workspace ./Organizador_Arquivos --dry-run

Options:
  --workspace TEXT      Caminho da pasta Organizador_Arquivos [required]
  --output TEXT         Caminho de saída (padrão: Organizador_Revit_Organizado)
  --dry-run            Modo visualização (não altera arquivos)
  --interactive        Modo interativo (confirmação antes de mover)
  --batch              Modo automático (requer --force)
  --force              Força processamento em modo batch
  --sample INTEGER      Processar apenas N arquivos aleatórios para teste
  --help               Show this message and exit.
```

---

## Resultado

Após execução, procure por:
```
Organizador_Revit_Organizado/
  ├── 01_PADROES_EMPRESA/
  │   ├── 01_Blocos_Margens_Carimbo/
  │   ├── 02_Folhas_Margens_Carimbo/
  │   ├── 03_Cartouchos_Titulos/
  │   └── ... (mais 3 subpastas)
  ├── 02_ARQUITETURA/
  ├── 03_ESTRUTURA/
  ├── 04_HIDRAULICA/
  ├── 05_ELETRICA/
  ├── 06_HVAC/
  ├── 07_PAISAGISMO/
  ├── 08_INTEGRACAO/
  └── 09_ARQUIVO/
```

E o relatório:
```
relatorio_20250130_143022.csv
```

---

## Troubleshooting Rápido

| Erro | Solução |
|------|---------|
| `ModuleNotFoundError: click` | `python -m pip install click tqdm` |
| `FileNotFoundError: workspace` | Verificar caminho com aspas |
| `UnicodeDecodeError` | (já corrigido na v1.0) |
| Classificação errada | Use `--interactive` para corrigir |
| Muitos arquivos baixa confiança | Adicione keywords em `config/classifier_keywords.py` |

---

**🚀 Pronto! Execute o primeiro comando acima e veja a magia acontecer!**

Data: 30-12-2025 | Versão: 1.0.0
