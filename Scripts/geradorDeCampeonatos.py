import csv

# Dados dos campeonatos
campeonatos = [
    {'nome': 'Campeonato Brasileiro', 'edicao': '2022', 'data_inicio': '30/04/2022', 'data_fim': '11/12/2022'},
    {'nome': 'Copa Libertadores da América', 'edicao': '2022', 'data_inicio': '16/02/2022', 'data_fim': '20/11/2022'},
    {'nome': 'Copa do Brasil', 'edicao': '2022', 'data_inicio': '08/02/2022', 'data_fim': '27/10/2022'},
    {'nome': 'Campeonato Paulista', 'edicao': '2022', 'data_inicio': '29/01/2022', 'data_fim': '22/05/2022'},
]

# Escreve os dados dos campeonatos em um arquivo CSV
with open('campeonatos.csv', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)

    # Cabeçalho
    writer.writerow(['nome', 'edicao', 'data_inicio', 'data_fim'])

    # Escreve os dados de cada campeonato na linha do arquivo CSV
    for campeonato in campeonatos:
        writer.writerow([campeonato['nome'], campeonato['edicao'], campeonato['data_inicio'], campeonato['data_fim']])