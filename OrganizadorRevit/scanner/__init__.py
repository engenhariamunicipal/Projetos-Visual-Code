"""
Scanner recursivo para varrer arquivos Revit (.rfa) em todas as subpastas.
"""

import os
import hashlib
import re
from pathlib import Path
from dataclasses import dataclass
from typing import List, Optional, Dict

@dataclass
class FileMetadata:
    """Metadados de um arquivo escaneado."""
    path: Path  # Caminho completo
    name: str  # Nome do arquivo
    extension: str  # Extensão (.rfa)
    size: int  # Tamanho em bytes
    parent_folder: str  # Pasta pai imediata
    is_duplicate_ext: bool = False  # Se tem extensão dupla .rfa.rfa
    has_version_suffix: bool = False  # Se tem sufixo de versão (.0001-.0020)
    version_suffix: Optional[str] = None  # O sufixo de versão detectado
    
    def __post_init__(self):
        # Detectar extensão dupla
        if self.name.endswith(".rfa.rfa"):
            self.is_duplicate_ext = True
        
        # Detectar sufixo de versão (.0001 até .0020)
        match = re.search(r'\.(\d{4})\.rfa$', self.name)
        if match:
            self.has_version_suffix = True
            self.version_suffix = match.group(1)

class RevitFileScanner:
    """Scanner para localizar e catalogar arquivos Revit."""
    
    def __init__(self, workspace_path: str):
        """
        Inicializa o scanner.
        
        Args:
            workspace_path: Caminho da pasta Organizador_Arquivos
        """
        self.workspace_path = Path(workspace_path)
        self.files: List[FileMetadata] = []
        
    def scan(self) -> List[FileMetadata]:
        """
        Varre recursivamente a pasta workspace buscando arquivos .rfa e .rfa.rfa
        
        Returns:
            Lista de FileMetadata com todos os arquivos encontrados
        """
        self.files = []
        
        if not self.workspace_path.exists():
            raise FileNotFoundError(f"Workspace não encontrado: {self.workspace_path}")
        
        # Varrer recursivamente
        for root, dirs, files in os.walk(self.workspace_path):
            for file in files:
                if file.endswith(".rfa") or file.endswith(".rfa.rfa"):
                    full_path = Path(root) / file
                    parent = Path(root).name
                    
                    metadata = FileMetadata(
                        path=full_path,
                        name=file,
                        extension=".rfa",
                        size=full_path.stat().st_size,
                        parent_folder=parent
                    )
                    
                    self.files.append(metadata)
        
        return self.files
    
    def get_duplicates(self) -> Dict[str, List[FileMetadata]]:
        """
        Identifica arquivos duplicados por nome (ignorando .rfa.rfa).
        
        Returns:
            Dict com nome base → lista de FileMetadata
        """
        duplicates_dict = {}
        
        for file_meta in self.files:
            # Nome base (sem versão .0001 e sem .rfa.rfa)
            base_name = file_meta.name
            if base_name.endswith(".rfa.rfa"):
                base_name = base_name[:-4]  # Remove último .rfa
            
            # Remove sufixo de versão se existir
            base_name_clean = re.sub(r'\.\d{4}\.rfa$', '.rfa', base_name)
            
            if base_name_clean not in duplicates_dict:
                duplicates_dict[base_name_clean] = []
            duplicates_dict[base_name_clean].append(file_meta)
        
        # Retornar apenas os que têm múltiplas versões
        return {k: v for k, v in duplicates_dict.items() if len(v) > 1}
    
    def get_stats(self) -> dict:
        """
        Retorna estatísticas do scan.
        
        Returns:
            Dict com contagem de arquivos, tamanho total, duplicatas, etc
        """
        duplicates = self.get_duplicates()
        duplicate_count = sum(len(files) - 1 for files in duplicates.values())
        version_files = sum(1 for f in self.files if f.has_version_suffix)
        
        return {
            "total_files": len(self.files),
            "total_size_mb": sum(f.size for f in self.files) / (1024 * 1024),
            "duplicate_ext_count": sum(1 for f in self.files if f.is_duplicate_ext),
            "version_suffix_count": version_files,
            "estimated_duplicates": duplicate_count,
            "duplicated_base_names": len(duplicates),
        }
    
    def get_files_by_folder(self) -> Dict[str, List[FileMetadata]]:
        """
        Agrupa arquivos por pasta pai.
        
        Returns:
            Dict com nome da pasta → lista de FileMetadata
        """
        result = {}
        for file_meta in self.files:
            if file_meta.parent_folder not in result:
                result[file_meta.parent_folder] = []
            result[file_meta.parent_folder].append(file_meta)
        return result
