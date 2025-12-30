"""
Configuração hardcoded da estrutura ISO 19650 para organização de famílias Revit.
Permite customização futura via arquivo JSON.
"""

ISO_STRUCTURE = {
    "01_PADROES_EMPRESA": {
        "label": "Padrões da Empresa",
        "subfolders": {
            "01_Blocos_Margens_Carimbo": "Blocos de margens, carimbos e elementos de página",
            "02_Folhas_Margens_Carimbo": "Folhas/pranchas pré-configuradas com margens e carimbos",
            "03_Cartouchos_Titulos": "Cartouchos, blocos de títulos e rótulos técnicos",
            "04_Legendas_Padrao": "Elementos de legenda padrão",
            "05_Selos_Governamentais": "Selos e elementos de órgãos públicos",
            "06_Elementos_Decorativos": "Elementos decorativos e de acabamento",
        }
    },
    "02_ARQUITETURA": {
        "label": "Arquitetura",
        "subfolders": {
            "01_Janelas": "Janelas (simples, duplas, correr, basculante, etc)",
            "02_Portas": "Portas (giro, duplas, pivotantes, automáticas, correr)",
            "03_Paredes": "Paredes (alvenaria, vidro, estruturais, divisórias)",
            "04_Telhas": "Telhas (cerâmica, concreto, metálica)",
            "05_Pisos": "Pisos (cerâmica, madeira, concreto, mármol)",
            "06_Acabamentos": "Acabamentos (rodapés, molduras, esquadrias)",
            "07_Mobiliario": "Mobiliário (mesas, cadeiras, armários, racks)",
            "08_Equipamentos": "Equipamentos (elevadores, escadas, rampas)",
        }
    },
    "03_ESTRUTURA": {
        "label": "Estrutura",
        "subfolders": {
            "01_Pilares": "Pilares (concreto, aço, alvenaria - várias seções)",
            "02_Vigas": "Vigas (concreto, aço - perfis I, U, T)",
            "03_Lajes": "Lajes (maciças, alveolares, cogumelo)",
            "04_Fundacoes": "Fundações (sapatas, blocos, baldrames, estacas)",
            "05_Escadas": "Escadas estruturais",
            "06_Secoes_Transversais": "Seções transversais padrão",
        }
    },
    "04_HIDRAULICA": {
        "label": "Hidráulica",
        "subfolders": {
            "01_Tubulacoes": "Tubulações (PVC, cobre, aço - vários diâmetros)",
            "02_Conexoes": "Conexões (joelhos, tês, reduções, flanges)",
            "03_Valvulas": "Válvulas (retenção, esfera, gaveta)",
            "04_Louças": "Louças sanitárias (vasos, cubas, bidês, mictórios)",
            "05_Torneiras": "Torneiras (cozinha, banheiro, monocomando, misturador)",
            "06_Acessorios": "Acessórios (sifões, cestos, ganchos)",
        }
    },
    "05_ELETRICA": {
        "label": "Elétrica",
        "subfolders": {
            "01_Distribuicao": "Quadros de distribuição e disjuntores",
            "02_Iluminacao": "Iluminação (arandelas, spots, pendentes, embutidas)",
            "03_Tomadas_Interruptores": "Tomadas e interruptores (simples, dupla, tripla, USB)",
            "04_Tubulacoes": "Tubulações e canaletas elétricas",
            "05_Dispositivos": "Dispositivos (sensores, timers, controles)",
        }
    },
    "06_HVAC": {
        "label": "HVAC - Ar Condicionado e Ventilação",
        "subfolders": {
            "01_Dutos": "Dutos (retangular, redondo - vários tamanhos)",
            "02_Difusores_Grelhas": "Difusores e grelhas de ar",
            "03_Equipamentos": "Equipamentos (compressores, condensadores)",
            "04_Valvulas_Controle": "Válvulas de controle",
            "05_Isolamento": "Isolamento de vibração",
            "06_Termostatos": "Termostatos e controles",
        }
    },
    "07_PAISAGISMO": {
        "label": "Paisagismo",
        "subfolders": {
            "01_Vegetacao": "Árvores, arbustos e plantas",
            "02_Mobiliario_Externo": "Elementos decorativos (bancos, lixeiras, fontes)",
            "03_Pavimentacao": "Pavimentação (blocos, lajotas, asfalto)",
            "04_Elementos_Agua": "Elementos de água (fontes, espelhos)",
            "05_Iluminacao_Externa": "Iluminação externa",
        }
    },
    "08_INTEGRACAO": {
        "label": "Integração e Coordenação",
        "subfolders": {
            "01_Modelo_Federado": "Modelos federados e coordenação",
            "02_Clash_Detection": "Clash detection e análise de conflitos",
            "03_Documentacao": "Documentação de integração",
        }
    },
    "09_ARQUIVO": {
        "label": "Arquivo e Descarte",
        "subfolders": {
            "01_Versoes_Anteriores": "Versões antigas descartadas (versionamento)",
            "02_Descartado": "Arquivos descartados ou obsoletos",
            "03_Historico": "Histórico e backups",
        }
    }
}

# Códigos de disciplina ISO 19650
DISCIPLINE_CODES = {
    "01_PADROES_EMPRESA": "AR",  # Padrões tratados como Arquitetura
    "02_ARQUITETURA": "AR",
    "03_ESTRUTURA": "ST",
    "04_HIDRAULICA": "HI",
    "05_ELETRICA": "EL",
    "06_HVAC": "HV",
    "07_PAISAGISMO": "LS",
    "08_INTEGRACAO": "IN",
    "09_ARQUIVO": "AR",
}

# Mapeamento de tipos (para geração de nomes ISO 19650)
TYPE_CODES = {
    "01_Blocos_Margens_Carimbo": "BLK",
    "02_Folhas_Margens_Carimbo": "FOL",
    "03_Cartouchos_Titulos": "CAR",
    "04_Legendas_Padrao": "LEG",
    "05_Selos_Governamentais": "SEL",
    "06_Elementos_Decorativos": "DEC",
    
    "01_Janelas": "JAN",
    "02_Portas": "POR",
    "03_Paredes": "PAR",
    "04_Telhas": "TEL",
    "05_Pisos": "PIS",
    "06_Acabamentos": "ACA",
    "07_Mobiliario": "MOB",
    "08_Equipamentos": "EQP",
    
    "01_Pilares": "PIL",
    "02_Vigas": "VIG",
    "03_Lajes": "LAJ",
    "04_Fundacoes": "FUN",
    "05_Escadas": "ESC",
    "06_Secoes_Transversais": "SEC",
    
    "01_Tubulacoes": "TUB",
    "02_Conexoes": "CON",
    "03_Valvulas": "VAL",
    "04_Louças": "LOA",
    "05_Torneiras": "TOR",
    "06_Acessorios": "ACS",
    
    "01_Distribuicao": "QDI",
    "02_Iluminacao": "ILU",
    "03_Tomadas_Interruptores": "TOM",
    "04_Tubulacoes": "TUB",
    "05_Dispositivos": "DIS",
    
    "01_Dutos": "DUT",
    "02_Difusores_Grelhas": "DIF",
    "03_Equipamentos": "EQP",
    "04_Valvulas_Controle": "VLC",
    "05_Isolamento": "ISO",
    "06_Termostatos": "TER",
    
    "01_Vegetacao": "VEG",
    "02_Mobiliario_Externo": "MOE",
    "03_Pavimentacao": "PAV",
    "04_Elementos_Agua": "AGU",
    "05_Iluminacao_Externa": "ILE",
    
    "01_Modelo_Federado": "MOD",
    "02_Clash_Detection": "CLS",
    "03_Documentacao": "DOC",
    
    "01_Versoes_Anteriores": "ARC",
    "02_Descartado": "DES",
    "03_Historico": "HIS",
}

def get_full_structure():
    """Retorna a estrutura completa ISO 19650."""
    return ISO_STRUCTURE

def get_discipline_code(folder_name):
    """Retorna o código de disciplina para uma pasta."""
    return DISCIPLINE_CODES.get(folder_name, "AR")

def get_type_code(subfolder_name):
    """Retorna o código de tipo para uma subpasta."""
    return TYPE_CODES.get(subfolder_name, "UNK")
