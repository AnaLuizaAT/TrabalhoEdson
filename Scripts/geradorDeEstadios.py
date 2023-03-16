import csv
import requests
from bs4 import BeautifulSoup

# Faz a requisição HTTP e obtém o HTML da página
url = "https://pt.wikipedia.org/wiki/Lista_dos_maiores_est%C3%A1dios_de_futebol_do_Brasil"
response = requests.get(url)
html = response.content

# Faz o parse do HTML com o BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Encontra a tabela que contém os dados dos estádios
table = soup.find_all('table')[0]

# Extrai os dados dos estádios da tabela
estadios = []
for row in table.find_all('tr')[1:]:
    columns = row.find_all('td')
    nome = columns[0].text.strip()
    cidade = columns[1].text.strip()

    estadio = {
        'nome': nome,
        'cidade': cidade,
    }

    estadios.append(estadio)

# Escreve os dados dos estádios em um arquivo CSV
with open('estadios.csv', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)

    # Cabeçalho
    writer.writerow(['nome', 'cidade'])

    # Escreve os dados de cada estádio na linha do arquivo CSV
    for estadio in estadios:
        writer.writerow([estadio['nome'], estadio['cidade']])