# 🚀 GUIA RÁPIDO - Organizador de Famílias Revit

## Instalação (primeira vez)

```bash
# Windows
pip install click tqdm

# Ou use Python direto
python -m pip install click tqdm
```

## Execução

### 1️⃣ Modo DRY-RUN (Recomendado - visualização sem alterar)

```bash
python main.py --workspace "C:\Caminho\Organizador_Arquivos" --dry-run
```

**O que faz:**
- ✓ Varre todos os arquivos
- ✓ Classifica automaticamente
- ✓ Mostra resumo
- ❌ NÃO altera nada

### 2️⃣ Modo INTERATIVO (Confirmação manual)

```bash
python main.py --workspace "C:\Caminho\Organizador_Arquivos" --interactive
```

**O que faz:**
- ✓ Mostra cada arquivo
- ✓ Permite confirmar ou corrigir classificação
- ✓ Pausa antes de cada ação
- ✓ Executa com sua aprovação

### 3️⃣ Modo BATCH (Automático)

```bash
python main.py --workspace "C:\Caminho\Organizador_Arquivos" --batch --force
```

**⚠️ CUIDADO:** Processa SEM confirmação. Use `--force` apenas após validar com `--dry-run`

---

## Exemplos Práticos

**Exemplo 1: Testar com poucos arquivos**
```bash
python main.py --workspace "C:\meus_arquivos" --dry-run --sample 10
```

**Exemplo 2: Processar após validar**
```bash
# Primeiro, visualizar
python main.py --workspace "C:\meus_arquivos" --dry-run

# Depois, confirmar tudo
python main.py --workspace "C:\meus_arquivos" --batch --force
```

**Exemplo 3: Especificar pasta de saída**
```bash
python main.py --workspace "C:\meus_arquivos" --output "C:\saida_organizada" --dry-run
```

---

## Saída Esperada

Após execução, será criada estrutura como:

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
│   ├── 01_Janelas/
│   ├── 02_Portas/
│   ├── 03_Paredes/
│   └── ...
├── 03_ESTRUTURA/
├── 04_HIDRAULICA/
│   ├── 01_Tubulacoes/
│   ├── 02_Conexoes/
│   ├── 03_Valvulas/
│   ├── 04_Louças/
│   ├── 05_Torneiras/
│   └── 06_Acessorios/
├── 05_ELETRICA/
├── 06_HVAC/
├── 07_PAISAGISMO/
├── 08_INTEGRACAO/
└── 09_ARQUIVO/
    └── 01_Versoes_Anteriores/
```

---

## Nomenclatura ISO 19650

Arquivos são renomeados seguindo padrão:

```
[DisciplinaCode]-[TipoCode]-[Descrição]-v[Versão]-[Status]-[Data].rfa

Exemplo:
AR-CAR-Cartouche_Padrão-v1.0-P-20250130.rfa
HI-LOA-Vaso_Cerâmica-v1.0-P-20250130.rfa
ST-PIL-100x100_Concreto-v1.0-P-20250130.rfa
```

---

## Dúvidas Frequentes

**P: Posso reverter após executar?**
R: Sim! Os arquivos originais são preservados. Apenas copiam (não movem). Você pode deletar a pasta de saída e reexecutar.

**P: Como adicionar novas palavras-chave de classificação?**
R: Edite `config/classifier_keywords.py` e adicione a palavra-chave desejada.

**P: Arquivo foi classificado incorretamente. O que fazer?**
R: Use `--interactive` e customize manualmente. Ou adicione palavras-chave em `classifier_keywords.py`.

**P: Pode processar em partes?**
R: Sim! Use `--sample 50` para testar com 50 arquivos.

---

## Arquivo de Log/Relatório

Após cada execução, será gerado `relatório_[timestamp].csv` com detalhes completos.

---

**Versão**: 1.0.0  
**Data**: 30-12-2025  
**Padrão**: ISO 19650 + ISO 9001
