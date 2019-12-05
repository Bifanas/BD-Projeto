def imprime(linha):
    print(' - '.join(map(str, linha)))

# ADICIONA MUSICAS
def adicionar_musica(conn,cur):
    a = '1'
    while a != '0':

        print ("Já existe uma musica do novo album registado?")
        r = eval(input("1 - SIM\n2 - NAO\n"))

        # CASO A MUSICA DO NOVO ALBUM JA FOI REGISTADO EM UM ALBUM ANTERIOR
        if(r == 1):
            b=1
            n=0
            while b:

                # VAI PROCURAR O NOME DA MUSICA NA BASE DE DADOS
                nome = input("Digite o nome da musica: ")
                cur.execute("SELECT count(*) FROM musica WHERE musica = %s", (nome, ))
                q = cur.fetchone()[0]

                # CASO NAO ENCONTRAR A MUSICA NA BASE DE DADOS
                if(q == 0):
                    print("Não existe musica com este nome.")
                    b = 1

                # VAI IMPRIMIR NA TELA O ID DA MUSICA QUE TENHA ENCONTRADO
                else:
                    b=0
                    cur.execute("SELECT id, musica FROM musica WHERE musica = %s;",(nome,))
                    for linha in cur.fetchall():
                        imprime(linha)

                    n = input("Digite o ID da musica: ")

            # VAI PROCURAR ULTIMO ALBUM REGISTADO E ADICIONAR OS IDS NA TABELA MUSICA_ALBUM
            cur.execute("SELECT MAX(id) FROM album")
            id_a = cur.fetchone()[0]

            cur.execute("INSERT INTO musica_album values (%s,%s)", (n, id_a))
            conn.commit()

        # CASO SEJA UMA NOVA MUSICA NA BASE DE DADOS
        elif(r == 2):

            Nome = input("Nome da Musica: ")

            # PROCURA ULTIMO ID DE MUSICA REGISTADO E ADICIONA A MUSICA NO PROXIMO
            cur.execute("SELECT MAX(id) FROM musica")
            id_m = cur.fetchone()[0]
            id_m += 1
            cur.execute("INSERT INTO musica values (%s,%s)", (id_m, Nome, ))
            conn.commit()

            # PROCURA ULTIMO ID DE ALBUM REGISTADO E SALVA O ID DO ALBUM E DA MUSICA NA TABELA MUSICA_ALBUM
            cur.execute("SELECT MAX(id) FROM album")
            id_a = cur.fetchone()[0]
            cur.execute("INSERT INTO musica_album values (%s,%s)", (id_m,id_a))
            conn.commit()

        # CASO O UTILIZADOR TENHA DIGITADO ALGO DIFERENTE DE 1 E 2
        else:
            print("Opcao nao valida")

        # CASO O UTILIZADOR NAO QUEIRA INSERIR MAIS MUSICAS NESTE ALBUM
        a = input("Insere 0 para voltar: ")