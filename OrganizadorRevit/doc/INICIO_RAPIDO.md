# Instruções Rápidas - Sistema de Versioning

## 🚀 Usar Agora

```bash
# 1. Primeira visualização (sem criar pasta)
python main.py --workspace ./Organizador_Arquivos --dry-run

# 2. Processar automaticamente (cria R00)
python main.py --workspace ./Organizador_Arquivos --batch --force

# 3. Executar novamente (cria R01 automaticamente)
python main.py --workspace ./Organizador_Arquivos --batch --force

# 4. E assim sucessivamente...
python main.py --workspace ./Organizador_Arquivos --batch --force
```

## 📁 O Que Será Criado

```
Projeto/
├── Organizador_Revit_Organizado_R00/  ← Primeira execução
│   ├── Arquitetura/
│   ├── Estrutura/
│   ├── MEP/
│   └── relatório_20250101_100000.csv ✓ Aqui!
│
├── Organizador_Revit_Organizado_R01/  ← Segunda execução (automático)
│   ├── Arquitetura/
│   ├── Estrutura/
│   ├── MEP/
│   └── relatório_20250101_110000.csv ✓ Aqui!
│
└── Organizador_Revit_Organizado_R02/  ← Terceira execução (automático)
    ├── Arquitetura/
    ├── Estrutura/
    ├── MEP/
    └── relatório_20250101_120000.csv ✓ Aqui!
```

## ✨ Características Principais

✅ **Automático**: Próxima versão criada sozinha  
✅ **Seguro**: Versões anteriores nunca são alteradas  
✅ **Organizado**: Cada pasta com seu relatório  
✅ **Pronto**: Cada pasta já pode ser usada  
✅ **Histórico**: Até 100 versões diferentes  

## 📊 Modo Interativo (Confirmar Manualmente)

```bash
python main.py --workspace ./Organizador_Arquivos --interactive
```

Permite revisar cada arquivo antes de mover.

## 📖 Documentação Completa

- [README_VERSIONING.md](README_VERSIONING.md) - Guia principal
- [ALTERACOES_VERSIONING.md](ALTERACOES_VERSIONING.md) - Detalhes técnicos
- [GUIA_VERSIONING.py](GUIA_VERSIONING.py) - Guia detalhado

## 🎯 Resumo

| Ação | Resultado |
|------|-----------|
| 1ª execução | Cria `_R00` |
| 2ª execução | Cria `_R01` (automático) |
| 3ª execução | Cria `_R02` (automático) |
| ... | ... |
| 100ª execução | Cria `_R99` (máximo) |

Cada pasta é **completa e independente**, com sua própria estrutura ISO e relatório.

---

**Pronto para usar!** 🎉
