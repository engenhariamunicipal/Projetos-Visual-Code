"""
Tradutor de nomes de famílias para português.
Detecta o idioma e traduz automaticamente se necessário.
"""

import re
from typing import Tuple
import sys
from pathlib import Path

# Adicionar diretório raiz ao path
sys.path.insert(0, str(Path(__file__).parent.parent))


class FamilyTranslator:
    """Traduz nomes de famílias para português."""
    
    def __init__(self):
        """Inicializa o tradutor."""
        self.try_googletrans = True
        self.try_textblob = True
        
    def _try_googletrans(self, text: str) -> Tuple[str, str]:
        """
        Tenta usar googletrans para tradução.
        
        Args:
            text: Texto a traduzir
            
        Returns:
            (texto_traduzido, idioma_detectado)
        """
        try:
            from googletrans import Translator
            translator = Translator()
            detection = translator.detect(text)
            detected_lang = detection.lang
            
            # Se já é português, retorna original
            if detected_lang in ['pt', 'pt-BR', 'pt-PT']:
                return text, detected_lang
            
            # Traduz para português
            translation = translator.translate(text, src_language=detected_lang, dest_language='pt')
            return translation['text'], detected_lang
        except Exception as e:
            return None, None
    
    def _try_textblob(self, text: str) -> Tuple[str, str]:
        """
        Tenta usar textblob para tradução.
        
        Args:
            text: Texto a traduzir
            
        Returns:
            (texto_traduzido, idioma_detectado)
        """
        try:
            from textblob import TextBlob
            blob = TextBlob(text)
            detected_lang = blob.detect_language()
            
            # Se já é português, retorna original
            if detected_lang in ['pt', 'pt-BR', 'pt-PT']:
                return text, detected_lang
            
            # Traduz para português
            translated = blob.translate(from_lang=detected_lang, to_lang='pt')
            return str(translated), detected_lang
        except Exception as e:
            return None, None
    
    def _simple_translation_dict(self) -> dict:
        """
        Dicionário simples de tradução para palavras comuns em Revit.
        Útil quando APIs de tradução não estão disponíveis.
        """
        return {
            # Inglês
            'wall': 'parede',
            'door': 'porta',
            'window': 'janela',
            'floor': 'piso',
            'ceiling': 'teto',
            'roof': 'telhado',
            'column': 'coluna',
            'beam': 'viga',
            'railing': 'guarda-corpo',
            'stair': 'escada',
            'furniture': 'móvel',
            'fixture': 'acessório',
            'lighting': 'iluminação',
            'electrical': 'elétrico',
            'hvac': 'ar condicionado',
            'plumbing': 'hidráulica',
            'mechanical': 'mecânico',
            'structural': 'estrutural',
            'architectural': 'arquitetônico',
            'landscape': 'paisagismo',
            'generic': 'genérico',
            'standard': 'padrão',
            'custom': 'personalizado',
            'detail': 'detalhe',
            'assembly': 'montagem',
            'component': 'componente',
            'model': 'modelo',
            'profile': 'perfil',
            'section': 'seção',
            'elevation': 'elevação',
            'plan': 'plano',
            'view': 'vista',
            'sheet': 'prancha',
            'template': 'modelo',
            'border': 'moldura',
            'titleblock': 'carimbo',
            'schedule': 'tabela',
            'legend': 'legenda',
            'symbol': 'símbolo',
            'annotation': 'anotação',
            'text': 'texto',
            'dimension': 'dimensão',
            'line': 'linha',
            'curve': 'curva',
            'arc': 'arco',
            'circle': 'círculo',
            'rectangle': 'retângulo',
            'polygon': 'polígono',
            'solid': 'sólido',
            'surface': 'superfície',
            'void': 'vazio',
            'opening': 'abertura',
            'frame': 'moldura',
            'handle': 'alça',
            'knob': 'maçaneta',
            'lever': 'alavanca',
            'hinge': 'dobradiça',
            'bracket': 'suporte',
            'clamp': 'grampo',
            'connector': 'conector',
            'joint': 'junta',
            'seal': 'vedação',
            'gasket': 'gaxeta',
            'washer': 'arruela',
            'bolt': 'parafuso',
            'screw': 'rosca',
            'nail': 'prego',
            'rivet': 'rebite',
            'weld': 'solda',
            'braze': 'brasagem',
            'solder': 'soldadura',
            'glue': 'cola',
            'adhesive': 'adesivo',
            'paint': 'tinta',
            'finish': 'acabamento',
            'coating': 'revestimento',
            'material': 'material',
            'texture': 'textura',
            'pattern': 'padrão',
            'color': 'cor',
            'shade': 'tom',
            'tint': 'tonalidade',
            'opacity': 'opacidade',
            'transparency': 'transparência',
            'reflectivity': 'reflexibilidade',
            'roughness': 'rugosidade',
            'scale': 'escala',
            'size': 'tamanho',
            'dimension': 'dimensão',
            'width': 'largura',
            'height': 'altura',
            'depth': 'profundidade',
            'length': 'comprimento',
            'radius': 'raio',
            'diameter': 'diâmetro',
            'thickness': 'espessura',
            'weight': 'peso',
            'volume': 'volume',
            'area': 'área',
            'perimeter': 'perímetro',
            'angle': 'ângulo',
            'slope': 'inclinação',
            'pitch': 'inclinação',
            'rise': 'altura',
            'run': 'comprimento',
            'step': 'degrau',
            'tread': 'piso',
            'riser': 'espelho',
            'landing': 'patamar',
            'handrail': 'corrimão',
            'baluster': 'balaústre',
            'newel': 'coluna de escada',
            
            # Espanhol
            'pared': 'parede',
            'puerta': 'porta',
            'ventana': 'janela',
            'piso': 'piso',
            'techo': 'teto',
            'techo de paja': 'telhado',
            'columna': 'coluna',
            'viga': 'viga',
            'baranda': 'guarda-corpo',
            'escalera': 'escada',
            'mueble': 'móvel',
            'accesorio': 'acessório',
            'iluminación': 'iluminação',
            'eléctrico': 'elétrico',
            'aire acondicionado': 'ar condicionado',
            'fontanería': 'hidráulica',
            'mecánico': 'mecânico',
            'estructural': 'estrutural',
            'arquitectónico': 'arquitetônico',
            'paisajismo': 'paisagismo',
            'genérico': 'genérico',
            'estándar': 'padrão',
            'personalizado': 'personalizado',
            'detalle': 'detalhe',
            'montaje': 'montagem',
            'componente': 'componente',
            'modelo': 'modelo',
            'perfil': 'perfil',
            'sección': 'seção',
            'elevación': 'elevação',
            'plano': 'plano',
            'vista': 'vista',
            'lámina': 'prancha',
            'plantilla': 'modelo',
            'borde': 'moldura',
            'cartela': 'carimbo',
            'tabla': 'tabela',
            'leyenda': 'legenda',
            'símbolo': 'símbolo',
            'anotación': 'anotação',
            'texto': 'texto',
            'dimensión': 'dimensão',
            'línea': 'linha',
            'curva': 'curva',
            'arco': 'arco',
            'círculo': 'círculo',
            'rectángulo': 'retângulo',
            'polígono': 'polígono',
            'sólido': 'sólido',
            'superficie': 'superfície',
            'vacío': 'vazio',
            'abertura': 'abertura',
            'marco': 'moldura',
            'asa': 'alça',
            'pomo': 'maçaneta',
            'palanca': 'alavanca',
            'bisagra': 'dobradiça',
            'soporte': 'suporte',
            'abrazadera': 'grampo',
            'conector': 'conector',
            'junta': 'junta',
            'sello': 'vedação',
            'junta tórica': 'gaxeta',
            'arandela': 'arruela',
            'perno': 'parafuso',
            'tornillo': 'rosca',
            'clavo': 'prego',
            'remache': 'rebite',
            'soldadura': 'solda',
            'brasaje': 'brasagem',
            'soldadura blanda': 'soldadura',
            'pegamento': 'cola',
            'adhesivo': 'adesivo',
            'pintura': 'tinta',
            'acabado': 'acabamento',
            'revestimiento': 'revestimento',
            'material': 'material',
            'textura': 'textura',
            'patrón': 'padrão',
            'color': 'cor',
            'matiz': 'tom',
            'tonalidad': 'tonalidade',
            'opacidad': 'opacidade',
            'transparencia': 'transparência',
            'reflectividad': 'reflexibilidade',
            'rugosidad': 'rugosidade',
            'escala': 'escala',
            'tamaño': 'tamanho',
            'ancho': 'largura',
            'alto': 'altura',
            'profundidad': 'profundidade',
            'largo': 'comprimento',
            'radio': 'raio',
            'diámetro': 'diâmetro',
            'grosor': 'espessura',
            'peso': 'peso',
            'volumen': 'volume',
            'área': 'área',
            'perímetro': 'perímetro',
            'ángulo': 'ângulo',
            'pendiente': 'inclinação',
            'inclinación': 'inclinação',
            'subida': 'altura',
            'recorrido': 'comprimento',
            'paso': 'degrau',
            'huella': 'piso',
            'contrahuella': 'espelho',
            'descanso': 'patamar',
            'pasamano': 'corrimão',
            'balaustrada': 'balaústre',
            'inicio': 'coluna de escada',
            
            # Francês
            'mur': 'parede',
            'porte': 'porta',
            'fenetre': 'janela',
            'fenêtre': 'janela',
            'sol': 'piso',
            'plafond': 'teto',
            'toit': 'telhado',
            'colonne': 'coluna',
            'poutre': 'viga',
            'balustrade': 'guarda-corpo',
            'escalier': 'escada',
            'meuble': 'móvel',
            'accessoire': 'acessório',
            'eclairage': 'iluminação',
            'electrique': 'elétrico',
            'climatisation': 'ar condicionado',
            'plomberie': 'hidráulica',
            'mecanique': 'mecânico',
            'structural': 'estrutural',
            'architectural': 'arquitetônico',
            'paysagisme': 'paisagismo',
            'generique': 'genérico',
            'standard': 'padrão',
            'personnalise': 'personalizado',
            'detail': 'detalhe',
            'montage': 'montagem',
            'composant': 'componente',
            'modele': 'modelo',
            'modèle': 'modelo',
            'profil': 'perfil',
            'section': 'seção',
            'elevation': 'elevação',
            'élévation': 'elevação',
            'plan': 'plano',
            'vue': 'vista',
            'feuille': 'prancha',
            'modele de base': 'modelo',
            'bordure': 'moldura',
            'cartouche': 'carimbo',
            'tableau': 'tabela',
            'legende': 'legenda',
            'légende': 'legenda',
            'symbole': 'símbolo',
            'annotation': 'anotação',
            'texte': 'texto',
            'dimension': 'dimensão',
            'ligne': 'linha',
            'courbe': 'curva',
            'arc': 'arco',
            'cercle': 'círculo',
            'rectangle': 'retângulo',
            'polygone': 'polígono',
            'solide': 'sólido',
            'surface': 'superfície',
            'vide': 'vazio',
            'ouverture': 'abertura',
            'cadre': 'moldura',
            'poignee': 'alça',
            'poignée': 'alça',
            'bouton': 'maçaneta',
            'levier': 'alavanca',
            'charniere': 'dobradiça',
            'support': 'suporte',
            'pince': 'grampo',
            'connecteur': 'conector',
            'joint': 'junta',
            'sceau': 'vedação',
            'joint torique': 'gaxeta',
            'rondelle': 'arruela',
            'boulon': 'parafuso',
            'vis': 'rosca',
            'clou': 'prego',
            'rivet': 'rebite',
            'soudure': 'solda',
            'brasage': 'brasagem',
            'soudure tendre': 'soldadura',
            'colle': 'cola',
            'adhesif': 'adesivo',
            'peinture': 'tinta',
            'finition': 'acabamento',
            'revetement': 'revestimento',
            'revêtement': 'revestimento',
            'materiau': 'material',
            'matériau': 'material',
            'texture': 'textura',
            'motif': 'padrão',
            'couleur': 'cor',
            'teinte': 'tom',
            'nuance': 'tonalidade',
            'opacite': 'opacidade',
            'opacité': 'opacidade',
            'transparence': 'transparência',
            'reflexivite': 'reflexibilidade',
            'rugosité': 'rugosidade',
            'echelle': 'escala',
            'taille': 'tamanho',
            'largeur': 'largura',
            'hauteur': 'altura',
            'profondeur': 'profundidade',
            'longueur': 'comprimento',
            'rayon': 'raio',
            'diametre': 'diâmetro',
            'diamètre': 'diâmetro',
            'epaisseur': 'espessura',
            'poids': 'peso',
            'volume': 'volume',
            'surface': 'área',
            'perimetre': 'perímetro',
            'angle': 'ângulo',
            'pente': 'inclinação',
            'montee': 'altura',
            'parcours': 'comprimento',
            'marche': 'degrau',
            'giron': 'piso',
            'contremarche': 'espelho',
            'palier': 'patamar',
            'main courante': 'corrimão',
            'balustre': 'balaústre',
            'noyau': 'coluna de escada',
        }
    
    def translate(self, text: str) -> Tuple[str, str, str]:
        """
        Traduz texto para português se necessário.
        Usa dicionário local primeiro (rápido), depois APIs se necessário.
        
        Args:
            text: Texto a traduzir
            
        Returns:
            (texto_traduzido, idioma_detectado, método_usado)
        """
        if not text or len(text.strip()) == 0:
            return text, "vazio", "nenhum"
        
        text = text.strip()
        
        # 1. Tentar dicionário local (MUITO mais rápido)
        translation_dict = self._simple_translation_dict()
        text_lower = text.lower()
        
        # Procura por correspondências exatas
        for word, translation in translation_dict.items():
            if text_lower == word:
                # Preservar maiúsculas/minúsculas do original
                if text[0].isupper():
                    return translation.capitalize(), "manual", "dicionário"
                return translation, "manual", "dicionário"
        
        # Procura por palavras-chave dentro do texto
        translated_parts = []
        words = text_lower.split()
        found_any = False
        
        for word in words:
            # Remover pontuação
            clean_word = re.sub(r'[^\w\s-]', '', word)
            if clean_word in translation_dict:
                translated_parts.append(translation_dict[clean_word])
                found_any = True
            else:
                translated_parts.append(word)
        
        if found_any:
            result = ' '.join(translated_parts)
            # Preservar maiúsculas do original
            if text[0].isupper():
                result = result.capitalize()
            return result, "manual", "dicionário (parcial)"
        
        # 2. Tentar googletrans (mais lento)
        translated, lang = self._try_googletrans(text)
        if translated:
            return translated, lang, "googletrans"
        
        # 3. Tentar textblob
        translated, lang = self._try_textblob(text)
        if translated:
            return translated, lang, "textblob"
        
        # 4. Se não conseguir traduzir, retorna original
        return text, "desconhecido", "sem tradução"


def translate_family_name(family_name: str) -> str:
    """
    Função auxiliar para traduzir nome de família.
    
    Args:
        family_name: Nome da família
        
    Returns:
        Nome traduzido para português
    """
    translator = FamilyTranslator()
    translated, lang, method = translator.translate(family_name)
    return translated
