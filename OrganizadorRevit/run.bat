@echo off
REM Script de inicialização rápida para Windows
REM Instala dependências e executa o programa

echo ======================================================================
echo Organizador de Familias Revit - ISO 19650
echo ======================================================================
echo.

REM Verificar se Python está disponível
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Erro: Python nao encontrado no PATH
    echo Por favor, instale Python 3.8+ em: https://www.python.org
    pause
    exit /b 1
)

echo Instalando dependencias...
python -m pip install click tqdm --quiet

echo.
echo ======================================================================
echo MENU PRINCIPAL
echo ======================================================================
echo.
echo 1. Modo DRY-RUN (visualizar sem alterar)
echo 2. Modo INTERATIVO (confirmar antes de mover)
echo 3. Modo BATCH (processar automaticamente)
echo 4. Sair
echo.

set /p opcao="Escolha uma opcao (1-4): "

if "%opcao%"=="1" goto dryrun
if "%opcao%"=="2" goto interactive
if "%opcao%"=="3" goto batch
if "%opcao%"=="4" goto fim

echo Opcao invalida!
pause
goto menu

:dryrun
set /p workspace="Digite o caminho da pasta Organizador_Arquivos: "
python main.py --workspace "%workspace%" --dry-run
pause
goto fim

:interactive
set /p workspace="Digite o caminho da pasta Organizador_Arquivos: "
python main.py --workspace "%workspace%" --interactive
pause
goto fim

:batch
set /p workspace="Digite o caminho da pasta Organizador_Arquivos: "
echo ATENCAO: Isto vai processar TODOS os arquivos sem confirmacao!
set /p confirm="Confirmar? (s/n): "
if /i "%confirm%"=="s" (
    python main.py --workspace "%workspace%" --batch --force
) else (
    echo Cancelado.
)
pause
goto fim

:fim
exit /b 0
