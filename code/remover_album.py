import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
cur = conn.cursor()


# É solicitado ao adm que insira o nome do album que deseja remover.
# É verificado se este album existe e caso não é pedido de novo o nome do album
# Caso o album exista é verificado se este album ja foi comprado por algum cliente.
# Se nao foi comprado por nenhum cliente, entao é eliminado da base de dados.
# Se ja foi comprado, aparece uma msg de erro.

def remover_album():
    a = 1
    while a:
        nome = input("Insira o Nome do album: ")
        cur.execute("SELECT count(nome) FROM album WHERE nome = %s;", (nome,))
        cont = cur.fetchone()[0]

        while (cont == 0):  # VERIFICAR SE EXISTE UM ALBUM COM ESTE NOME
            print("Nao existe um album com este nome.")
            nome = input("Insira o Nome do album: ")
            cur.execute("SELECT count(nome) FROM album WHERE nome = %s;", (nome,))
            cont = cur.fetchone()[0]

        cur.execute("SELECT albumid, nome FROM album WHERE nome = %s;", (nome,))
        print(cur.fetchall())

        ID = eval(input("Insira o ID do album: "))
        cur.execute("SELECT count(nome_album) FROM historico_c WHERE albumid = %s;", (ID,))

        cont = cur.fetchone()[0]
        if (cont == 0):
            cur.execute("DELETE FROM album WHERE albumid = %s;", (ID,))
            conn.commit()
        else:
            print("Não é possivel eliminar este album pois algum cliente já o comprou.")

        a = eval(input("Digite 1 para retirar outro album: "))
