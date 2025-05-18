#!/bin/bash

# ---- 1. Install OpenJDK 8 system-wide (no default update) ----
sudo add-apt-repository -y ppa:openjdk-r/ppa
sudo apt-get update
sudo apt-get install -y openjdk-8-jdk

# ---- 2. Create Conda Environment with Python 3.8 ----
conda create -y -n minerl python=3.8
source "$(conda info --base)/etc/profile.d/conda.sh"

# ---- 3. Activate the environment ----
conda activate minerl

# ---- 4. Set Java 8 only for this env ----
JAVA_PATH="/usr/lib/jvm/java-8-openjdk-amd64"
mkdir -p "$CONDA_PREFIX/etc/conda/activate.d"
mkdir -p "$CONDA_PREFIX/etc/conda/deactivate.d"

# On activate
echo "export JAVA_HOME=$JAVA_PATH" > "$CONDA_PREFIX/etc/conda/activate.d/env_vars.sh"
echo "export PATH=\$JAVA_HOME/bin:\$PATH" >> "$CONDA_PREFIX/etc/conda/activate.d/env_vars.sh"

# On deactivate
echo "unset JAVA_HOME" > "$CONDA_PREFIX/etc/conda/deactivate.d/env_vars.sh"
echo "export PATH=\$(echo \$PATH | sed -e 's#\$JAVA_HOME/bin:##')" >> "$CONDA_PREFIX/etc/conda/deactivate.d/env_vars.sh"

# ---- 5. Install MineRL and dependencies ----
pip install --upgrade pip
pip install minerl==0.4.4 gym==0.17.2
pip install torch torchvision

# ---- 6. Done ----
echo "MineRL environment ready. Run 'conda activate minerl' to use it."
