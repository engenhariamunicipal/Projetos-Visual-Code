# ✨ Atualização: Sistema de Versioning de Pastas

## 📋 Resumo das Mudanças

O programa **Organizador de Famílias Revit** foi atualizado com um sistema automático de versioning de pastas. Agora, **cada execução cria uma nova pasta com sufixo sequencial** (_R00, _R01, _R02, etc.), e **todos os relatórios são salvos dentro de cada pasta de versão**.

## 🎯 Objetivo Alcançado

✅ **Pastas versionadas**: Cada execução cria `Organizador_Revit_Organizado_R##`  
✅ **Sem conflitos**: Versões anteriores nunca são sobrescritas  
✅ **Relatórios integrados**: CSV fica dentro da pasta versionada  
✅ **Pronto para usar**: Cada pasta é auto-contida e funcional  
✅ **Histórico completo**: Rastreabilidade total de processamentos  

## 📁 Estrutura de Versões

```
Projeto/
├── Organizador_Revit_Organizado_R00/  ← 1ª execução
│   ├── Arquitetura/
│   ├── Estrutura/
│   ├── MEP/
│   └── relatório_20250101_100000.csv ✓
│
├── Organizador_Revit_Organizado_R01/  ← 2ª execução
│   ├── Arquitetura/
│   ├── Estrutura/
│   ├── MEP/
│   └── relatório_20250101_110000.csv ✓
│
└── Organizador_Revit_Organizado_R02/  ← 3ª execução
    ├── Arquitetura/
    ├── Estrutura/
    ├── MEP/
    └── relatório_20250101_120000.csv ✓
```

## 🔧 Como Usar

### Primeira Execução (Visualização)
```bash
python main.py --workspace ./Organizador_Arquivos --dry-run
```

### Primeira Execução (Automática)
```bash
python main.py --workspace ./Organizador_Arquivos --batch --force
# Cria: Organizador_Revit_Organizado_R00/
```

### Segunda Execução (Automática)
```bash
python main.py --workspace ./Organizador_Arquivos --batch --force
# Cria: Organizador_Revit_Organizado_R01/ (automaticamente)
```

### Terceira Execução (Automática)
```bash
python main.py --workspace ./Organizador_Arquivos --batch --force
# Cria: Organizador_Revit_Organizado_R02/ (automaticamente)
```

## 📦 Arquivos Novos

| Arquivo | Descrição |
|---------|-----------|
| `version_manager.py` | Módulo de gerenciamento de versões |
| `test_version_manager.py` | Testes automatizados |
| `demo_versioning.py` | Demonstração do sistema |
| `ALTERACOES_VERSIONING.md` | Documentação técnica |
| `RESUMO_ALTERACOES.py` | Resumo visual das mudanças |
| `GUIA_VERSIONING.py` | Guia completo de uso |
| `README_VERSIONING.md` | Este arquivo |

## 🔄 Fluxo de Execução

```
Primeira Execução:
  ├─ Detecta que não existe _R00
  ├─ Cria: Organizador_Revit_Organizado_R00/
  ├─ Processa arquivos
  └─ Salva relatório.csv DENTRO da pasta

Segunda Execução:
  ├─ Detecta que existe _R00
  ├─ Procura por _R01, não encontra
  ├─ Cria: Organizador_Revit_Organizado_R01/
  ├─ Processa arquivos
  └─ Salva relatório.csv DENTRO da pasta

Terceira Execução:
  ├─ Detecta que existem _R00 e _R01
  ├─ Procura por _R02, não encontra
  ├─ Cria: Organizador_Revit_Organizado_R02/
  ├─ Processa arquivos
  └─ Salva relatório.csv DENTRO da pasta
```

## ✨ Benefícios

| Benefício | Descrição |
|-----------|-----------|
| 🔍 **Rastreabilidade** | Cada versão tem seu relatório próprio |
| 🚀 **Sem conflitos** | Versões anteriores nunca são alteradas |
| 📊 **Auditoria** | Histórico completo de processamentos |
| 📦 **Auto-contido** | Cada pasta tem tudo que precisa |
| 🔄 **Reversível** | Pode voltar a versão anterior quando quiser |
| 🎯 **Automático** | Próxima versão criada automaticamente |

## 🧪 Testes Realizados

✅ Extração de número de versão  
✅ Detecção de pastas existentes  
✅ Incremento automático  
✅ Formatação com 2 dígitos  
✅ Múltiplas execuções sequenciais  
✅ Relatórios na pasta correta  
✅ Integração com CLI  

## 📝 Relatórios CSV

Cada versão contém um arquivo CSV com:

- **Arquivo_Original**: Nome do arquivo .rfa original
- **Caminho_Origem**: Localização original
- **Arquivo_Novo**: Nome após organização
- **Pasta_Destino**: Pasta final conforme ISO 19650
- **Disciplina**: Engenharia responsável
- **Tipo_Familia**: Subcategoria
- **Acao**: Ação realizada (move, skip, etc)
- **Motivo**: Razão de skip, se aplicável
- **Data_Geracao**: Timestamp de processamento

## 🎨 Compatibilidade

✅ Python 3.10+  
✅ Windows, Linux, macOS  
✅ Padrão ISO 19650 mantido  
✅ Todos os modos funcionando  

## 📖 Leia Mais

Para informações detalhadas:
- 📄 [ALTERACOES_VERSIONING.md](ALTERACOES_VERSIONING.md)
- 📚 [GUIA_VERSIONING.py](GUIA_VERSIONING.py)
- 🔬 [version_manager.py](version_manager.py)

## 🚀 Próximos Passos

1. Execute com `--dry-run` para visualizar
2. Execute com `--interactive` para confirmar manualmente
3. Execute com `--batch --force` para processar automaticamente

Cada execução cria uma nova versão pronta para usar!

---

**Versão**: 2.0.0 com Sistema de Versioning  
**Data**: 30 de dezembro de 2025  
**Status**: ✅ Testado e pronto para produção
