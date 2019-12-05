import pesquisa

def imprime(linha):
    print(' - '.join(map(str, linha)))

#Adicionar album no carrinho
def add(conn, cur,id):
    add = input("Deseja adicionar album no carrinho? [s/n]")
    while (add == 'S' or add == 's'):
        pesquisa(conn, cur, id)

        cur.execute("SELECT SUM(preco) FROM pedido, album WHERE cliente_id = %s and album_id = album.id;", (id,))
        print("Valor Total: ", cur.fetchone()[0])
        add = input("Deseja adicionar album no carrinho? [s/n]")


# Remover album do carrinho
def rem(conn,cur,id):
    remover = input("Deseja remover album do carrinho? [s/n]")
    while (remover == 's' or remover == 'S'):
        cur.execute("SELECT album_id, nome, preco FROM pedido, album WHERE cliente_id = %s and album_id = album.id;",(id,))
        for linha in cur.fetchall():
            imprime(linha)

        n = eval(input("Insira o albumID: "))
        cur.execute("DELETE FROM pedido WHERE cliente_id = %s and album_id = %s;", (id, n))
        conn.commit()
        cur.execute("SELECT SUM(preco) FROM pedido, album WHERE cliente_id = %s and album_id = album.id;", (id,))
        print("Valor Total: ", cur.fetchone()[0])
        remover = input("Deseja remover album no carrinho? [s/n]")















