import csv
import random

# Gera 500 partidas com dados aleatórios
partidas = []
for _ in range(500):
    partida = {
        'data_hora': f'2022-{random.randint(1, 12):02d}-{random.randint(1, 28):02d} {random.randint(0, 23):02d}:{random.randint(0, 59):02d}',
        'id_time_casa': str(random.randint(1, 20)),
        'id_time_visitante': str(random.randint(1, 20)),
        'id_estadio': str(random.randint(1, 209)),
        'id_campeonato': str(random.randint(1, 4)),
        'placar_casa': str(random.randint(0, 20)),
        'placar_visitante': str(random.randint(0, 20))
    }
    partidas.append(partida)

# Escreve os dados das partidas em um arquivo CSV
with open('partidas.csv', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)

    # Cabeçalho
    writer.writerow(['data_hora', 'id_time_casa', 'id_time_visitante', 'id_estadio', 'id_campeonato', 'placar_casa', 'placar_visitante'])

    # Escreve os dados de cada partida na linha do arquivo CSV
    for partida in partidas:
        writer.writerow([partida['data_hora'], partida['id_time_casa'], partida['id_time_visitante'], partida['id_estadio'], partida['id_campeonato'], partida['placar_casa'], partida['placar_visitante']])