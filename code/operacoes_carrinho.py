def imprime(linha):
    print(' - '.join(map(str, linha)))

#Adicionar album no carrinho
def add(conn, cur,id):
    add = 's'

    #Verifica se o cliente quer adicionar album no carrinho
    while (add == 'S' or add == 's'):

        #Permite ao cliente ver o id do album que quer adicionar ao carrinho
        v = input("Deseja ver os album em stock? [s/n]")
        while(v == 's' or v == 'S'):
            cur.execute("SELECT id, nome, preco FROM album WHERE stock > 0;", (id,))
            for linha in cur.fetchall():
                imprime(linha)
            v = 'n'
        #Pede q o cliente insira o respectivo id
        i = eval(input("Digite o ID do album: "))

        #Verifica se o album tem em stock
        cur.execute("SELECT stock FROM album WHERE id = %s;", (i,))
        q = cur.fetchone()[0]
        if(q<1):
            print("Album indisponivel")

        #Insere no pedido o album e o cliente
        else:
            cur.execute("INSERT INTO pedido VALUES (%s,%s);", (id,i))

            #Mostra total de compras
            cur.execute("SELECT SUM(preco) FROM pedido, album WHERE cliente_id = %s and album_id = album.id;", (id,))
            print("Valor Total No Carrinho: ", cur.fetchone()[0])

        add = input("Deseja adicionar outro album no carrinho? [s/n]")


# Remover album do carrinho
def rem(conn,cur,id):
    remover = 's'

    #Verifica se quer remover do pedido
    while (remover == 's' or remover == 'S'):

        #Mostra os pedidos no carrinho
        cur.execute("SELECT album_id, nome, preco FROM pedido, album WHERE cliente_id = %s and album_id = album.id;",(id,))
        for linha in cur.fetchall():
            imprime(linha)

        #Pede o id e deleta do carrinho
        n = eval(input("Insira o albumID: "))
        cur.execute("DELETE FROM pedido WHERE cliente_id = %s and album_id = %s;", (id, n))
        conn.commit()

        #Mostra total no carrinho
        cur.execute("SELECT SUM(preco) FROM pedido, album WHERE cliente_id = %s and album_id = album.id;", (id,))
        print("Valor Total: ", cur.fetchone()[0])

        remover = input("Deseja remover outro album no carrinho? [s/n]")