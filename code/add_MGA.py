import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
cur = conn.cursor()


# ADICIONA MUSICAS AO ALBUM
def adicionar_musica():
    a = 1
    while a != 0:
        Nome = input("Nome da Musica: ")
        Tempo = input("Duracao da musica: ")

        cur.execute("INSERT INTO musica values (%s,%s)", (Nome, Tempo))
        conn.commit()

        a = eval(input("Insere 0 para voltar: "))


# ADICIONA UM GENERO
def adicionar_genero():
    a = 1
    while a != 0:
        tipo_genero = input("Nome do Genero: ")
        cur.execute("INSERT INTO genero values (%s)", (tipo_genero))
        conn.commit()


# ADICIONA UM ARTISTA
def adicionar_artista():
    a = 1
    while a != 0:
        Nome = input("Nome do Artista: ")

        cur.execute("INSERT INTO artista values (%s)", (Nome,))
        conn.commit()

        a = eval(input("Insere 0 para voltar: "))