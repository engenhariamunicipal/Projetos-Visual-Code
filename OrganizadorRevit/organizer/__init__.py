"""
Organizador de famílias Revit conforme estrutura ISO 19650.
Gerencia movimentação, renomeação e limpeza de duplicatas.
"""

import os
import re
import shutil
from pathlib import Path
from datetime import datetime
from typing import Tuple, Optional, List
from dataclasses import dataclass
import sys

# Adicionar diretório raiz ao path
sys.path.insert(0, str(Path(__file__).parent.parent))

from config.iso_structure import ISO_STRUCTURE, DISCIPLINE_CODES, TYPE_CODES, get_type_code
from translator import FamilyTranslator

@dataclass
class OrganizationPlan:
    """Plano de reorganização para um arquivo."""
    original_path: Path
    original_name: str
    destination_folder: Path
    new_name: str
    discipline: str
    type_family: str
    action: str  # "move", "skip_duplicate", "skip_version"
    reason: str = ""


class RevitOrganizer:
    """Organizador de famílias Revit conforme ISO 19650."""
    
    def __init__(self, output_base: Path):
        """
        Inicializa o organizador.
        
        Args:
            output_base: Caminho base para a saída (ex: C:/Saida/Organizador_Revit)
        """
        self.output_base = Path(output_base)
        self.iso_structure = ISO_STRUCTURE
        self.translator = FamilyTranslator()
        
    def create_iso_structure(self):
        """Cria a estrutura de diretórios ISO 19650 na saída."""
        for discipline_name, discipline_data in self.iso_structure.items():
            discipline_path = self.output_base / discipline_name
            discipline_path.mkdir(parents=True, exist_ok=True)
            
            for subfolder_name in discipline_data.get("subfolders", {}).keys():
                subfolder_path = discipline_path / subfolder_name
                subfolder_path.mkdir(parents=True, exist_ok=True)
    
    def sanitize_filename(self, filename: str, max_length: int = 250) -> str:
        """
        Sanitiza um nome de arquivo removendo caracteres inválidos Windows.
        
        Args:
            filename: Nome original
            max_length: Tamanho máximo do nome final (sem caminho)
        
        Returns:
            Nome sanitizado e válido para Windows
        """
        # Caracteres inválidos em Windows: < > : " | ? * \
        invalid_chars = r'[<>:"|?*\\]'
        sanitized = re.sub(invalid_chars, '', filename)
        
        # Remover espaços múltiplos
        sanitized = re.sub(r'\s+', ' ', sanitized)
        
        # Truncar se necessário (mantendo extensão)
        if len(sanitized) > max_length:
            # Encontrar a última ocorrência de .rfa
            ext = ".rfa"
            if sanitized.endswith(ext):
                base = sanitized[:-len(ext)]
                base = base[:max_length - len(ext)]
                sanitized = base + ext
        
        return sanitized.strip()
    
    def extract_version_from_name(self, filename: str) -> str:
        """
        Extrai versão do nome do arquivo ou usa padrão.
        
        Args:
            filename: Nome do arquivo
        
        Returns:
            String de versão (ex: "v1.0")
        """
        # Procurar por padrão v[número].[número]
        match = re.search(r'v(\d+)\.(\d+)', filename, re.IGNORECASE)
        if match:
            return f"v{match.group(1)}.{match.group(2)}"
        
        # Se não encontrar, usar v1.0
        return "v1.0"
    
    def translate_description(self, description: str) -> str:
        """
        Traduz descrição para português.
        Usa apenas dicionário local para ser rápido.
        
        Args:
            description: Descrição original
            
        Returns:
            Descrição traduzida para português
        """
        # Traduzir apenas usando dicionário local (muito rápido)
        translation_dict = self.translator._simple_translation_dict()
        text_lower = description.lower()
        
        # Procura por correspondências exatas
        for word, translation in translation_dict.items():
            if text_lower == word:
                # Preservar maiúsculas/minúsculas do original
                if description and description[0].isupper():
                    return translation.capitalize()
                return translation
        
        # Procura por palavras-chave dentro do texto
        import re
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
            if description and description[0].isupper():
                result = result.capitalize()
            return result
        
        # Se não conseguiu traduzir, retorna original
        return description
    
    def generate_iso_name(
        self,
        original_name: str,
        discipline: str,
        type_family: str,
        version: Optional[str] = None,
        status: str = "P",
        timestamp: Optional[str] = None
    ) -> str:
        """
        Gera nome ISO 19650 para o arquivo.
        
        Padrão: [DisciplinaCode]-[TipoCode]-[Descrição]-v[Versão]-[Status]-[Data].rfa
        
        Args:
            original_name: Nome original do arquivo
            discipline: Disciplina (ex: "04_HIDRAULICA")
            type_family: Tipo de família (ex: "04_Louças")
            version: Versão (ex: "1.0"), usa padrão se None
            status: Status (W/S/P/A), padrão P (Published)
            timestamp: Data (YYYYMMDD), usa hoje se None
        
        Returns:
            Nome no padrão ISO 19650
        """
        # Extrair códigos
        discipline_code = DISCIPLINE_CODES.get(discipline, "AR")
        type_code = get_type_code(type_family)
        
        # Extrair versão do nome original se não fornecida
        if version is None:
            version = self.extract_version_from_name(original_name)
        
        # Limpar versão (remover prefixo 'v' se existir)
        version = version.lstrip("v")
        
        # Usar data hoje se não fornecida
        if timestamp is None:
            timestamp = datetime.now().strftime("%Y%m%d")
        
        # Extrair descrição (tudo antes de .rfa, removendo padrões versionados)
        base_name = original_name.replace(".rfa.rfa", ".rfa")
        base_name = re.sub(r'\.\d{4}\.rfa$', '.rfa', base_name)
        description = base_name[:-4]  # Remove .rfa
        
        # Traduzir descrição para português
        description = self.translate_description(description)
        
        # Sanitizar descrição
        description = self.sanitize_filename(description)
        
        # Montar nome ISO
        iso_name = f"{discipline_code}-{type_code}-{description}-v{version}-{status}-{timestamp}.rfa"
        
        # Sanitizar nome final
        iso_name = self.sanitize_filename(iso_name)
        
        return iso_name
    
    def plan_organization(
        self,
        file_path: Path,
        discipline: str,
        type_family: str,
        is_duplicate: bool = False,
        is_version_suffix: bool = False
    ) -> OrganizationPlan:
        """
        Cria um plano de organização para um arquivo.
        
        Args:
            file_path: Caminho completo do arquivo
            discipline: Disciplina destino
            type_family: Tipo de família destino
            is_duplicate: Se é duplicata de outro arquivo
            is_version_suffix: Se tem sufixo de versão (.0001 etc)
        
        Returns:
            OrganizationPlan com detalhes da operação
        """
        # Verificar se deve descartar (duplicata ou versão antiga)
        if is_duplicate or is_version_suffix:
            return OrganizationPlan(
                original_path=file_path,
                original_name=file_path.name,
                destination_folder=None,
                new_name=None,
                discipline=discipline,
                type_family=type_family,
                action="skip_duplicate",
                reason="Arquivo duplicado ou versão anterior - descartado conforme opção"
            )
        
        # Gerar novo nome ISO
        new_name = self.generate_iso_name(
            file_path.name,
            discipline,
            type_family
        )
        
        # Determinar pasta destino
        destination_folder = self.output_base / discipline / type_family
        
        return OrganizationPlan(
            original_path=file_path,
            original_name=file_path.name,
            destination_folder=destination_folder,
            new_name=new_name,
            discipline=discipline,
            type_family=type_family,
            action="move",
            reason="Reorganizado conforme ISO 19650"
        )
    
    def execute_plan(self, plan: OrganizationPlan, dry_run: bool = False) -> bool:
        """
        Executa o plano de organização.
        
        Args:
            plan: OrganizationPlan a executar
            dry_run: Se True, apenas simula sem alterar arquivos
        
        Returns:
            True se executado com sucesso, False caso contrário
        """
        if plan.action == "skip_duplicate":
            # Não fazer nada, apenas registrar
            return True
        
        if plan.action != "move":
            return False
        
        try:
            # Garantir que pasta destino existe
            plan.destination_folder.mkdir(parents=True, exist_ok=True)
            
            # Caminho destino final
            destination_path = plan.destination_folder / plan.new_name
            
            if not dry_run:
                # Copiar arquivo (não mover, preservar original)
                shutil.copy2(plan.original_path, destination_path)
            
            return True
        
        except Exception as e:
            print(f"  ❌ Erro ao processar {plan.original_name}: {e}")
            return False
