# É solicitado ao adm que insira o nome do album que deseja remover.
# É verificado se este album existe e caso não é pedido de novo o nome do album
# Caso o album exista é verificado se este album ja foi comprado por algum cliente.
# Se ja foi comprado, aparece uma msg de erro.
# Se nao foi comprado por nenhum cliente, entao é eliminado da base de dados.

def imprime(linha):
    print('       '.join(map(str, linha)))

def func(conn, cur):
    print('\nRemover album')
    a = '1'

    # Enquanto o adm nao inserir 0 para voltar ao menu ficará removendo album
    while a != '0':
        b = 1
        # Enquanto o adm nao inserir o nome correto ficara pedindo o nome do album
        while b:
            q = 0

            #Procura album com o nome dado
            nome = input("Insira o nome do album: ")
            cur.execute("SELECT count(*) FROM album WHERE nome = %s GROUP BY nome;", (nome,))
            q = cur.fetchone()[0]

            #Caso nao exista
            if (q is None):
                print("Não existe album com este nome.")
                b=1

            #Caso exista, mostra no ecra todos os albuns com o mesmo nome
            else:
                print("ID       NOME       PRECO")
                cur.execute("SELECT id, nome, preco FROM album WHERE nome = %s ORDER BY id;", (nome,))
                for linha in cur.fetchall():
                    imprime(linha)
                id = eval(input("Insira o albumID: "))
                b=0

        # Verifica se o album ja foi comprado
        cur.execute("SELECT count(*) FROM historico_c_album WHERE album_id = %s;", (id,))
        cont = cur.fetchone()[0]

        if (cont != 0 ):
            print("Não é possivel eliminar este album pois algum cliente já o comprou.")
            b=1

        else:
            #Deleta das tabelas existentes
            conn.begin()
            cur.execute("DELETE FROM album_genero WHERE album_id = %s;", (id,))
            cur.execute("DELETE FROM musica_album WHERE album_id = %s;", (id,))
            cur.execute("DELETE FROM artista_album WHERE album_id = %s;", (id,))
            cur.execute("DELETE FROM historico_a WHERE album_id = %s;", (id,))
            cur.execute("DELETE FROM album WHERE id = %s;", (id,))
            conn.commit()
            b=0

        a = input("Insere 0 para voltar: ")
