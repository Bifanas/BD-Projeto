# ADICIONA UM GENERO
def adicionar_genero(conn,cur):
    a = '1'
    while a != '0':
        print("\nJá existe um genero do novo album registado?")
        r = eval(input("1 - SIM\n2 - NAO\n"))
        if (r == 1):
            b = 1
            while b:
                nome = input("Digite o nome do genero: ")
                cur.execute("SELECT count(*) FROM tipo_genero WHERE genero = %s GROUP BY tipo_genero", (nome,))
                q = cur.fetchone()[0]
                if (q is None):
                    print("Não existe genero com este nome.")
                    b = 1

                else:
                    b = 0
                    cur.execute("SELECT id, tipo_genero FROM genero WHERE tipo_genero = %s;"(nome, ))
                    for linha in cur.fetchall():
                        imprime(linha)

                    n = input("Digite o ID do genero: ")

            cur.execute("SELECT MAX(id) FROM album")
            id_a = cur.fetchone()[0]

            cur.execute("INSERT INTO album_genero values (%s,%s)", (n, id_a))
            conn.commit()

        elif (r == 2):
            tipo_genero = input("Nome do Genero: ")
            cur.execute("INSERT INTO genero (tipo_genero) values (%s)", (tipo_genero))
            conn.commit()

            cur.execute("SELECT MAX(id) FROM album")
            id_a = cur.fetchone()[0]

            cur.execute("SELECT MAX(id) FROM genero")
            id_g = cur.fetchone()[0]

            cur.execute("INSERT INTO album_genero values (%s,%s)", (id_a, id_g))
            conn.commit()

        else:
            print("Opcao nao valida")

        a = input("Insere 0 para voltar: ")


# ADICIONA ARTISTAs
def adicionar_artista(conn, cur):
    a = '1'
    while a != '0':
        print("\nJá existe um artista do novo album registado?")
        r = eval(input("1 - SIM\n2 - NAO\n"))
        if (r == 1):
            b = 1
            while b:
                nome = input("Digite o nome do artista: ")
                cur.execute("SELECT count(*) FROM artista WHERE artista = %s GROUP BY artista", (nome,))
                q = cur.fetchone()[0]
                if (q is None):
                    print("Não existe artista com este nome.")
                    b = 1

                else:
                    b = 0
                    cur.execute("SELECT id, artista FROM artista WHERE artista = %s;"(nome, ))
                    for linha in cur.fetchall():
                        imprime(linha)

                    n = input("Digite o ID do artista: ")

            cur.execute("SELECT MAX(id) FROM album")
            id_a = cur.fetchone()[0]

            cur.execute("INSERT INTO artista_album values (%s,%s)", (n, id_a))
            conn.commit()

        elif (r == 2):
            Nome = input("Nome do Artista: ")

            cur.execute("INSERT INTO artista (artista) values (%s)", (Nome,))
            conn.commit()

            cur.execute("SELECT MAX(id) FROM album")
            id_a = cur.fetchone()[0]

            cur.execute("SELECT MAX(id) FROM artista")
            id_art = cur.fetchone()[0]
            cur.execute("INSERT INTO artista_album values (%s,%s)", (id_art, id_a))
            conn.commit()

        else:
            print("Opcao nao valida")

        a = input("Insere 0 para voltar: ")
