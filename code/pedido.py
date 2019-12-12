import operacoes_carrinho
import finalizar_compra

def func(conn,cur, id, nome):
    x = 0
    while x != '4':
        print("\n")
        print('Usuario:', nome)
        print('CARRINHO')

        cur.execute("SELECT count(album_id) FROM pedido WHERE cliente_id = %s;", (id,))
        q = cur.fetchone()[0]

        x=0
        if (q == 0):
            print("Carrinho está vazio.")

        else:
            cur.execute("SELECT album_id, nome, preco FROM pedido, album WHERE cliente_id = %s and album_id = album.id ORDER BY album.id asc;",(id,))
            for linha in cur.fetchall():
                print("ID:", linha[0], " | Nome:", linha[1], " | Preço:", linha[2] )


        print('1 - Adicionar album\n2 - Remover album\n3 - Finalizar compras\n4 - Voltar')
        x = input('')

        if x == '1':
            operacoes_carrinho.add(conn, cur, id, nome)

        elif x == '2':
            if(q == 0):
                 print("Nao é possivel remover.")
            else:
                operacoes_carrinho.rem(conn, cur, id, nome)

        elif x == '3':
            if (q == 0):
                print("Nao é possivel finalizar compras pois não há álbum no carrinho.")
            else:

                finalizar_compra.finalizar(conn, cur, id, nome)

        elif x == '4':
            print('Retornar')

        else:
            print("Opcao nao valida")

