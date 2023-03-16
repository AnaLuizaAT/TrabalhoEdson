-- Criando a tabela Times
CREATE TABLE Times (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  fundacao DATE,
  cidade VARCHAR(50),
  estado CHAR(2)
);

-- Importando dados para a tabela Times
COPY Times (nome, fundacao, cidade, estado)
FROM '/times.csv'
DELIMITER ','
CSV HEADER;

-- Criando a tabela Jogadores
CREATE TABLE Jogadores (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  data_nascimento DATE,
  altura NUMERIC(4,2),
  posicao VARCHAR(20),
  id_time INTEGER REFERENCES Times(id)
);

-- Importando dados para a tabela Jogadores
COPY Jogadores (nome, data_nascimento, altura, posicao, id_time)
FROM '/jogadores.csv'
DELIMITER ','
CSV HEADER;

-- Criando a tabela Estadios
CREATE TABLE Estadios (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  cidade VARCHAR(50),
  estado CHAR(2),
  capacidade INTEGER
);

-- Importando dados para a tabela Estadios
COPY Estadios (nome, cidade, estado, capacidade)
FROM '/estadios.csv'
DELIMITER ','
CSV HEADER;

-- Criando a tabela Campeonatos
CREATE TABLE Campeonatos (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  edicao INTEGER,
  data_inicio DATE,
  data_fim DATE
);

-- Importando dados para a tabela Campeonatos
COPY Campeonatos (nome, edicao, data_inicio, data_fim)
FROM '/campeonatos.csv'
DELIMITER ','
CSV HEADER;

-- Criando a tabela Partidas
CREATE TABLE Partidas (
  id SERIAL PRIMARY KEY,
  data_hora TIMESTAMP NOT NULL,
  id_time_casa INTEGER REFERENCES Times(id),
  id_time_visitante INTEGER REFERENCES Times(id),
  id_estadio INTEGER REFERENCES Estadios(id),
  id_campeonato INTEGER REFERENCES Campeonatos(id),
  placar_casa INTEGER,
  placar_visitante INTEGER
);

-- Importando dados para a tabela Partidas
COPY Partidas (data_hora, id_time_casa, id_time_visitante, id_estadio, id_campeonato, placar_casa, placar_visitante)
FROM '/partidas.csv'
DELIMITER ','
CSV HEADER;