"""
Gerenciador de versões de pastas.
Controla a criação de pastas com sufixo _R00, _R01, _R02, etc.
"""

from pathlib import Path
import re
from typing import Tuple


class VersionManager:
    """Gerencia versionamento de pastas de saída."""
    
    @staticmethod
    def extract_version_suffix(folder_name: str) -> int | None:
        """
        Extrai o número de versão do nome da pasta.
        
        Args:
            folder_name: Nome da pasta (ex: "Organizador_Revit_Organizado_R05")
        
        Returns:
            Número da versão (ex: 5) ou None se não tiver sufixo
        """
        match = re.search(r'_R(\d+)$', folder_name)
        if match:
            return int(match.group(1))
        return None
    
    @staticmethod
    def get_next_version_folder(base_path: Path, base_name: str) -> Tuple[Path, int]:
        """
        Encontra a próxima versão disponível para a pasta e retorna o caminho.
        
        Args:
            base_path: Caminho pai das pastas (ex: c:/output/)
            base_name: Nome base da pasta (ex: "Organizador_Revit_Organizado")
        
        Returns:
            Tupla (caminho_completo, número_versão)
            Ex: (Path("c:/output/Organizador_Revit_Organizado_R03"), 3)
        """
        base_path = Path(base_path)
        base_path.mkdir(parents=True, exist_ok=True)
        
        # Encontrar todas as pastas que correspondem ao padrão
        existing_versions = []
        for item in base_path.iterdir():
            if item.is_dir():
                # Verificar se começa com o nome base e tem sufixo _R##
                if item.name.startswith(base_name):
                    version = VersionManager.extract_version_suffix(item.name)
                    if version is not None:
                        existing_versions.append(version)
        
        # Encontrar próximo número
        next_version = 0
        if existing_versions:
            next_version = max(existing_versions) + 1
        
        # Criar nome da pasta
        version_folder_name = f"{base_name}_R{next_version:02d}"
        version_folder_path = base_path / version_folder_name
        
        return version_folder_path, next_version
    
    @staticmethod
    def format_version_string(version_num: int) -> str:
        """
        Formata número de versão com dois dígitos (00, 01, ..., 99).
        
        Args:
            version_num: Número da versão (0, 1, 2, ...)
        
        Returns:
            String formatada (ex: "R00", "R01", "R05")
        """
        return f"R{version_num:02d}"
