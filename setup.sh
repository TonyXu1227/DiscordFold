#!/bin/bash
pip install -U discord
pip install -U python-dotenv

echo "Running install colabfold"
bash install_colabbatch_M1mac.sh


export PATH="/Users/bigricce1227/Documents/Coding_Projects/DiscordFold/localcolabfold/colabfold-conda/bin:$PATH"

echo "Running inputbot"
python inputbot.py