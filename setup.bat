@echo off
SET ENV_NAME=minerl

echo Activating conda env...
call activate %ENV_NAME%

echo 📦 Installing MineRL

pip install git+https://github.com/minerllabs/minerl --user

echo ✅ Installation complete!
echo 👉 To start working, run: conda activate %ENV_NAME% to use MineRL ! :)

conda deactivate
pause
