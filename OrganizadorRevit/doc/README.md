# Organizador de Famílias Revit - ISO 19650

Programa Python standalone para organizar automaticamente famílias Revit (.rfa) seguindo padrões ISO 19650 e ISO 9001.

## 🎯 Funcionalidades

- **Scanner Recursivo**: Varre todas as subpastas buscando arquivos `.rfa` e `.rfa.rfa`
- **Classificador Híbrido**: Identifica tipo de família automaticamente via palavras-chave + regex + opção de revisão manual
- **Limpeza de Duplicatas**: Descarta versões antigas (`.0001`-`.0020`) e extensões duplas (`.rfa.rfa`)
- **Renomeação ISO 19650**: Padrão `[Disciplina]-[Tipo]-[Descrição]-v[Versão]-[Status]-[Data].rfa`
- **Modos CLI**:
  - `--dry-run`: Visualização sem alterar arquivos (com ⚠️ em baixa confiança)
  - `--interactive`: Confirmação manual antes de cada operação
  - `--batch`: Processamento automático (requer `--force`)
- **Relatório CSV**: Documentação completa de todas as operações

## 📋 Estrutura ISO 19650

```
Organizador_Revit_Organizado/
├── 01_PADROES_EMPRESA/
│   ├── 01_Blocos_Margens_Carimbo/
│   ├── 02_Folhas_Margens_Carimbo/
│   ├── 03_Cartouchos_Titulos/
│   ├── 04_Legendas_Padrao/
│   ├── 05_Selos_Governamentais/
│   └── 06_Elementos_Decorativos/
├── 02_ARQUITETURA/
├── 03_ESTRUTURA/
├── 04_HIDRAULICA/
├── 05_ELETRICA/
├── 06_HVAC/
├── 07_PAISAGISMO/
├── 08_INTEGRACAO/
└── 09_ARQUIVO/
```

## 🚀 Instalação

1. **Clone ou copie este repositório**

2. **Crie um ambiente virtual Python**:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # ou
   source venv/bin/activate  # Linux/Mac
   ```

3. **Instale dependências**:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Uso

### 1. Primeiro: Executar em Modo Dry-Run (Recomendado)

```bash
python main.py --workspace "C:\Caminho\Para\Organizador_Arquivos" --dry-run
```

Este modo:
- ✓ Varre todos os arquivos
- ✓ Classifica automaticamente
- ✓ Exibe ⚠️ para arquivos com confiança baixa (<50%)
- ❌ NÃO altera os arquivos reais
- ✓ Mostra resumo com estatísticas

### 2. Depois: Modo Interativo (Para Revisão Manual)

```bash
python main.py --workspace "C:\Caminho\Para\Organizador_Arquivos" --interactive
```

Este modo:
- ✓ Mostra cada arquivo encontrado
- ✓ Exibe sugestão de classificação
- ✓ Permite aceitar (s), rejeitar (n) ou customizar (c) cada classificação
- ✓ Pausa antes de CADA movimentação
- ✓ Executa apenas com sua confirmação

### 3. Opcional: Modo Batch (Automático)

```bash
python main.py --workspace "C:\Caminho\Para\Organizador_Arquivos" --batch --force
```

**⚠️ Requer `--force` para executar sem confirmação!**

### Opções Adicionais

```bash
--output <caminho>    # Pasta de saída (padrão: Organizador_Revit_Organizado)
--sample <N>          # Processar apenas N arquivos aleatórios para teste
--help                # Mostrar ajuda
```

## 📊 Exemplo de Execução

```
$ python main.py --workspace ./Organizador_Arquivos --dry-run

======================================================================
MODO DRY-RUN (simulação sem alterar arquivos)
======================================================================

📂 Escaneando arquivos...
✓ Encontrados 302 arquivos .rfa
  - Tamanho total: 1,234.56 MB
  - Extensões duplas (.rfa.rfa): 45
  - Com sufixo de versão (.0001-.0020): 78
  - Duplicatas estimadas: 23

🔍 Classificando arquivos (isto pode levar alguns minutos)...

[████████████████████████████████████████████████] 302/302

======================================================================
RESUMO DO DRY-RUN
======================================================================
Total de arquivos: 302
Serão movidos: 279
Serão descartados (duplicatas/versões): 23
⚠️  Arquivos com confiança baixa: 5 (revisar manualmente)

======================================================================

Próximo passo: Execute com --interactive para confirmar classificações
Ou use --batch para processar automaticamente (requer --force)
```

## 📄 Exemplo de Relatório CSV

```
Arquivo_Original,Caminho_Origem,Arquivo_Novo,Pasta_Destino,Disciplina,Tipo_Familia,Acao,Motivo
"A1 01.rfa","C:\...\Blocos de margens e carimbo","AR-BLK-A1_01-v1.0-P-20250130.rfa","...\01_PADROES_EMPRESA\01_Blocos_Margens_Carimbo","01 PADROES EMPRESA","01 Blocos Margens Carimbo","Move","Reorganizado conforme ISO 19650"
"HI-LOA-Vaso.rfa.rfa","C:\...\Famílias","[Descartado]","[N/A]","04 HIDRAULICA","04 Louças","Skip Duplicate","Arquivo duplicado ou versão anterior - descartado"
```

## 🔍 Classificação Automática

O classificador usa uma abordagem **híbrida** com 3 níveis de confiança:

### 1. **Alta Confiança (100%)**
Palavras-chave exatas encontradas no nome
```
"Cartouche" → AR-CAR (Cartouchos/Títulos)
"Louça" / "Vaso" / "Cuba" → HI-LOA (Louças)
"Tubulação" / "PVC" → HI-TUB (Tubulações)
```

### 2. **Média Confiança (70%)**
Palavras-chave secundárias
```
"Legenda" → AR-LEG (Legendas)
"Torneira" → HI-TOR (Torneiras)
```

### 3. **Baixa Confiança (40%)**
Padrões regex genéricos
```
r"^A[0-4]\s+\d+" → AR-BLK (Blocos de tamanho padrão)
```

**Modo Interativo**: Qualquer classificação com <50% de confiança pede confirmação manual.

## ⚙️ Configuração

Todos os dicionários de palavras-chave estão em `config/classifier_keywords.py`.

Para adicionar novas palavras-chave:

```python
"HIDRAULICA": {
    "Louças": {
        "high_confidence": ["vaso", "cuba", "lavatório", "minha_nova_palavra"],
        "medium_confidence": ["cerâmica"],
        "patterns": [r"sua_nova_regex"]
    }
}
```

A estrutura ISO 19650 está em `config/iso_structure.py` e pode ser customizada via arquivo `config.json` no futuro.

## 📊 Padrão de Nomenclatura ISO 19650

```
[DisciplinaCode]-[TipoCode]-[Descrição]-v[Versão]-[Status]-[Data].rfa

Exemplos:
AR-BLK-Margens_A1-v1.0-P-20250130.rfa     (Blocos de margens - Arquitetura)
HI-LOA-Vaso_Cerâmica-v2.1-P-20250130.rfa  (Louça - Hidráulica)
ST-PIL-100x100_Concreto-v1.0-P-20250130.rfa (Pilar - Estrutura)
```

**Códigos de Disciplina**:
- AR = Arquitetura
- ST = Estrutura
- HI = Hidráulica
- EL = Elétrica
- HV = HVAC
- LS = Paisagismo
- IN = Integração
- SF = Segurança

**Códigos de Status**:
- W = WIP (Trabalho em Progresso)
- S = Shared (Compartilhado)
- P = Published (Publicado) ← Padrão
- A = Archive (Arquivado)

## 🛠️ Estrutura do Projeto

```
OrganizadorRevit/
├── main.py                    # Ponto de entrada
├── requirements.txt           # Dependências Python
├── config/
│   ├── iso_structure.py      # Estrutura ISO 19650 hardcoded
│   └── classifier_keywords.py # Dicionário de classificação
├── scanner/
│   └── __init__.py           # Scanner recursivo
├── classifier/
│   └── __init__.py           # Classificador híbrido
├── organizer/
│   └── __init__.py           # Organizador e renomearor
├── report/
│   └── __init__.py           # Gerador de relatório CSV
└── cli/
    └── __init__.py           # Interface CLI
```

## 🐛 Troubleshooting

### Erro: "Arquivo não encontrado"
- Verifique o caminho da pasta `--workspace`
- Use aspas se houver espaços: `"C:\Meu Projeto\Organizador_Arquivos"`

### Classificação incorreta
- Use `--interactive` para revisar manualmente
- Adicione palavras-chave em `config/classifier_keywords.py`
- Reexecute o programa

### Baixa memória com muitos arquivos
- Use `--sample 100` para testar com 100 arquivos primeiro
- Processe em lotes menores

## 📝 Licença

Uso livre para fins educacionais e profissionais.

## ✉️ Suporte

Abra uma issue ou entre em contato com o desenvolvedor.

---

**Última Atualização**: 30 de dezembro de 2025
**Versão**: 1.0.0
