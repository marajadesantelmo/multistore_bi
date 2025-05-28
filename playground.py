import pandas as pd
arribos_impo_historico = pd.read_csv('data/arribos_impo_historico.csv')
arribos_impo_historico.drop(columns=['e-tally'], inplace=True, errors='ignore')
arribos_impo_historico.to_csv('data/arribos_impo_historico.csv', index=False)