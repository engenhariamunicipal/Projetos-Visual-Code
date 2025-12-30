"""
Dicionário de palavras-chave para classificação automática de famílias Revit.
Organizado por disciplina e tipo de família.
"""

CLASSIFIER_KEYWORDS = {
    # ==================== PADRÕES DA EMPRESA ====================
    "PADROES_EMPRESA": {
        "Blocos_Margens_Carimbo": {
            "high_confidence": ["margem", "margin", "bloco", "block", "a0", "a1", "a2", "a3", "a4"],
            "medium_confidence": ["em branco", "blank", "tamanho"],
            "patterns": [r"^[Aa][0-4]\s+\d+", r"^[Aa][0-4]\s+(?:em\s+branco|m[ée]trico)"],
        },
        "Folhas_Margens_Carimbo": {
            "high_confidence": ["folha", "sheet", "prancha", "layout", "formato"],
            "medium_confidence": ["a0", "a1", "a2", "a3", "a4", "abnt"],
            "patterns": [r"folha.*(?:selo|receita|prefeitura)", r"prancha.*(?:prefeitura|stand)"],
        },
        "Cartouchos_Titulos": {
            "high_confidence": ["cartouche", "cartuchos", "carimbo", "título", "title block", "titleblock"],
            "medium_confidence": ["rótulo", "label", "revisão", "révision"],
            "patterns": [r"cartouche\s*[—-]?\s*\d+", r"carimbo.*(?:bim|revit)"],
        },
        "Legendas_Padrao": {
            "high_confidence": ["legenda", "legend", "chave", "key"],
            "medium_confidence": ["clara", "pequena", "padrão"],
            "patterns": [r"legenda\s+(?:clara|pequena|pmjp)"],
        },
        "Selos_Governamentais": {
            "high_confidence": ["selo", "prefeitura", "receita", "federal", "jacareí"],
            "medium_confidence": ["governo", "público", "municipal"],
            "patterns": [r"(?:selo|prefeitura)\s+(?:jacareí|pmjp|receita)"],
        },
        "Elementos_Decorativos": {
            "high_confidence": ["guarda", "corrimão", "decorativo", "elemento", "diversas"],
            "medium_confidence": ["acabamento", "ornamental"],
            "patterns": [r"guarda_corpo", r"diversas\s+\d+"],
        },
    },
    
    # ==================== ARQUITETURA ====================
    "ARQUITETURA": {
        "Janelas": {
            "high_confidence": ["janela", "window", "vidro", "glass"],
            "medium_confidence": ["correr", "basculante", "pivotante", "alumínio"],
            "patterns": [r"jan\w*(?:.*(?:correr|basculante|pivotante|dupla|simples))?"],
        },
        "Portas": {
            "high_confidence": ["porta", "door", "giro", "pivotante"],
            "medium_confidence": ["dupla", "automática", "correr", "madeira"],
            "patterns": [r"por(?:ta)?(?:.*(?:giro|dupla|automática))?"],
        },
        "Paredes": {
            "high_confidence": ["parede", "wall", "alvenaria", "vidro", "divisória"],
            "medium_confidence": ["estrutural", "cortina"],
            "patterns": [r"par(?:ede)?(?:.*(?:alvenaria|vidro|divisória))?"],
        },
        "Telhas": {
            "high_confidence": ["telha", "tile", "cobertura", "roof", "cerâmica"],
            "medium_confidence": ["concreto", "metálica", "amianto"],
            "patterns": [r"telha(?:.*(?:cerâmica|concreto|metálica))?"],
        },
        "Pisos": {
            "high_confidence": ["piso", "floor", "cerâmica", "madeira", "concreto"],
            "medium_confidence": ["porcelanato", "mármol", "granito"],
            "patterns": [r"piso(?:.*(?:cerâmica|madeira|concreto))?"],
        },
        "Acabamentos": {
            "high_confidence": ["rodapé", "moldura", "esquadria", "acabamento", "trim"],
            "medium_confidence": ["batente", "marco"],
            "patterns": [r"rodapé|moldura|esquadria"],
        },
        "Mobiliario": {
            "high_confidence": ["mobiliário", "furniture", "mesa", "cadeira", "armário", "rack"],
            "medium_confidence": ["estante", "prateleira", "bancada"],
            "patterns": [r"mob(?:iliário)?|mesa|cadeira|arm[áa]rio"],
        },
        "Equipamentos": {
            "high_confidence": ["elevador", "escada", "rampa", "equipment", "ascensor"],
            "medium_confidence": ["escalável", "escadaria"],
            "patterns": [r"elevador|escada|rampa"],
        },
    },
    
    # ==================== ESTRUTURA ====================
    "ESTRUTURA": {
        "Pilares": {
            "high_confidence": ["pilar", "column", "pilastra"],
            "medium_confidence": ["concreto", "aço", "alvenaria"],
            "patterns": [r"pil(?:ar)?(?:.*(?:concreto|aço|alvenaria))?"],
        },
        "Vigas": {
            "high_confidence": ["viga", "beam", "vão"],
            "medium_confidence": ["concreto", "aço", "perfil"],
            "patterns": [r"vig(?:a)?(?:.*(?:concreto|aço|perfil))?"],
        },
        "Lajes": {
            "high_confidence": ["laje", "slab", "piso estrutural"],
            "medium_confidence": ["maciça", "alveolar", "cogumelo"],
            "patterns": [r"laj(?:e)?(?:.*(?:maciça|alveolar|cogumelo))?"],
        },
        "Fundacoes": {
            "high_confidence": ["fundação", "foundation", "sapata", "bloco", "estaquia"],
            "medium_confidence": ["baldrame", "estaca"],
            "patterns": [r"fund(?:ação)?|sapata|bloco"],
        },
        "Escadas": {
            "high_confidence": ["escada estrutural", "escada"],
            "medium_confidence": ["degrau", "lanço"],
            "patterns": [r"escada(?:.*estrutural)?"],
        },
        "Secoes_Transversais": {
            "high_confidence": ["seção", "section", "corte", "perfil"],
            "medium_confidence": ["transversal"],
            "patterns": [r"seção|section|corte"],
        },
    },
    
    # ==================== HIDRÁULICA ====================
    "HIDRAULICA": {
        "Tubulacoes": {
            "high_confidence": ["tubulação", "tubo", "pipe", "pvc", "cobre", "aço", "ø"],
            "medium_confidence": ["diâmetro", "dn"],
            "patterns": [r"tub(?:ulação)?(?:.*(?:pvc|cobre|aço))?|(?:dn|ø)\s*\d+"],
        },
        "Conexoes": {
            "high_confidence": ["conexão", "connection", "joelho", "tê", "redução", "flange"],
            "medium_confidence": ["acoplamento", "nipo"],
            "patterns": [r"(?:joelho|tê|redução|flange|conexão)"],
        },
        "Valvulas": {
            "high_confidence": ["válvula", "valve", "esfera", "retenção", "gaveta", "reguladora"],
            "medium_confidence": ["bloqueio", "controle"],
            "patterns": [r"válvula(?:.*(?:esfera|retenção|gaveta|reguladora))?"],
        },
        "Louças": {
            "high_confidence": ["louça", "vaso", "cuba", "lavatório", "lavatorio", "bidê", "mictório", "sanitário", "fixture", "bowl"],
            "medium_confidence": ["cerâmica", "porcelana", "branco"],
            "patterns": [r"(?:louça|vaso|cuba|lavatório|lavatorio|bidê|mictório|sanitário)"],
        },
        "Torneiras": {
            "high_confidence": ["torneira", "faucet", "monocomando", "misturador", "bica", "boca"],
            "medium_confidence": ["cromado", "polida", "escovada"],
            "patterns": [r"torneira|monocomando|misturador"],
        },
        "Acessorios": {
            "high_confidence": ["acessório", "sifão", "cesto", "gancho", "suporte"],
            "medium_confidence": ["engate", "rosca"],
            "patterns": [r"(?:sifão|cesto|gancho|suporte|acessório)"],
        },
    },
    
    # ==================== ELÉTRICA ====================
    "ELETRICA": {
        "Distribuicao": {
            "high_confidence": ["quadro", "distribuição", "painel", "disjuntor", "breaker"],
            "medium_confidence": ["amp", "a", "trifásico"],
            "patterns": [r"quadro(?:.*distribuição)?|\d+\s*[aA](?:mp)?"],
        },
        "Iluminacao": {
            "high_confidence": ["iluminação", "lighting", "lâmpada", "arandela", "spot", "pendente", "embutida"],
            "medium_confidence": ["led", "fluorescente", "incandescente"],
            "patterns": [r"(?:iluminação|arandela|spot|pendente|embutida|lâmpada)"],
        },
        "Tomadas_Interruptores": {
            "high_confidence": ["tomada", "outlet", "interruptor", "switch", "dupla", "tripla", "usb"],
            "medium_confidence": ["simples", "branca", "preta"],
            "patterns": [r"(?:tomada|interruptor|switch)(?:.*(?:dupla|tripla|usb))?"],
        },
        "Tubulacoes": {
            "high_confidence": ["canaleta", "eletroduto", "tubo elétrico", "conduit"],
            "medium_confidence": ["pvc", "galvanizado"],
            "patterns": [r"(?:canaleta|eletroduto|tubo.*elétrico|conduit)"],
        },
        "Dispositivos": {
            "high_confidence": ["sensor", "timer", "relé", "controle", "detector", "botão"],
            "medium_confidence": ["movimento", "presença", "emergência"],
            "patterns": [r"(?:sensor|timer|relé|detector|botão)"],
        },
    },
    
    # ==================== HVAC ====================
    "HVAC": {
        "Dutos": {
            "high_confidence": ["duto", "duct", "retangular", "redondo", "circular", "galvanizado"],
            "medium_confidence": ["flexível", "isolado"],
            "patterns": [r"duto(?:.*(?:retangular|redondo|circular))?"],
        },
        "Difusores_Grelhas": {
            "high_confidence": ["difusor", "grelha", "diffuser", "grille", "saída", "entrada"],
            "medium_confidence": ["redondo", "quadrado"],
            "patterns": [r"(?:difusor|grelha|saída|entrada)"],
        },
        "Equipamentos": {
            "high_confidence": ["compressor", "condensador", "evaporador", "unidade", "equipamento"],
            "medium_confidence": ["split", "inverter"],
            "patterns": [r"(?:compressor|condensador|evaporador|equipamento)"],
        },
        "Valvulas_Controle": {
            "high_confidence": ["válvula", "valve", "expansão", "retenção", "controle"],
            "medium_confidence": ["termostática"],
            "patterns": [r"válvula(?:.*(?:expansão|retenção|controle))?"],
        },
        "Isolamento": {
            "high_confidence": ["isolamento", "vibração", "vibration", "amortecedor"],
            "medium_confidence": ["borracha", "metal"],
            "patterns": [r"(?:isolamento|vibração|amortecedor)"],
        },
        "Termostatos": {
            "high_confidence": ["termostato", "controle de temperatura", "thermostat"],
            "medium_confidence": ["digital", "analógico"],
            "patterns": [r"termostato|controle.*temperatura"],
        },
    },
    
    # ==================== PAISAGISMO ====================
    "PAISAGISMO": {
        "Vegetacao": {
            "high_confidence": ["árvore", "tree", "arbusto", "planta", "plant", "vegetação"],
            "medium_confidence": ["espécie", "palmeira", "conífera"],
            "patterns": [r"(?:árvore|arbusto|planta|vegetação)"],
        },
        "Mobiliario_Externo": {
            "high_confidence": ["banco", "bench", "lixeira", "trash", "fonte", "fountain", "decorativo"],
            "medium_confidence": ["elemento", "mobiliário externo"],
            "patterns": [r"(?:banco|lixeira|fonte|decorativo)"],
        },
        "Pavimentacao": {
            "high_confidence": ["pavimentação", "paving", "bloco", "lajota", "asfalto", "concreto"],
            "medium_confidence": ["intertravado", "argamassa"],
            "patterns": [r"(?:pavimentação|bloco|lajota|asfalto)"],
        },
        "Elementos_Agua": {
            "high_confidence": ["água", "water", "fonte", "espelho", "lago", "açude", "cascata"],
            "medium_confidence": ["hidráulico"],
            "patterns": [r"(?:água|fonte|espelho|lago|cascata)"],
        },
        "Iluminacao_Externa": {
            "high_confidence": ["iluminação externa", "external lighting", "poste", "luminárias"],
            "medium_confidence": ["solar", "led"],
            "patterns": [r"(?:iluminação.*externa|poste|luminária)"],
        },
    },
}

def get_keywords(discipline, family_type):
    """
    Retorna o dicionário de palavras-chave para uma disciplina e tipo específicos.
    
    Args:
        discipline: Nome da disciplina (ex: "HIDRAULICA")
        family_type: Nome do tipo de família (ex: "Louças")
    
    Returns:
        Dict com 'high_confidence', 'medium_confidence' e 'patterns'
    """
    if discipline in CLASSIFIER_KEYWORDS:
        if family_type in CLASSIFIER_KEYWORDS[discipline]:
            return CLASSIFIER_KEYWORDS[discipline][family_type]
    return {"high_confidence": [], "medium_confidence": [], "patterns": []}
