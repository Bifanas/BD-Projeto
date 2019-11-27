import psycopg2

# ADICIONA MUSICAS
def adicionar_musica(conn,cur):
    a = 1
    while a != 0:
        Nome = input("Nome da Musica: ")
        cur.execute("INSERT INTO musica (musica) values (%s)", (Nome, ))
        conn.commit()

        cur.execute("SELECT MAX(id) FROM album")
        id_a = cur.fetchone()[0]

        cur.execute("SELECT MAX(id) FROM musica")
        id_m = cur.fetchone()[0]

        cur.execute("INSERT INTO musica_album values (%s%s)", (id_m,id_a))
        conn.commit()

        a = eval(input("Insere 0 para voltar: "))


# ADICIONA UM GENERO
def adicionar_genero(conn,cur):
    a = 1
    while a != 0:
        tipo_genero = input("Nome do Genero: ")
        cur.execute("INSERT INTO genero (tipo_genero) values (%s)", (tipo_genero))
        conn.commit()

        cur.execute("SELECT MAX(id) FROM album")
        id_a = cur.fetchone()[0]

        cur.execute("SELECT MAX(id) FROM genero")
        id_g = cur.fetchone()[0]

        cur.execute("INSERT INTO album_genero values (%s%s)", (id_a, id_g))
        conn.commit()

        a = eval(input("Insere 0 para voltar: "))


# ADICIONA ARTISTAs
def adicionar_artista(conn, cur):
    a = 1
    while a != 0:
        Nome = input("Nome do Artista: ")

        cur.execute("INSERT INTO artista (artista) values (%s)", (Nome,))
        conn.commit()

        cur.execute("SELECT MAX(id) FROM album")
        id_a = cur.fetchone()[0]

        cur.execute("SELECT MAX(id) FROM artista")
        id_art = cur.fetchone()[0]
        cur.execute("INSERT INTO artista_album values (%s%s)", (id_art, id_a))
        conn.commit()

        a = eval(input("Insere 0 para voltar: "))
