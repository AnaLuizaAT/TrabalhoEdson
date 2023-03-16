import csv
import random
import datetime

# Lista de nomes de jogadores
nomes = ["André", "Bruno", "Carlos", "Diego", "Eduardo", "Felipe", "Gustavo", "Henrique", "Igor", "João", "Lucas", "Marcelo", "Nathan", "Otávio", "Paulo", "Rafael", "Samuel", "Thiago", "Victor", "Willian"]

# Lista de posições de jogadores
posicoes = ["goleiro", "zagueiro", "lateral-direito", "lateral-esquerdo", "volante", "meio-campista", "atacante"]

# Lista de Clubes de jogadores Brasileiros
clubes = ["Corinthians", "Palmeiras", "Santos", "São Paulo", "Flamengo", "Fluminense", "Vasco da Gama", "Botafogo", "Grêmio", "Internacional", "Cruzeiro", "Atlético Mineiro", "Bahia", "Vitória", "Sport", "Santa Cruz", "Ceará", "Fortaleza", "Coritiba", "Athetico Paranaense"]

# Criação do arquivo CSV
with open('jogadores.csv', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)

    # Cabeçalho
    writer.writerow(['nome', 'data_nascimento', 'altura', 'posicao', 'id_time'])

    # Geração de 10.000 registros aleatórios
    for _ in range(10000):
        nome = f"{random.choice(nomes)} {random.choice(nomes)}"
        ano = random.randint(1950, 2020)
        mes = random.randint(1, 12)
        dia = random.randint(1, 28)
        data_nascimento = datetime.date(ano, mes, dia)
        altura = round(random.uniform(1.50, 2.10), 2)
        posicao = random.choice(posicoes)
        id_time = random.randint(1, 20)

        # Escreve os dados na linha do arquivo CSV
        writer.writerow([nome, data_nascimento, altura, posicao, id_time])