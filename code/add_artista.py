def adicionar_artista(conn, cur):
    r = '0'
    while r != '3':
        print('\n')
        print('ADICIONAR ARTISTA')

        # Mostra todos os albuns registados
        print("Álbuns Existentes:")
        cur.execute("SELECT * FROM album ORDER BY ID;")
        for linha in cur.fetchall():
            print("ID:", linha[0], " | Nome:", linha[1])

        # Verifica se digitou o id certo
        ida = eval(input("Insira o albumID: "))
        cur.execute("SELECT count(*) FROM album WHERE id = %s;", (ida,))
        f = cur.fetchone()[0]
        while (f == 0):
            z = '0'
            z = input("Prima 0 para sair ou 1 para tentar novamente: ")
            if z == '0':
                return
            ida = eval(input("Insira o albumID: "))
            cur.execute("SELECT count(*) FROM album WHERE id = %s;", (ida,))
            f = cur.fetchone()[0]

        print("\nJá existe o artista do album de ID", ida, "registado?")
        print("1 - SIM\n2 - NAO\n3 - VOLTAR")
        r = input('')

        # CASO O ARTISTA DO NOVO ALBUM JA FOI REGISTADO EM UM ALBUM ANTERIOR
        if (r == '1'):
            idart = 0
            b = 1
            n = 0
            while b:

                # VAI PROCURAR O NOME DO ARTISTA NA BASE DE DADOS
                nome = input("Digite o nome do artista: ")
                cur.execute("SELECT count(*) FROM artista WHERE artista = %s", (nome,))
                q = cur.fetchone()[0]

                # CASO NAO ENCONTRAR O artista NA BASE DE DADOS
                if (q == 0):
                    print("Não existe artista com este nome.")
                    b = 1
                    z = '0'
                    z = input("Prima 0 para sair ou 1 para tentar novamente: ")
                    if z == '0':
                        return

                # VAI IMPRIMIR NA TELA O ID DO ARTISTA QUE TENHA ENCONTRADO
                else:
                    idart = 0
                    if (q != 1):
                        cur.execute("SELECT id, artista FROM artista WHERE artista = %s;", (nome,))
                        for linha in cur.fetchall():
                            print("ID:", linha[0], " | Nome:", linha[1])

                        # Verifica se digitou o id certo
                        idart = input("Digite o ID do artista: ")
                        cur.execute("SELECT count(*) FROM artista WHERE id = %s;", (idart,))
                        h = cur.fetchone()[0]
                        while (h == 0):
                            z = '0'
                            z = input("Prima 0 para sair ou 1 para tentar novamente: ")
                            if z == '0':
                                return
                            idart = input("Digite o ID do artista: ")
                            cur.execute("SELECT count(*) FROM artista WHERE id = %s;", (idart,))
                            h = cur.fetchone()[0]
                        b = 0

                    # Existe só um
                    else:
                        cur.execute("SELECT id FROM artista WHERE artista = %s;", (nome,))
                        idart = cur.fetchone()[0]
                        b = 0

            cur.execute("INSERT INTO artista_album values (%s,%s)", (idart, ida))
            conn.commit()
            r = input("Prima 3 para sair.")

        # CASO SEJA UMU NOVO ARTISTA NA BASE DE DADOS
        elif (r == '2'):

            Nome = input("Nome do Artista: ")

            # PROCURA ULTIMO ID DO ARTISTA REGISTADO E ADICIONA A MUSICA NO PROXIMO
            cur.execute("SELECT MAX(id) FROM artista")
            idart = cur.fetchone()[0]

            # VERIFICA SE NAO TEM NENHUM ARTISTA REGISTADO
            if (idart is None):
                idart = 0
            idart += 1
            cur.execute("INSERT INTO artista values (%s,%s)", (idart, Nome,))
            conn.commit()

            cur.execute("INSERT INTO artista_album values (%s,%s)", (idart, ida))
            conn.commit()
            r = input("Prima 3 para sair.")

        # CASO O UTILIZADOR TENHA DIGITADO ALGO DIFERENTE DE 1 E 2
        elif (r == '3'):
            print('\n')
            print("VOLTAR")


        else:
            print('\n')
            print("Opção não válida")