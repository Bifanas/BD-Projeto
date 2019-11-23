import psycopg2

conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
cur = conn.cursor()

def remover_album():

    nome = input("Insira o Nome da musica")
    cur.execute("SELECT count(nome) FROM album WHERE nome = %s;", (nome,))
    cont = cur.fetchone()[0]

    while(cont == 0):
        print("Nao existe um album com este nome.")
        nome = input("Insira o Nome da musica")
        cur.execute("SELECT count(nome) FROM album WHERE nome = %s;", (nome,))
        cont = cur.fetchone()[0]


    cur.execute("SELECT * FROM album WHERE nome = %s;", (nome,))
    print(cur.fetchall())
    ID = eval(input("Insira o ID do album"))

    cur.execute("DELETE FROM album WHERE albumid = %s;", (ID,))
    cur.execute("DELETE FROM musica_album WHERE albumid = %s;", (ID,))
    cur.execute("DELETE FROM artista_album WHERE albumid = %s;", (ID,))
    cur.execute("DELETE FROM genero_album WHERE albumid = %s;", (ID,))
    conn.commit()


