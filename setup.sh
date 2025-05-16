#!/bin/bash
pip install -U discord
pip install -U python-dotenv

echo "Running install colabfold"
bash install_colabbatch_M1mac.sh
echo "Running inputbot"
python inputbot.py