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

        while (cont != 0):
            albumID = eval(input('Insira outro albumID: '))
            cur.execute("SELECT count(albumid) FROM album WHERE albumid = %s;", (albumID,))
            cont = cur.fetchone()[0]

        a = 1
        while a:
            Nome = input("Nome do Album: ")
            if (len(Nome) != None):
                a = 0

        a = 1
        while a:
            Tempo = input("Duracao do Album: ")
            if (len(Tempo) != None):
                a = 0

        print("Data de Lançamento:")
        data = funcaoData.data()

        Stock = eval(input("Quantidade em stock: "))

        Preco = eval(input("Preco: "))

        cur.execute("INSERT INTO album values (%s,%s,%s,%s,%s,%s,0)", (albumID, Nome, Tempo, data, Stock, Preco))
        conn.commit()

