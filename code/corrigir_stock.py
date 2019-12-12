def func(conn,cur):
    print("\n")
    print("CORRIGIR STOCK")
    cur.execute("SELECT count(id) FROM album WHERE stock <= 0;")
    a = cur.fetchone()[0]

    if(a == 0):
        print("Não há álbuns registados indisponíveis.")
        return

    else:
        cur.execute("SELECT id, nome, preco FROM album WHERE stock < 0 ORDER BY ID;")
        for linha in cur.fetchall():
            print("ID:", linha[0], " | Nome:", linha[1], " | Preço: ", linha[2])

    # Pede q o cliente insira o respectivo id
    i = input("Digite o ID do album: ")
    while (i[0] < '1' or i[0] > '9'):
        print("Não existe este ID.")
        i = input("Digite o id do álbum: ")

    i = eval(i)

    # Verifica se o album tem em stock
    cur.execute("SELECT count(stock) FROM album WHERE id = %s;", (i,))
    q = cur.fetchone()[0]

    while (q == 0):
        print("Não existe este ID.")
        i = input("Digite o id do álbum: ")

        while (i[0] < '1' or i[0] > '9'):
            i = input("Digite o id do álbum: ")

        i = eval(i)

        cur.execute("SELECT count(stock) FROM album WHERE id = %s;", (i,))
        q = cur.fetchone()[0]

    stock = input("Insira a nova quantidade disponível: ")
    while (stock[0] < '1' or stock[0] > '9'):
        print("Não existe este ID.")
        stock = input("Insira a nova quantidade disponível: ")

    stock = eval(stock)

    cur.execute("UPDATE album SET stock = %s WHERE id = %s;", (stock, i))
    conn.commit()