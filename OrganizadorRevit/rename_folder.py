import os
from pathlib import Path

old_path = Path(r"c:\Users\danie\OneDrive\Área de Trabalho\Projetos-Visual-Code\OrganizadorRevit\workspace_data")
new_path = Path(r"c:\Users\danie\OneDrive\Área de Trabalho\Projetos-Visual-Code\OrganizadorRevit\ultima_versao")

print(f"Verificando se existe: {old_path}")
print(f"Existe: {old_path.exists()}")

if old_path.exists():
    print(f"Renomeando para: {new_path}")
    old_path.rename(new_path)
    print(f"✓ Pasta renomeada com sucesso!")
else:
    print(f"✗ Pasta não encontrada")
    
input("Pressione Enter para sair...")
