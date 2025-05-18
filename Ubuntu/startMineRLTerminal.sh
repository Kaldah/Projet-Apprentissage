#!/bin/bash

# Load conda
source "$(conda info --base)/etc/profile.d/conda.sh"

# Activate minerl env
conda activate minerl

# Confirm Java setup
echo "JAVA_HOME is set to: $JAVA_HOME"
java -version

# Optional: Run a quick MineRL test
echo "Testing MineRL with Treechop environment..."
python -c "
import minerl
env = minerl.make('Treechop-v0')
obs = env.reset()
print('MineRL environment loaded successfully.')
env.close()
"
