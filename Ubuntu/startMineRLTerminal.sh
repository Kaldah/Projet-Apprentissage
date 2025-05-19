#!/bin/bash

# Load conda
source "$(conda info --base)/etc/profile.d/conda.sh"

# Activate minerl env
conda activate minerl

# Confirm Java setup
echo "JAVA_HOME is set to: $JAVA_HOME"
java -version

# Launch a new bash shell with the env activated
exec bash --rcfile <(echo "source ~/.bashrc; conda activate minerl")

