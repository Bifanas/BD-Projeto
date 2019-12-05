import datetime
# A funcao imprime serve para dar um espaco entre cada informacao sobre o album

# É pedido o nome do album e é exibido todos os albuns que tem o mesmo nome
# Em seguida é pedido o id do album e o novo preco
# O preco é atualizado e inserido no historico do album

def imprime(linha):
    print('       '.join(map(str, linha)))

def func(conn, cur,adm):
    a = '1'
    b = 1

    #Enquanto o adm nao inserir 0 para voltar ao menu ficará removendo album
    while a != '0':
        b=1

        #Enquanto o adm nao inserir o nome correto ficara pedindo o nome do album
        while b != 0:
            q = 0
            nome = input("Insira o nome do album: ")

            #Procura na base de dados pelo nome do album
            cur.execute("SELECT count(*) FROM album WHERE nome = %s;", (nome,))
            q = cur.fetchone()

            #Caso nao exista album com este nome
            if (q == 0):
                print("Não existe album com este nome.")
                b=1

            #Caso exista album com o nome selecionado
            else:

                #Imprimo na tela todos os album com o nome dado e pede ao utilizador o id do album
                print("ID       NOME       PRECO")
                cur.execute("SELECT id, nome, preco FROM album WHERE nome = %s ORDER BY id;", (nome,))
                for linha in cur.fetchall():
                    imprime(linha)

                id = eval(input("Insira o albumID: "))
                b=0

        #Regista novo preco e a data da alteracao e insere em historico_a
        preco = eval(input("Insira o novo preco: "))
        now = datetime.datetime.now()
        data = (str(now.day) + '-' + str(now.month) + '-' + str(now.year) + ' ' + str(now.hour) + ':' + str(now.minute))
        cur.execute("INSERT INTO historico_a values (%s,%s,%s,%s)", (preco, data, adm, id))

        #Faz a alteracao do preco do album
        cur.execute("UPDATE album SET preco = %s WHERE id = %s;", (preco, id))
        conn.commit()

        #Caso utilizador nao queira fazer mais alteracoes
        a = input("Insere 0 para voltar: ")
