def adicionar_musica(conn,cur):
    r = '0'
    while r != '3':
        print('\n')
        print('ADICIONAR MÚSICA')

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

        print("\nJá existe uma musica do album de ID", ida, "registado?")
        print("1 - SIM\n2 - NAO\n3 - VOLTAR")
        r = input('')

        # CASO A MUSICA DO NOVO ALBUM JA FOI REGISTADO EM UM ALBUM ANTERIOR
        if (r == '1'):
            idm = 0
            b = 1
            n = 0
            while b:

                # VAI PROCURAR O NOME DA MUSICA NA BASE DE DADOS
                nome = input("Digite o nome da música: ")
                cur.execute("SELECT count(*) FROM musica WHERE musica = %s", (nome,))
                q = cur.fetchone()[0]

                # CASO NAO ENCONTRAR A MUSICA NA BASE DE DADOS
                if (q == 0):
                    print("Não existe música com este nome.")
                    b = 1
                    z = '0'
                    z = input("Prima 0 para sair ou 1 para tentar novamente: ")
                    if z == '0':
                        return

                # VAI IMPRIMIR NA TELA O ID DA MUSICA QUE TENHA ENCONTRADO
                else:
                    idm = 0
                    if (q != 1):
                        cur.execute("SELECT id, musica FROM musica WHERE musica = %s;", (nome,))
                        for linha in cur.fetchall():
                            print("ID:", linha[0], " | Nome:", linha[1])

                        # Verifica se digitou o id certo
                        idm = input("Digite o ID da musica: ")
                        cur.execute("SELECT count(*) FROM musica WHERE id = %s;", (idm,))
                        h = cur.fetchone()[0]
                        while (h == 0):
                            z = '0'
                            z = input("Prima 0 para sair ou 1 para tentar novamente: ")
                            if z == '0':
                                return
                            idm = input("Digite o ID da musica: ")
                            cur.execute("SELECT count(*) FROM musica WHERE id = %s;", (idm,))
                            h = cur.fetchone()[0]
                        b = 0

                    # Existe só um
                    else:
                        cur.execute("SELECT id FROM musica WHERE musica = %s;", (nome,))
                        idm = cur.fetchone()[0]
                        b = 0

            cur.execute("INSERT INTO musica_album values (%s,%s)", (idm, ida))
            conn.commit()
            r = input("Prima 3 para sair.")

        # CASO SEJA UMA NOVA MUSICA NA BASE DE DADOS
        elif (r == '2'):

            Nome = input("Nome da Música: ")

            # PROCURA ULTIMO ID DE MUSICA REGISTADO E ADICIONA A MUSICA NO PROXIMO
            cur.execute("SELECT MAX(id) FROM musica")
            id_m = cur.fetchone()[0]

            # VERIFICA SE NAO TEM NENHUMA MUSICA REGISTADO
            if (id_m is None):
                id_m = 0
            id_m += 1
            cur.execute("INSERT INTO musica values (%s,%s)", (id_m, Nome,))
            conn.commit()

            cur.execute("INSERT INTO musica_album values (%s,%s)", (id_m, ida))
            conn.commit()
            r = input("Prima 3 para sair.")

        # CASO O UTILIZADOR TENHA DIGITADO ALGO DIFERENTE DE 1 E 2
        elif (r == '3'):
            print('\n')
            print("VOLTAR")

        else:
            print('\n')
            print("Opção não válida")

