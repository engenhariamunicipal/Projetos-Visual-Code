## Alterações Implementadas - Sistema de Versioning de Pastas

### Resumo das Mudanças

O programa foi atualizado para criar automaticamente versões numeradas de pastas com sufixo `_R00`, `_R01`, `_R02`, etc. Toda vez que o programa é executado, uma nova versão é gerada. Todos os relatórios agora estão incluídos dentro da pasta de versão correspondente, deixando-a pronta para uso.

### Arquivos Modificados

#### 1. **novo arquivo: `version_manager.py`**
   - Novo módulo com a classe `VersionManager`
   - Funções principais:
     - `extract_version_suffix()`: Extrai número de versão do nome da pasta
     - `get_next_version_folder()`: Encontra próxima versão disponível
     - `format_version_string()`: Formata número com dois dígitos (R00, R01, etc.)

#### 2. **modificado: `cli/__init__.py`**
   - Importação do novo `VersionManager`
   - Alteração no `__init__` da classe `OrganizadorCLI`:
     - Agora calcula automaticamente a próxima versão disponível
     - Cria pasta com sufixo `_R##` (ex: `Organizador_Revit_Organizado_R03`)
     - Exibe versão gerada e localização ao iniciar
   
   - Modificação em `run_interactive()`:
     - Relatório CSV agora é salvo dentro da pasta de versão
     - Mensagem confirma localização do relatório
   
   - Modificação em `run_batch()`:
     - Relatório CSV agora é salvo dentro da pasta de versão
     - Mensagem confirma localização do relatório
   
   - Modificação em `main()`:
     - Melhor tratamento de parâmetros de saída
     - Suporta tanto caminho completo quanto nome base

### Como Funciona

**Primeira execução:**
```
Organizador_Revit_Organizado_R00/
  ├── Disciplina_1/
  ├── Disciplina_2/
  └── relatório_20250101_001000.csv
```

**Segunda execução:**
```
Organizador_Revit_Organizado_R00/  (anterior)
Organizador_Revit_Organizado_R01/  (novo)
  ├── Disciplina_1/
  ├── Disciplina_2/
  └── relatório_20250101_001500.csv
```

**Terceira execução:**
```
Organizador_Revit_Organizado_R00/  (anterior)
Organizador_Revit_Organizado_R01/  (anterior)
Organizador_Revit_Organizado_R02/  (novo)
  ├── Disciplina_1/
  ├── Disciplina_2/
  └── relatório_20250101_002000.csv
```

### Benefícios

✓ **Histórico completo**: Cada execução cria uma nova versão preservando as anteriores
✓ **Relatórios organizados**: CSV fica dentro da pasta versionada
✓ **Pronto para usar**: Pasta é auto-contida com tudo necessário
✓ **Sem conflitos**: Nunca sobrescreve versões anteriores
✓ **Numeração sequencial**: _R00, _R01, _R02... até _R99

### Uso

O programa continua funcionando da mesma forma:

```bash
# Modo dry-run
python main.py --workspace ./Organizador_Arquivos --dry-run

# Modo interativo
python main.py --workspace ./Organizador_Arquivos --interactive

# Modo batch
python main.py --workspace ./Organizador_Arquivos --batch --force
```

A pasta de saída será automaticamente criada com o próximo número de versão.

### Testes Realizados

✓ Extrair versão do nome da pasta
✓ Detectar pastas existentes e incrementar
✓ Formatar número com dois dígitos
✓ Múltiplas execuções sequenciais
✓ Relatórios salvos na pasta correta

