def imprime(linha):
    print(' - '.join(map(str, linha)))

# ADICIONA UM GENERO
def adicionar_genero(conn,cur):
    a = '1'
    while a != '0':
        print("\nJá existe um genero do novo album registado?")
        r = eval(input("1 - SIM\n2 - NAO\n"))

        # CASO O GENERO DO NOVO ALBUM JA FOI REGISTADO EM UM ALBUM ANTERIOR
        if (r == 1):
            n=0
            b = 1
            while b:
                nome = input("Digite o nome do genero: ")

                # VAI PROCURAR O NOME DO GENERO NA BASE DE DADOS
                cur.execute("SELECT count(*) FROM genero WHERE tipo_genero = %s", (nome,))
                q = cur.fetchone()[0]

                # CASO NAO ENCONTRAR O GENERO NA BASE DE DADOS
                if (q == 0):
                    print("Não existe genero com este nome.")
                    b = 1
                # VAI IMPRIMIR NA TELA O ID DO GENERO QUE TENHA ENCONTRADO
                else:
                    b = 0
                    cur.execute("SELECT id, tipo_genero FROM genero WHERE tipo_genero = %s;",(nome, ))
                    for linha in cur.fetchall():
                        imprime(linha)

                    n = input("Digite o ID do genero: ")

            # VAI PROCURAR ULTIMO ALBUM REGISTADO E ADICIONAR OS IDS NA TABELA ALBUM_GENERO
            cur.execute("SELECT MAX(id) FROM album")
            id_a = cur.fetchone()[0]

            cur.execute("INSERT INTO album_genero values (%s,%s)", (id_a, n))
            conn.commit()

        # CASO SEJA UMA NOVO GENERO NA BASE DE DADOS
        elif (r == 2):
            tipo_genero = input("Nome do Genero: ")

            # PROCURA ULTIMO ID DE GENERO REGISTADO E ADICIONA O GENERO NO PROXIMO
            cur.execute("SELECT MAX(id) FROM genero")
            id_g = cur.fetchone()[0]
            id_g += 1
            cur.execute("INSERT INTO genero values (%s,%s)", (id_g,tipo_genero))
            conn.commit()

            # PROCURA ULTIMO ID DE ALBUM REGISTADO E SALVA O ID DO ALBUM E DO GENERO NA TABELA ALBUM_GENERO
            cur.execute("SELECT MAX(id) FROM album")
            id_a = cur.fetchone()[0]
            cur.execute("INSERT INTO album_genero values (%s,%s)", (id_a, id_g))
            conn.commit()

        # CASO O UTILIZADOR TENHA DIGITADO ALGO DIFERENTE DE 1 E 2
        else:
            print("Opcao nao valida")

        # CASO O UTILIZADOR NAO QUEIRA INSERIR MAIS GENEROS NESTE ALBUM
        a = input("Insere 0 para voltar: ")