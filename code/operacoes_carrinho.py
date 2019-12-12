

#Adicionar album no carrinho
def add(conn, cur,id,nome):
    x = '1'
    while(x != '2'):
        if (x == '1'):
            print('\n')
            print('Usuario:', nome)
            print('ADICIONAR ALBUM AO CARRINHO')
            cur.execute("SELECT id, nome, preco FROM album WHERE stock > 0;", (id,))
            for linha in cur.fetchall():
                print("ID: ", linha[0], " | Nome:", linha[1], " | Preço:", linha[2])

            # Pede q o cliente insira o respectivo id
            i = input("Digite o ID do album: ")
            while (i[0] < '1' or i[0] > '9'):
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

            if (q < 1):
                print("Album indisponivel")

            # Insere no pedido o album e o cliente
            else:
                cur.execute("INSERT INTO pedido VALUES (%s,%s);", (id, i))
                conn.commit()

                # Mostra total de compras
                cur.execute("SELECT SUM(preco) FROM pedido, album WHERE cliente_id = %s and album_id = album.id;",
                            (id,))
                print("Valor Total No Carrinho: ", cur.fetchone()[0])

            print("Deseja adicionar outro album no carrinho? ")
            print("1 - SIM\n2 - NAO")
            x = input('')

        elif (x == '2'):
            return

        else:
            print("Opção não válida.")


# Remover album do carrinho
def rem(conn,cur,id,nome):
    print('\n')
    print('Usuario:', nome)
    print('REMOVER ALBUM AO CARRINHO')

    x = '1'
    while (x != '2'):
        if(x == '1'):
            #Mostra os pedidos no carrinho
            cur.execute("SELECT album_id, nome, preco FROM pedido, album WHERE cliente_id = %s and album_id = album.id ORDER BY album.id asc;",(id,))
            for linha in cur.fetchall():
                print("ID:", linha[0], "Nome:", linha[1], "Preço:", linha[2])

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

            cur.execute("DELETE FROM pedido WHERE cliente_id = %s and album_id = %s;", (id, i))
            conn.commit()

            #Mostra total no carrinho
            cur.execute("SELECT SUM(preco) FROM pedido, album WHERE cliente_id = %s and album_id = album.id;", (id,))
            s = cur.fetchone()[0]
            if (s is not None):
                print("\nValor Total: ", cur.fetchone()[0])

            else:
                print("\nCarrinho vazio.")

        return