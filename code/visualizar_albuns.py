import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
cur = conn.cursor()

# Mostra todos os albuns disponiveis em stock
def imprime(linha):
    print('       '.join(map(str, linha)))


def func():
    a = 1
    while a:
        cur.execute("SELECT * FROM album WHERE stock > 0;")
        print ("ID | NOME | DURACAO | DATA  | QUANT | STOCK")

        for linha in cur.fetchall():
            imprime(linha)

        a = eval(input("Insere 0 para voltar: "))


func()