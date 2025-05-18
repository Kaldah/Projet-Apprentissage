@echo off
REM filepath: c:\Users\coren\Documents\Projets\Projet-Apprentissage\manage_maps.bat
SETLOCAL

SET ENV_NAME=minerl

REM Vérification si conda est disponible
where conda >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Conda non trouve. Execution sans environnement conda.
    goto :execute
)

REM Activation de l'environnement conda
call conda activate %ENV_NAME%

:execute
REM Exécution du script de gestion des cartes
python utils/manage_maps.py %*

REM Désactivation de l'environnement conda si activé
if defined CONDA_PREFIX (
    call conda deactivate
)

ENDLOCAL
