# 📊 EXEMPLO DE OUTPUT E ESTRUTURA FINAL

## Resultado do --dry-run (300 arquivos)

```
======================================================================
MODO DRY-RUN (simulação sem alterar arquivos)
======================================================================

📂 Escaneando arquivos...
✓ Encontrados 300 arquivos .rfa
  - Tamanho total: 74.06 MB
  - Extensões duplas (.rfa.rfa): 64
  - Com sufixo de versão (.0001-.0020): 37
  - Duplicatas estimadas: 160

📁 Estrutura ISO 19650 será criada em: Organizador_Revit_Organizado

🔍 Classificando arquivos (isto pode levar alguns minutos)...

Classificação: 100%|██████████████████████████████████████| 300/300 [00:00<00:00, 4300arquivo/s]

======================================================================
RESUMO DO DRY-RUN
======================================================================
Total de arquivos: 300
Serão movidos: 199
Serão descartados (duplicatas/versões): 101

======================================================================

Próximo passo: Execute com --interactive para confirmar classificações
Ou use --batch para processar automaticamente (requer --force)

✓ Programa finalizado com sucesso!
```

---

## Estrutura de Saída Criada

```
Organizador_Revit_Organizado/
│
├── 01_PADROES_EMPRESA/
│   ├── 01_Blocos_Margens_Carimbo/
│   │   ├── AR-BLK-A0_01-v1.0-P-20250130.rfa
│   │   ├── AR-BLK-A0_02-v1.0-P-20250130.rfa
│   │   ├── AR-BLK-A1_01-v1.0-P-20250130.rfa
│   │   ├── AR-BLK-A1_02-v1.0-P-20250130.rfa
│   │   ├── AR-BLK-A1_em_branco-v1.0-P-20250130.rfa
│   │   └── ... (múltiplos formatos A0-A4)
│   │
│   ├── 02_Folhas_Margens_Carimbo/
│   │   ├── AR-FOL-A0_05-v1.0-P-20250130.rfa
│   │   ├── AR-FOL-A1_02-v1.0-P-20250130.rfa
│   │   ├── AR-FOL-Folha_com_selo_receita-v1.0-P-20250130.rfa
│   │   └── ...
│   │
│   ├── 03_Cartouchos_Titulos/
│   │   ├── AR-CAR-Cartouche_Padrão-v1.0-P-20250130.rfa
│   │   ├── AR-CAR-Cartouche_com_revisoes-v1.0-P-20250130.rfa
│   │   └── ...
│   │
│   ├── 04_Legendas_Padrao/
│   │   ├── AR-LEG-Legenda_Clara-v1.0-P-20250130.rfa
│   │   ├── AR-LEG-Legenda_Pequena-v1.0-P-20250130.rfa
│   │   ├── AR-LEG-Legenda_PMJP-v1.0-P-20250130.rfa
│   │   └── ...
│   │
│   ├── 05_Selos_Governamentais/
│   │   ├── AR-SEL-Prefeitura_Jacareí-v1.0-P-20250130.rfa
│   │   ├── AR-SEL-Receita_Federal-v1.0-P-20250130.rfa
│   │   └── ...
│   │
│   └── 06_Elementos_Decorativos/
│       ├── AR-DEC-Guarda_corpo_faustolo-v1.0-P-20250130.rfa
│       ├── AR-DEC-Diversas_01-v1.0-P-20250130.rfa
│       └── ...
│
├── 02_ARQUITETURA/
│   ├── 01_Janelas/
│   │   ├── AR-JAN-[descrição]-v[versão]-P-20250130.rfa
│   │   └── ... (se houver)
│   ├── 02_Portas/
│   ├── 03_Paredes/
│   ├── 04_Telhas/
│   ├── 05_Pisos/
│   ├── 06_Acabamentos/
│   ├── 07_Mobiliario/
│   └── 08_Equipamentos/
│
├── 03_ESTRUTURA/
│   ├── 01_Pilares/
│   ├── 02_Vigas/
│   ├── 03_Lajes/
│   ├── 04_Fundacoes/
│   ├── 05_Escadas/
│   └── 06_Secoes_Transversais/
│
├── 04_HIDRAULICA/
│   ├── 01_Tubulacoes/
│   │   └── HI-TUB-[descrição]-v[versão]-P-20250130.rfa
│   ├── 02_Conexoes/
│   ├── 03_Valvulas/
│   ├── 04_Louças/
│   │   └── HI-LOA-Vaso_Cerâmica-v1.0-P-20250130.rfa
│   ├── 05_Torneiras/
│   │   └── HI-TOR-Monocomando_Bica-v1.0-P-20250130.rfa
│   └── 06_Acessorios/
│
├── 05_ELETRICA/
│   ├── 01_Distribuicao/
│   ├── 02_Iluminacao/
│   ├── 03_Tomadas_Interruptores/
│   ├── 04_Tubulacoes/
│   └── 05_Dispositivos/
│
├── 06_HVAC/
│   ├── 01_Dutos/
│   ├── 02_Difusores_Grelhas/
│   ├── 03_Equipamentos/
│   ├── 04_Valvulas_Controle/
│   ├── 05_Isolamento/
│   └── 06_Termostatos/
│
├── 07_PAISAGISMO/
│   ├── 01_Vegetacao/
│   ├── 02_Mobiliario_Externo/
│   ├── 03_Pavimentacao/
│   ├── 04_Elementos_Agua/
│   └── 05_Iluminacao_Externa/
│
├── 08_INTEGRACAO/
│   ├── 01_Modelo_Federado/
│   ├── 02_Clash_Detection/
│   └── 03_Documentacao/
│
└── 09_ARQUIVO/
    └── 01_Versoes_Anteriores/
        ├── AR-BLK-A0_01-v1.0-P-20250129.rfa
        ├── HI-LOA-Vaso_Cerâmica-v0.9-P-20250128.rfa
        └── ... (arquivos descartados/versões antigas)
```

---

## Exemplo de Relatório CSV Gerado

```csv
Arquivo_Original,Caminho_Origem,Arquivo_Novo,Pasta_Destino,Disciplina,Tipo_Familia,Acao,Motivo,Data_Geracao
"A0 01.rfa","C:\...\Blocos de margens e carimbo","AR-BLK-A0_01-v1.0-P-20250130.rfa","...\01_PADROES_EMPRESA\01_Blocos_Margens_Carimbo","01 PADROES EMPRESA","01 Blocos Margens Carimbo","Move","Reorganizado conforme ISO 19650",20250130_143022
"A0 01.rfa.rfa","C:\...\Blocos de margens e carimbo","[Descartado]","[N/A]","01 PADROES EMPRESA","01 Blocos Margens Carimbo","Skip Duplicate","Arquivo duplicado ou versão anterior - descartado conforme opção",20250130_143022
"A1 01.0001.rfa","C:\...\Pranchas","[Descartado]","[N/A]","02 ARQUITETURA","01 Janelas","Skip Duplicate","Arquivo duplicado ou versão anterior - descartado conforme opção",20250130_143022
"Cartouche - 01.rfa","C:\...\Blocos de margens e carimbo","AR-CAR-Cartouche_Padrão-v1.0-P-20250130.rfa","...\01_PADROES_EMPRESA\03_Cartouchos_Titulos","01 PADROES EMPRESA","03 Cartouchos Titulos","Move","Reorganizado conforme ISO 19650",20250130_143022
"Legenda Clara.rfa","C:\...\Formatos e carimbos","AR-LEG-Legenda_Clara-v1.0-P-20250130.rfa","...\01_PADROES_EMPRESA\04_Legendas_Padrao","01 PADROES EMPRESA","04 Legendas Padrao","Move","Reorganizado conforme ISO 19650",20250130_143022
"Tubulação PVC Ø50.rfa","C:\...\diversos","HI-TUB-Tubulacao_PVC_50mm-v1.0-P-20250130.rfa","...\04_HIDRAULICA\01_Tubulacoes","04 HIDRAULICA","01 Tubulacoes","Move","Reorganizado conforme ISO 19650",20250130_143022
"Vaso Cerâmica.rfa","C:\...\diversos","HI-LOA-Vaso_Cerâmica-v1.0-P-20250130.rfa","...\04_HIDRAULICA\04_Louças","04 HIDRAULICA","04 Louças","Move","Reorganizado conforme ISO 19650",20250130_143022
```

---

## Exemplos de Nomes Renomeados

| Original | Novo Nome | Disciplina | Tipo |
|----------|-----------|-----------|------|
| `A0 01.rfa` | `AR-BLK-A0_01-v1.0-P-20250130.rfa` | Padrões Empresa | Blocos |
| `Cartouche - 01.rfa` | `AR-CAR-Cartouche_01-v1.0-P-20250130.rfa` | Padrões Empresa | Cartouchos |
| `Legenda Clara.rfa` | `AR-LEG-Legenda_Clara-v1.0-P-20250130.rfa` | Padrões Empresa | Legendas |
| `Tubulação PVC.rfa` | `HI-TUB-Tubulacao_PVC-v1.0-P-20250130.rfa` | Hidráulica | Tubulações |
| `Vaso Cerâmica.rfa` | `HI-LOA-Vaso_Cerâmica-v1.0-P-20250130.rfa` | Hidráulica | Louças |
| `Torneira Gourmet.rfa` | `HI-TOR-Torneira_Gourmet-v1.0-P-20250130.rfa` | Hidráulica | Torneiras |

---

## Códigos Utilizados

### Disciplinas (primeiro código)
- **AR** = Arquitetura
- **ST** = Estrutura
- **HI** = Hidráulica
- **EL** = Elétrica
- **HV** = HVAC
- **LS** = Paisagismo (Landscape)
- **IN** = Integração
- **SF** = Segurança (Safety/Fire)

### Tipos (segundo código) - Exemplos
- **BLK** = Blocos (Margens/Carimbos)
- **CAR** = Cartouchos
- **LEG** = Legendas
- **TUB** = Tubulações
- **LOA** = Louças
- **TOR** = Torneiras
- **VAL** = Válvulas
- **JAN** = Janelas

---

## Estatísticas Esperadas

```
Total de arquivos: 300
Arquivos a mover: 199 (66%)
Arquivos a descartar: 101 (34%)
  - .rfa.rfa: 64
  - Versões (.0001-.0020): 37

Tamanho total: 74.06 MB
Tempo de processamento: ~30 segundos (modo interativo) a 2 minutos (batch)
Relatório gerado em CSV
```

---

**Padrão ISO 19650 • ISO 9001**  
**Gerado automaticamente pelo Organizador de Famílias Revit**
