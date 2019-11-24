import psycopg2
import funcaoData
import add

conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
cur = conn.cursor()

# ADICIONAR ALBUM À BASE DE DADOS

def adicionar_album():
    a=1
    while a:
        # Pede que digite o albumID do album e verifica se este ja existe na base de dados
        albumID = eval(input("AlbumID: "))
        cur.execute("SELECT count(albumid) FROM album WHERE albumid = %s;", (albumID,))
        cont = cur.fetchone()[0]


        a = 1
        while a:
            Tempo = input("Duracao do Album: ")
            if (len(Tempo) != None):
                a = 0

        print("Data de Lançamento:")
        data = funcaoData.data()

        Stock = eval(input("Quantidade em stock: "))

        Preco = eval(input("Preco: "))

        cur.execute("INSERT INTO album values (%s,%s,%s,%s,%s,%s,%s)", (albumID, Nome, Tempo, data, Stock, Preco))
        cur.execute("INSERT INTO historico_a values (%s,%s,%s)", (Preco, Stock, albumID))
        conn.commit()

