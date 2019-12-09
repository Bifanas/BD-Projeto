import datetime

# É pedido o nome do album e é exibido todos os albuns que tem o mesmo nome
# Em seguida é pedido o id do album e o novo preco
# O preco é atualizado e inserido no historico do album

def func(conn, cur,id):
    print('\nCorrigir preço')
    a = '1'
    b = 1

    #Enquanto o adm nao inserir 0 para voltar ao menu ficará removendo album
    while a != '0':
        b=1

        #Enquanto o adm nao inserir o nome correto ficara pedindo o nome do album
        while b != 0:
            q = 0
            nome = input("Insira o nome do álbum: ")

            #Procura na base de dados pelo nome do album
            cur.execute("SELECT count(*) FROM album WHERE nome = %s;", (nome,))
            q = cur.fetchone()[0]

            #Caso nao exista album com este nome
            if (q == 0):
                print("Não existe álbum com este nome.")
                b=1
                z = '0'
                z = input("Prima 0 para sair ou 1 para tentar novamente: ")
                if z == '0':
                    print("\n")
                    return

            #Caso exista album com o nome selecionado
            else:
                #Exista mais que um
                if(q != 1):

                    #Imprimo na tela todos os album com o nome dado e pede ao utilizador o id do album
                    cur.execute("SELECT id, nome, preco FROM album WHERE nome = %s ORDER BY id;", (nome,))
                    for linha in cur.fetchall():
                        print("ID:", linha[0], " | Nome:", linha[1], " | Preço: ", linha[2])

                    # Verifica se digitou o id certo
                    i = eval(input("Insira o albumID: "))
                    cur.execute("SELECT count(*) FROM album WHERE id = %s and nome = %s;", (i, nome))
                    f = cur.fetchone()[0]
                    while(f == 0):
                        i = eval(input("Insira o albumID: "))
                        cur.execute("SELECT count(*) FROM album WHERE id = %s and nome = %s;", (i, nome))
                        f = cur.fetchone()[0]
                    b=0

                #Existe só um
                else:
                    cur.execute("SELECT id FROM album WHERE nome = %s;", (nome,))
                    i = cur.fetchone()[0]
                    b=0

        #acrescentar preco antigo no historico_a
        cur.execute("SELECT preco FROM album WHERE id = %s;", (i,))
        p = cur.fetchone()[0]
        now = datetime.datetime.now()
        data = (str(now.day) + '-' + str(now.month) + '-' + str(now.year) + ' ' + str(now.hour) + ':' + str(now.minute))
        cur.execute("INSERT INTO historico_a values (%s,%s,%s,%s)", (p, data, id, i))

        #Faz a alteracao do preco do album
        preco = eval(input("Insira o novo preço: "))
        cur.execute("UPDATE album SET preco = %s WHERE id = %s;", (preco, i))
        conn.commit()

        #Caso utilizador nao queira fazer mais alteracoes
        a = input("Insira 0 para voltar: ")
    print("\n")