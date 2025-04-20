#!/bin/bash

# Installation de JDK 8
echo "🔧 Installing OpenJDK 8"

sudo apt update
sudo apt install openjdk-8-jdk

# Nom de l'environnement
ENV_NAME="minerl"

# Création de l'environnement conda
echo "🔧 Creating conda environment: $ENV_NAME with Python 3.8... (java JDK 1.8 required)"
conda create -n $ENV_NAME python=3.8 -y

# Activation de l'environnement
echo "✅ Environment created. To activate it, run: conda activate $ENV_NAME"

# Installation de MineRL
echo "📦 Installing MineRL and dependencies..."
conda activate $ENV_NAME
pip install git+https://github.com/minerllabs/minerl

echo "✅ Installation complete!"
echo "👉 You can now run: conda activate $ENV_NAME"
