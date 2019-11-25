import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
cur = conn.cursor()

# É pedido o nome do album e é exibido todos os albuns que tem o mesmo nome
# Em seguida é pedido o id do album e o novo preco
# É registrado quantos discos ha em stock
# O preco é atualizado e inserido no historico do album

def func():
    a = 1
    while a != 0:
        nome = input("Insira o nome do album: ")
        cur.execute("SELECT nome, albumid, preco FROM album WHERE nome = %s;", (nome,))
        for linha in cur.fetchall():
            print(linha)

        id = eval(input("Insira o albumID: "))

        preco = eval(input("Insira o novo preco: "))

        cur.execute("SELECT stock FROM album WHERE albumid = %s;", (id,))
        stock = cur.fetchone()

        cur.execute("UPDATE album SET preco = %s WHERE albumid = %s;", (preco, id))
        cur.execute("INSERT INTO historico_a values (%s,%s,%s)", (preco, stock, id))
        conn.commit()
        a = eval(input("Insere 0 para voltar: "))
