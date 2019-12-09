# É solicitado ao adm que insira o nome do album que deseja remover.
# É verificado se este album existe e caso não é pedido de novo o nome do album
# Caso o album exista é verificado se este album ja foi comprado por algum cliente.
# Se ja foi comprado, aparece uma msg de erro.
# Se nao foi comprado por nenhum cliente, entao é eliminado da base de dados.

def func(conn, cur):
    print('\n')
    print('REMOVER ÁLBUM')
    a = '1'

    # Enquanto o adm nao inserir 0 para voltar ao menu ficará removendo album
    while a != '0':
        b = 1
        # Enquanto o adm nao inserir o nome correto ficara pedindo o nome do album
        while b:
            q = 0

            #Procura album com o nome dado
            nome = input("Insira o nome do álbum: ")
            cur.execute("SELECT count(*) FROM album WHERE nome = %s;", (nome,))
            q = cur.fetchone()[0]
            #Caso nao exista
            if (q == 0):
                print("Não existe álbum com este nome.")
                b=1
                z = '0'
                z = input("Prima 0 para sair ou 1 para tentar novamente: ")
                if z == '0':
                    return

            #Caso exista, mostra no ecra todos os albuns com o mesmo nome
            else:
                if(q != 1):
                    cur.execute("SELECT id, nome, preco FROM album WHERE nome = %s ORDER BY id;", (nome,))
                    for linha in cur.fetchall():
                        print("ID:", linha[0], " | Nome:", linha[1], " | Preço: ", linha[2])

                    # Verifica se digitou o id certo
                    i = eval(input("Insira o albumID: "))
                    cur.execute("SELECT count(*) FROM album WHERE id = %s and nome = %s;", (i, nome))
                    f = cur.fetchone()[0]
                    while (f == 0):
                        z = '0'
                        z = input("Prima 0 para sair ou 1 para tentar novamente: ")
                        if z == '0':
                            return
                        i = eval(input("Insira o albumID: "))
                        cur.execute("SELECT count(*) FROM album WHERE id = %s and nome = %s;", (i, nome))
                        f = cur.fetchone()[0]
                    b = 0

                # Existe só um
                else:
                    cur.execute("SELECT id FROM album WHERE nome = %s;", (nome,))
                    i = cur.fetchone()[0]
                    b = 0

        # Verifica se o album ja foi comprado
        cur.execute("SELECT count(*) FROM historico_c_album WHERE album_id = %s;", (i,))
        cont = cur.fetchone()[0]

        if (cont != 0 ):
            print("Não é possivel eliminar este álbum pois algum cliente já o comprou.")

        else:
            #Deleta das tabelas existentes
            cur.execute("DELETE FROM album_genero WHERE album_id = %s;", (i,))
            cur.execute("DELETE FROM musica_album WHERE album_id = %s;", (i,))
            cur.execute("DELETE FROM artista_album WHERE album_id = %s;", (i,))
            cur.execute("DELETE FROM historico_a WHERE album_id = %s;", (i,))
            cur.execute("DELETE FROM album WHERE id = %s;", (i,))
            conn.commit()

        a = input("Insira 0 para voltar: ")