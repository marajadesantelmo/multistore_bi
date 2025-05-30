import pandas as pd
import os
arribos_impo_historico = pd.read_csv('data/arribos_impo_historico.csv')
arribos_impo_historico.drop(columns=['e-tally'], inplace=True, errors='ignore')
arribos_impo_historico.to_csv('data/arribos_impo_historico.csv', index=False)

data_folder = 'data'
for filename in os.listdir(data_folder):
    if filename.endswith('.csv'):
        file_path = os.path.join(data_folder, filename)
        df = pd.read_csv(file_path)
        df.drop(columns=['e-tally'], inplace=True, errors='ignore')
        df.to_csv(file_path, index=False)

        replacements = {
            'lift': 'Cargo',
            'merco': 'Euro',
            'textil': 'Metal',
            'argentina': 'Brasil'
        }

        import re

import random
import string


pattern_replacements = {re.compile(k, re.IGNORECASE): v for k, v in replacements.items()}
for filename in os.listdir(data_folder):
    if filename.endswith('.csv'):
        file_path = os.path.join(data_folder, filename)
        df = pd.read_csv(file_path)
        if 'Cliente' in df.columns:
            extra_replacements = {
            'Jupam': 'Latos',
            'Cargo': 'Transport',
            'Nueva': 'Logic'
            }
            df['Cliente'] = df['Cliente'].replace(extra_replacements, regex=True)
            df.to_csv(file_path, index=False)