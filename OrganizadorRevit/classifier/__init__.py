"""
Classificador híbrido de famílias Revit.
Combina detecção automática (palavras-chave + regex) com opção de revisão manual.
"""

import re
from typing import Tuple, Optional, Dict, List
from pathlib import Path
import sys
from pathlib import Path as PathLib

# Adicionar diretório raiz ao path
sys.path.insert(0, str(PathLib(__file__).parent.parent))

from config.iso_structure import ISO_STRUCTURE, DISCIPLINE_CODES, TYPE_CODES
from config.classifier_keywords import CLASSIFIER_KEYWORDS, get_keywords


class RevitClassifier:
    """Classificador automático e interativo de famílias Revit."""
    
    def __init__(self):
        """Inicializa o classificador."""
        self.iso_structure = ISO_STRUCTURE
        
    def classify_file(self, filename: str) -> Tuple[Optional[str], Optional[str], float]:
        """
        Classifica um arquivo automaticamente.
        
        Args:
            filename: Nome do arquivo a classificar
        
        Returns:
            Tupla (disciplina, tipo_familia, confianca) onde:
            - disciplina: Nome da pasta raiz (ex: "04_HIDRAULICA")
            - tipo_familia: Nome da subfolder (ex: "04_Louças")
            - confianca: Score 0.0-1.0 indicando confiança da classificação
        """
        filename_lower = filename.lower()
        
        best_discipline = None
        best_type = None
        best_confidence = 0.0
        
        # Iterar por todas as disciplinas
        for discipline_name, discipline_data in self.iso_structure.items():
            subfolders = discipline_data.get("subfolders", {})
            
            # Iterar por tipos dentro da disciplina
            for subfolder_name in subfolders.keys():
                # Extrair o tipo base (ex: "Louças" de "04_Louças")
                type_base = subfolder_name.split("_", 1)[1] if "_" in subfolder_name else subfolder_name
                
                # Buscar keywords para esta combinação disciplina+tipo
                keywords = get_keywords(discipline_name.split("_", 1)[1], type_base)
                
                # Calcular confiança desta classificação
                confidence = self._calculate_confidence(filename_lower, keywords)
                
                # Atualizar melhor match se score for superior
                if confidence > best_confidence:
                    best_confidence = confidence
                    best_discipline = discipline_name
                    best_type = subfolder_name
        
        return best_discipline, best_type, best_confidence
    
    def _calculate_confidence(self, filename: str, keywords: dict) -> float:
        """
        Calcula score de confiança (0.0-1.0) baseado em palavras-chave e patterns.
        
        Args:
            filename: Nome do arquivo (em lowercase)
            keywords: Dict com 'high_confidence', 'medium_confidence', 'patterns'
        
        Returns:
            Score entre 0.0 e 1.0
        """
        confidence = 0.0
        
        # Verificar high confidence keywords (100% = 1.0 points)
        for keyword in keywords.get("high_confidence", []):
            if keyword in filename:
                confidence = max(confidence, 1.0)
                break  # Encontrou high confidence, máximo
        
        # Se não achou high confidence, verificar medium (70% = 0.7 points)
        if confidence < 1.0:
            for keyword in keywords.get("medium_confidence", []):
                if keyword in filename:
                    confidence = max(confidence, 0.7)
        
        # Se ainda não confiante, verificar patterns regex (40% = 0.4 points)
        if confidence < 0.7:
            for pattern in keywords.get("patterns", []):
                if re.search(pattern, filename, re.IGNORECASE):
                    confidence = max(confidence, 0.4)
        
        return confidence
    
    def get_all_classification_options(self) -> Dict[str, Dict[str, str]]:
        """
        Retorna todas as opções de classificação disponíveis.
        
        Returns:
            Dict estruturado com disciplinas e tipos
        """
        return self.iso_structure
    
    def get_disciplines(self) -> List[str]:
        """Retorna lista de disciplinas disponíveis."""
        return list(self.iso_structure.keys())
    
    def get_types_by_discipline(self, discipline: str) -> List[str]:
        """Retorna tipos disponíveis para uma disciplina."""
        if discipline in self.iso_structure:
            return list(self.iso_structure[discipline].get("subfolders", {}).keys())
        return []
    
    def classify_file_interactive(self, filename: str) -> Tuple[str, str]:
        """
        Classificação interativa com aprovação/correção do usuário.
        
        Args:
            filename: Nome do arquivo
        
        Returns:
            Tupla (disciplina, tipo_familia) aprovada pelo usuário
        """
        # Primeiro, tentar classificação automática
        discipline, type_family, confidence = self.classify_file(filename)
        
        print(f"\n{'='*70}")
        print(f"Arquivo: {filename}")
        print(f"{'='*70}")
        
        if discipline is None or confidence < 0.5:
            # Baixa confiança - pedir ao usuário
            print(f"⚠️  Classificação com baixa confiança (score: {confidence:.0%})")
            return self._ask_user_for_classification(filename)
        else:
            # Confiança aceitável - mostrar sugestão e permitir override
            print(f"✓ Classificação sugerida: {discipline} → {type_family}")
            print(f"  Confiança: {confidence:.0%}")
            
            response = input("\nAcei tar? (s/n/c para customizar): ").lower().strip()
            if response in ["s", ""]:
                return discipline, type_family
            elif response == "c":
                return self._ask_user_for_classification(filename)
            else:  # "n"
                return self._ask_user_for_classification(filename)
    
    def _ask_user_for_classification(self, filename: str) -> Tuple[str, str]:
        """Apresenta menu para usuário escolher disciplina e tipo."""
        disciplines = self.get_disciplines()
        
        # Escolher disciplina
        print("\nDisciplinas disponíveis:")
        for i, disc in enumerate(disciplines, 1):
            label = self.iso_structure[disc].get("label", disc)
            print(f"  {i}. {disc} - {label}")
        
        while True:
            try:
                choice = int(input("\nEscolha disciplina (número): ")) - 1
                if 0 <= choice < len(disciplines):
                    discipline = disciplines[choice]
                    break
            except ValueError:
                pass
            print("Opção inválida. Tente novamente.")
        
        # Escolher tipo
        types = self.get_types_by_discipline(discipline)
        print(f"\nTipos em {discipline}:")
        for i, type_family in enumerate(types, 1):
            description = self.iso_structure[discipline]["subfolders"].get(type_family, "")
            print(f"  {i}. {type_family}")
            if description:
                print(f"     {description}")
        
        while True:
            try:
                choice = int(input("\nEscolha tipo (número): ")) - 1
                if 0 <= choice < len(types):
                    type_family = types[choice]
                    break
            except ValueError:
                pass
            print("Opção inválida. Tente novamente.")
        
        return discipline, type_family
