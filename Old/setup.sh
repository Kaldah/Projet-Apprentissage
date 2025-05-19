#!/bin/bash

# Installation de JDK 8
echo "🔧 Installing OpenJDK 8"

sudo apt update
sudo apt install openjdk-8-jdk

# Nom de l'environnement
ENV_NAME="minerl"


# Installation de MineRL
echo "📦 Installing MineRL and dependencies..."
conda activate $ENV_NAME
pip install git+https://github.com/minerllabs/minerl --user

echo "✅ Installation complete!"
echo "👉 You can now run: conda activate $ENV_NAME" to use MineRL ! :)
