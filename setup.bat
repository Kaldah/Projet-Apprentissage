@echo off
SET ENV_NAME=minerl

echo 🔧 Updating Conda...
call conda update -n base -c defaults conda -y

echo 🔧 Creating Conda environment: %ENV_NAME% with Python 3.8...
call conda create -n %ENV_NAME% python=3.8 -y

echo ✅ Environment created. Now activating...
call activate %ENV_NAME%

echo 📦 Installing MineRL

pip install git+https://github.com/minerllabs/minerl

echo ✅ Installation complete!
echo 👉 To start working, run: conda activate %ENV_NAME%
pause
