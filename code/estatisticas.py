import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
cur = conn.cursor()

def func():
    a = 1
    while a:
        cur.execute("SELECT count(username) FROM cliente;")
        cont = cur.fetchone()[0]
        print("TOTAL DE CLIENTES: ", cont)

        cur.execute("SELECT count(albumid) FROM album;")
        cont = cur.fetchone()[0]
        print("\nTOTAL DE DISCOS: ", cont)

        cur.execute("SELECT count(preco) FROM album WHERE stock >0;")
        cont = cur.fetchone()[0]
        print("\nVALOR TOTAL DOS DISCOS EM STOCK: ", cont)

        cur.execute("SELECT count(preco) FROM historico_c;")
        cont = cur.fetchone()[0]
        print("\nVALOR TOTAL DAS VENDAS: ", cont)

        cur.execute("SELECT DISTINCT genero_tipo_genero, count(*) FROM album_genero GROUP BY genero_tipo_genero;")
        print("\nTOTAL DE DISCOS POR GENERO MUSICAL: ")
        for linha in cur.fetchall():
            print(linha)

        cur.execute("SELECT DISTINCT artista, count(*) FROM artista_genero  GROUP BY ;")
        print("\nTOTAL DE DISCOS VENDIDOS POR ARTISTA: ")
        for linha in cur.fetchall():
            print(linha)

        a = eval(input("Insere 0 para voltar: "))