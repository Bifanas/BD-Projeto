def imprime(linha):
    print(' - '.join(map(str, linha)))

# ADICIONA ARTISTAs
def adicionar_artista(conn, cur):
    a = '1'
    while a != '0':

        print("\nJá existe um artista do novo album registado?")
        r = eval(input("1 - SIM\n2 - NAO\n"))

        # CASO O ARTISTA DO NOVO ALBUM JA FOI REGISTADO EM UM ALBUM ANTERIOR
        if (r == 1):
            n=0
            b = 1
            while b:

                # VAI PROCURAR O NOME DO ARTISTA NA BASE DE DADOS
                nome = input("Digite o nome do artista: ")
                cur.execute("SELECT count(*) FROM artista WHERE artista = %s", (nome,))
                q = cur.fetchone()[0]

                # CASO NAO ENCONTRAR O ARTISTA NA BASE DE DADOS
                if (q == 0):
                    print("Não existe artista com este nome.")
                    b = 1

                # VAI IMPRIMIR NA TELA O ID DO ARTISTA QUE TENHA ENCONTRADO
                else:
                    b = 0
                    cur.execute("SELECT id, artista FROM artista WHERE artista = %s;",(nome, ))
                    for linha in cur.fetchall():
                        imprime(linha)

                    n = input("Digite o ID do artista: ")

            # VAI PROCURAR ULTIMO ALBUM REGISTADO E ADICIONAR OS IDS NA TABELA ARTISTA_ALBUM
            cur.execute("SELECT MAX(id) FROM album")
            id_a = cur.fetchone()[0]

            cur.execute("INSERT INTO artista_album values (%s,%s)", (n, id_a))
            conn.commit()


        # CASO SEJA UM NOVO ARTISTA NA BASE DE DADOS
        elif (r == 2):
            Nome = input("Nome do Artista: ")

            # PROCURA ULTIMO ID DE ARTISTA REGISTADO E ADICIONA O ARTISTA NO PROXIMO
            cur.execute("SELECT MAX(id) FROM artista")
            id_art = cur.fetchone()[0]
            id_art += 1
            cur.execute("INSERT INTO artista values (%s,%s)", (id_art,Nome,))
            conn.commit()

            # PROCURA ULTIMO ID DE ALBUM REGISTADO E SALVA O ID DO ALBUM E DO ARTISTA NA TABELA ARTISTA_ALBUM
            cur.execute("SELECT MAX(id) FROM album")
            id_a = cur.fetchone()[0]

            cur.execute("INSERT INTO artista_album values (%s,%s)", (id_art, id_a))
            conn.commit()

        # CASO O UTILIZADOR TENHA DIGITADO ALGO DIFERENTE DE 1 E 2
        else:
            print("Opcao nao valida")


        # CASO O UTILIZADOR NAO QUEIRA INSERIR MAIS ARTISTAS NESTE ALBUM
        a = input("Insere 0 para voltar: ")