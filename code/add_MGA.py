import psycopg2
import funcaoData
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
cur = conn.cursor()

 # ADICIONA UMA MUSICA E RETORNA SEU ID
def adicionar_musica():
    musicaID = eval(input("MusicaID: "))
    cur.execute("SELECT count(musicaid) FROM album WHERE username = %s;", (musicaID,))
    cont = cur.fetchone()[0]

    while (cont != 0):
        musicaID = eval(input('Insira outro musicaID: '))
        cur.execute("SELECT count(musicaid) FROM album WHERE username = %s;", (musicaID,))
        cont = cur.fetchone()[0]

    a = 1
    while a:
        Nome = input("Nome da Musica: ")
        if (len(Nome) != None):
            a = 0

    a = 1
    while a:
        Tempo = input("Duracao da musica: ")
        if (len(Tempo) != None):
            a = 0

    cur.execute("INSERT INTO musica values (%s,%s,%s)", (musicaID, Nome, Tempo))
    conn.commit()

    return (musicaID)


# ADICIONA UM ARTISTA E RETORNA SEU ID
def adicionar_artista():
    artistaID = eval(input("ArtistaID: "))
    cur.execute("SELECT count(musicaid) FROM album WHERE artistaid = %s;", (artistaID,))
    cont = cur.fetchone()[0]

    while (cont != 0):
        artistaID = eval(input('Insira outro artistaID: '))
        cur.execute("SELECT count(artistaid) FROM album WHERE artistaid = %s;", (artistaID,))
        cont = cur.fetchone()[0]

    a = 1
    while a:
        Nome = input("Nome do Artista: ")
        if (len(Nome) != None):
            a = 0

    cur.execute("INSERT INTO artista values (%s,%s)", (artistaID, Nome))
    conn.commit()
    return (artistaID)

# ADICIONA UM GENERO E RETORNA SEU ID
def adicionar_genero():
    generoID = eval(input("GeneroID: "))
    cur.execute("SELECT count(generoid) FROM album WHERE generoid = %s;", (generoID,))
    cont = cur.fetchone()[0]

    while (cont != 0):
        generoID = eval(input('Insira outro generoID: '))
        cur.execute("SELECT count(generoid) FROM album WHERE generoid = %s;", (generoID,))
        cont = cur.fetchone()[0]

    a = 1
    while a:
        tipo_genero = input("Nome do Genero: ")
        if (len(tipo_genero) != None):
            a = 0


    cur.execute("INSERT INTO genero values (%s,%s)", (generoID, tipo_genero))
    conn.commit()

    return (generoID)
