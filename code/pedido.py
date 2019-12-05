import operacoes_carrinho
import finalizar_compra

def imprime(linha):
    print(' - '.join(map(str, linha)))

def func(conn,cur, id):
    cur.execute("SELECT count(album_id) FROM pedido WHERE cliente_id = %s;", (id,))
    q = cur.fetchone()[0]

    x=0
    if (q == 0):
        print("Carrinho está vazio.")

    else:
        cur.execute("SELECT album_id, nome, preco FROM pedido, album WHERE cliente_id = %s and album_id = album.id;",
                    (id,))
        for linha in cur.fetchall():
            imprime(linha)

    x = 0
    while x != '4':
        print('\n1 - Adicionar album\n2 - Remover album\n3 - Finalizar compras\n4 - Logout')
        x = input('\n')

        if x == '1':
            operacoes_carrinho.add(conn, cur, id)

        elif x == '2':
            print('Remover album')
            if(q == 0):
                 print("Nao é possivel remover.")
            else:
                operacoes_carrinho.rem(conn, cur, id)

        elif x == '3':
            print('Finalizar compras')
            if (q == 0):
                print("Nao é possivel finalizar compras pois não há álbum no carrinho.")
            else:
                finalizar_compra.finalizar(conn, cur, id)

        elif x == '4':
            print('Retornar')

        else:
            print("Opcao nao valida")

