import datetime

def finalizar(conn, cur, id, nome):
    print("\n")
    print('Usuario:', nome)
    print('FINALIZAR COMPRAS')

    # Regista o saldo do cliente disponivel
    cur.execute("SELECT saldo FROM cliente WHERE id = %s;", (id,))
    saldo = cur.fetchone()[0]
    print("Saldo disponivel: ", saldo)

    # Regista o valor total da compra
    cur.execute("SELECT SUM(preco) FROM pedido, album WHERE cliente_id = %s and album_id = album.id;", (id,))
    valor = cur.fetchone()[0]
    print("Valor Total: ", valor)

    # Ve se o cliente tem dinheiro suficiente
    if (saldo < valor):
        print("Dinheiro insuficiente.")

    else:
        #Procura ultimo id
        cur.execute("SELECT MAX(id) FROM historico_c WHERE cliente_id = %s;", (id,))
        j = cur.fetchone()[0]

        if(j is None):
            j=1
        else:
            j+=1

        #Regista novo pedido
        now = datetime.datetime.now()
        data = (str(now.day) + '-' + str(now.month) + '-' + str(now.year) + ' ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second))
        cur.execute("INSERT INTO historico_c  VALUES (%s,%s,%s);", (j, data, id))
        conn.commit()


        # Regista quantos albuns estao no pedido
        cur.execute("SELECT count(album_id) FROM pedido WHERE cliente_id = %s;", (id,))
        p = cur.fetchone()[0]

        #Procura o maior id registado em historico__C
        cur.execute("SELECT MAX(id) FROM historico_c WHERE cliente_id = %s;", (id,))
        j = cur.fetchone()[0]

        # Enquanto tiver pedido no carrinho
        while p != 0:
            #Procura o menor id dos albuns que tem no carrinho
            cur.execute("SELECT MIN(album_id) FROM pedido WHERE cliente_id = %s;", (id,))
            i = cur.fetchone()[0]

            # Ve quantos tem em stock e substrai 1
            cur.execute("SELECT stock FROM album WHERE id = %s;", (i,))
            stock = cur.fetchone()[0]

            # Insere no historico_c
            cur.execute("INSERT INTO historico_c_album VALUES (%s,%s);", (j, i))
            conn.commit()

            stock -= 1
            cur.execute("UPDATE album SET stock = %s WHERE id = %s;", (stock, i))
            conn.commit()

            # Precos do album atual
            cur.execute("SELECT preco FROM album WHERE id = %s;", (i,))
            preco = cur.fetchone()[0]

            # Atualizacao do saldo do cliente
            s_atual = (saldo-preco)
            cur.execute("UPDATE cliente SET saldo = %s WHERE id = %s;", (s_atual, id))
            conn.commit()

            #Deleta album comprado do carrinho
            cur.execute("DELETE FROM pedido WHERE album_id = %s and cliente_id = %s;", (i, id,))
            conn.commit()

            #Conta quantos albuns tem no carrinho
            cur.execute("SELECT count(album_id) FROM pedido WHERE cliente_id = %s;", (id,))
            p = cur.fetchone()[0]

        print("\nAlbuns comprados.")
        cur.execute("SELECT saldo FROM cliente WHERE id = %s;", (id,))
        saldo = cur.fetchone()[0]
        print("Saldo atualizado: ", saldo)