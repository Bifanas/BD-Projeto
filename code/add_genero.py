def adicionar_genero(conn, cur):
    r = '0'
    while r != '3':
        print('\n')
        print('ADICIONAR GENERO')

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

        print("\nJá existe o gênero do album de ID", ida, "registado?")
        print("1 - SIM\n2 - NAO\n3 - VOLTAR")
        r = input('')

        # CASO O GENERO DO NOVO ALBUM JA FOI REGISTADO EM UM ALBUM ANTERIOR
        if (r == '1'):
            idg = 0
            b = 1
            n = 0
            while b:

                # VAI PROCURAR O NOME DO gênero NA BASE DE DADOS
                nome = input("Digite o nome do gênero: ")
                cur.execute("SELECT count(*) FROM genero WHERE tipo_genero = %s", (nome,))
                q = cur.fetchone()[0]

                # CASO NAO ENCONTRAR O gênero NA BASE DE DADOS
                if (q == 0):
                    print("Não existe gênero com este nome.")
                    b = 1
                    z = '0'
                    z = input("Prima 0 para sair ou 1 para tentar novamente: ")
                    if z == '0':
                        return

                # VAI IMPRIMIR NA TELA O ID DO gênero QUE TENHA ENCONTRADO
                else:
                    idg = 0
                    if (q != 1):
                        cur.execute("SELECT id, tipo_genero FROM genero WHERE genero = %s;", (nome,))
                        for linha in cur.fetchall():
                            print("ID:", linha[0], " | Estilo:", linha[1])

                        # Verifica se digitou o id certo
                        idg = input("Digite o ID do gênero: ")
                        cur.execute("SELECT count(*) FROM genero WHERE id = %s;", (idg,))
                        h = cur.fetchone()[0]
                        while (h == 0):
                            z = '0'
                            z = input("Prima 0 para sair ou 1 para tentar novamente: ")
                            if z == '0':
                                return
                            idg = input("Digite o ID do gênero: ")
                            cur.execute("SELECT count(*) FROM genero WHERE id = %s;", (idg,))
                            h = cur.fetchone()[0]
                        b = 0

                    # Existe só um
                    else:
                        cur.execute("SELECT id FROM genero WHERE tipo_genero = %s;", (nome,))
                        idg = cur.fetchone()[0]
                        b = 0

            cur.execute("INSERT INTO album_genero values (%s,%s)", (ida, idg ))
            conn.commit()
            r = input("Prima 3 para sair:")

        # CASO SEJA UM NOVO gênero NA BASE DE DADOS
        elif (r == '2'):

            Nome = input("Nome do gênero: ")

            # PROCURA ULTIMO ID DO gênero REGISTADO E ADICIONA A MUSICA NO PROXIMO
            cur.execute("SELECT MAX(id) FROM genero")
            idg = cur.fetchone()[0]

            # VERIFICA SE NAO TEM NENHUM gênero REGISTADO
            if (idg is None):
                idg = 0
            idg += 1
            cur.execute("INSERT INTO genero values (%s,%s)", (idg, Nome,))
            conn.commit()

            cur.execute("INSERT INTO album_genero values (%s,%s)", (ida, idg))
            conn.commit()
            r = input("Prima 3 para sair:")

        # CASO O UTILIZADOR TENHA DIGITADO ALGO DIFERENTE DE 1 E 2
        elif (r == '3'):
            print('\n')
            print("VOLTAR")


        else:
            print('\n')
            print("Opção não válida")