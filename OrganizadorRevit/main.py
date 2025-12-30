#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Organizador de Famílias Revit - ISO 19650

Programa standalone para organizar automaticamente famílias Revit (.rfa)
seguindo padrões ISO 19650 e ISO 9001.

Uso:
    python main.py --workspace ./Organizador_Arquivos --dry-run
    python main.py --workspace ./Organizador_Arquivos --interactive
    python main.py --workspace ./Organizador_Arquivos --batch --force

Autor: Sistema de Organização de Arquivos BIM
Data: 2025-01-30
Versão: 1.0.0
"""

import sys
import os
from pathlib import Path

# Forçar UTF-8 em Windows
if sys.platform == 'win32':
    os.environ['PYTHONIOENCODING'] = 'utf-8'

# Adicionar diretório raiz ao path para importações
sys.path.insert(0, str(Path(__file__).parent))

from cli import main

if __name__ == "__main__":
    main()
