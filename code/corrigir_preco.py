import datetime
# A funcao imprime serve para dar um espaco entre cada informacao sobre o album

# É pedido o nome do album e é exibido todos os albuns que tem o mesmo nome
# Em seguida é pedido o id do album e o novo preco
# O preco é atualizado e inserido no historico do album

def imprime(linha):
    print('       '.join(map(str, linha)))

def func(conn, cur):
    a = 1
    while a != 0:
        q=0
        nome = input("Insira o nome do album: ")
        cur.execute("SELECT count(*) FROM album WHERE nome = %s GROUP BY nome;", (nome,))
        q = cur.fetchone()[0]
        if (q == 0):
            print("Não existe album com este nome.")

        elif(q > 1):
            print("ID       NOME       PRECO")
            cur.execute("SELECT id, nome, preco FROM album WHERE nome = %s ORDER BY id;", (nome,))
            for linha in cur.fetchall():
                imprime(linha)
            id = eval(input("Insira o albumID: "))


        preco = eval(input("Insira o novo preco: "))
        cur.execute("SELECT preco FROM album WHERE id = %s;", (id,))
        p_ant = cur.fetchone()[0]

        now = datetime.datetime.now()
        data = (str(now.day) + '-' + str(now.month) + '-' + str(now.year) + ' ' + str(now.hour) + ':' + str(now.minute))

        cur.execute("INSERT INTO historico_a values (%s,%s,1,%s)", (p_ant, data, id))


        cur.execute("UPDATE album SET preco = %s WHERE id = %s;", (preco, id))
        conn.commit()
        a = eval(input("Insere 0 para voltar: "))
