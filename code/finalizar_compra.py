import datetime
import psycopg2
# vai importar todas as funcoes dos arquivos

conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
cur = conn.cursor()

def finalizar(conn, cur, id):
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
        # Regista quantos albuns estao no pedido
        cur.execute("SELECT count(album_id) FROM pedido WHERE cliente_id = %s;", (id,))
        p = cur.fetchone()[0]

        now = datetime.datetime.now()
        data = (str(now.day) + '-' + str(now.month) + '-' + str(now.year) + ' ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second))
        cur.execute("INSERT INTO historico_c (data_de_compra, cliente_id) VALUES (%s,%s);", (data, id))
        conn.commit()

        cur.execute("SELECT MAX(id) FROM historico_c WHERE cliente_id = %s;", (id,))
        j = cur.fetchone()[0]

        # Enquanto tiver pedido no carrinho
        while p != 0:

            cur.execute("SELECT MIN(album_id) FROM pedido WHERE cliente_id = %s;", (id,))
            i = cur.fetchone()[0]

            cur.execute("INSERT INTO historico_c_album VALUES (%s,%s);", (j, i))
            conn.commit()

            cur.execute("SELECT stock FROM album WHERE id = %s;", (i,))
            stock = cur.fetchone()[0]
            stock -= 1

            cur.execute("UPDATE album SET stock = %s WHERE id = %s;",(stock, i ))
            conn.commit()

            cur.execute("SELECT preco FROM album WHERE id = %s;",(i, ))
            preco = cur.fetchone()[0]

            s_atual = saldo - preco

            cur.execute("UPDATE cliente SET saldo = %s WHERE id = %s;", (s_atual,id))
            conn.commit()

            cur.execute("DELETE FROM pedido WHERE album_id = %s and cliente_id = %s;", (i, id,))
            conn.commit()




finalizar(conn,cur,1)