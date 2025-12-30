@echo off
chcp 65001 > nul
setlocal enabledelayedexpansion

cd /d "c:\Users\danie\OneDrive\Área de Trabalho\Projetos-Visual-Code\OrganizadorRevit"

echo Limpando versão anterior...
if exist "ultima_versao" rmdir /s /q "ultima_versao" 2>nul
del *.csv 2>nul

echo.
echo Executando programa...
python main.py --workspace "c:\Users\danie\OneDrive\Área de Trabalho\Projetos-Visual-Code\Organizador_Arquivos" --batch --force

echo.
echo Programa finalizado!
pause
