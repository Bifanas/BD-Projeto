import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
cur = conn.cursor()

def func():
    x = 0
    while(x != 5):
        print("Pesquisa: ")
        print("1 - Por nome de album ")
        print("2 - Por nome de música ")
        print("3 - Por nome de género musical ")
        print("4 - Por nome de grupo ")
        print("5 - Voltar ")
        x = eval(input(''))

        if (x == 1):
            cur.execute("SELECT albumid, nome, tempo, data, preco FROM album WHERE stock > 0;")
            for linha in cur.fetchall():
                print(linha)

        elif (x == 2):
            cur.execute("SELECT  FROM  WHERE stock > 0;")
            for linha in cur.fetchall():
                print(linha)

        elif (x == 3):
            cur.execute("SELECT  FROM  WHERE stock > 0;")
            for linha in cur.fetchall():
                print(linha)
        elif (x == 4):
            cur.execute("SELECT  FROM  WHERE stock > 0;")
            for linha in cur.fetchall():
                print(linha)
        else:
            print("Opcao nao valida")