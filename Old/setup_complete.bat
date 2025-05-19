@echo off
REM filepath: c:\Users\coren\Documents\Projets\Projet-Apprentissage\setup_complete.bat
SETLOCAL

SET ENV_NAME=minerl
echo ==== Installation de l'environnement pour JumpAI ====

REM Vérification si conda est disponible
where conda >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Conda non trouvé. Veuillez installer Miniconda ou Anaconda.
    exit /b 1
)

REM Vérification si l'environnement existe déjà
conda env list | findstr /C:"%ENV_NAME%" >nul
IF %ERRORLEVEL% EQU 0 (
    echo L'environnement %ENV_NAME% existe déjà.
    choice /C YN /M "Souhaitez-vous le recréer? (Y/N)"
    IF !ERRORLEVEL! EQU 1 (
        echo Suppression de l'environnement existant...
        call conda env remove -n %ENV_NAME% -y
    ) ELSE (
        echo Utilisation de l'environnement existant.
        goto :activation
    )
)

echo Création de l'environnement conda...
call conda create -n %ENV_NAME% python=3.8 -y

:activation
echo Activation de l'environnement conda...
call conda activate %ENV_NAME%

echo Installation des dépendances...
pip install -r Requirements.txt

echo Installation de MineRL...
pip install git+https://github.com/minerllabs/minerl --user

echo Configuration terminée.
echo Pour démarrer le projet:
echo 1. Activez l'environnement: conda activate %ENV_NAME%
echo 2. Pour tester: python main.py --course 1 --mode test
echo 3. Pour entraîner: python train_agent.py --course 1 --algo PPO
echo 4. Pour évaluer un modèle: python eval_agent.py --model-path models/final_1_PPO_XXXXX

ENDLOCAL
pause
