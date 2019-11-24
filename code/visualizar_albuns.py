import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
cur = conn.cursor()

# Mostra todos os albuns disponiveis em stock

def visualiza():
    if True:
        cur.execute("SELECT * FROM album WHERE stock > 0;")
        print(cur.fetchall())



