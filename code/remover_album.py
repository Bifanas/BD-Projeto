import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
cur = conn.cursor()


# É solicitado ao adm que insira o nome do album que deseja remover.
# É verificado se este album existe e caso não é pedido de novo o nome do album
# Caso o album exista é verificado se este album ja foi comprado por algum cliente.
# Se nao foi comprado por nenhum cliente, entao é eliminado da base de dados.
# Se ja foi comprado, aparece uma msg de erro.
def imprime(linha):
    print('       '.join(map(str, linha)))

def func(conn, cur):
    a = 1
    while a:
        q=0
        nome = input("Insira o nome do album: ")
        cur.execute("SELECT count(*) FROM album WHERE nome = %s GROUP BY nome;", (nome,))
        q = cur.fetchone()[0]
        if (q == 0):
            print("Não existe album com este nome.")

        elif(q > 1):
            print("ID       NOME       PRECO")
            cur.execute("SELECT id, nome, preco FROM album WHERE nome = %s ORDER BY id;", (nome,))
            for linha in cur.fetchall():
                imprime(linha)
            id = eval(input("Insira o albumID: "))

        else:
            cur.execute("SELECT id FROM album WHERE nome = %s;", (nome,))
            id = cur.fetchone()[0]

        cont=0
        cur.execute("SELECT count(*) FROM historico_c_album WHERE album_id = %s GROUP BY album_id;", (id,))
        cont = str(cur.fetchone()[0])
        print(cont)

        if (cont == 0):
            cur.execute("DELETE FROM album WHERE albumid = %s;", (ID,))
            conn.commit()
        else:
            print("Não é possivel eliminar este album pois algum cliente já o comprou.")

        a = eval(input("Insere 0 para voltar: "))
