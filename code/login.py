import psycopg2

conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
cur = conn.cursor()


def func():
    c = 0
    a = 0
    while (c == 0 and a == 0):

        user = input("USERNAME: ")
        senha = input("SENHA: ")

        aux = 0

        cur.execute("SELECT count(*) FROM administrador WHERE email = %s GROUP BY email;", (user, ))
        aux = cur.fetchone()[0]
        print(aux)

        if (aux == 1):
            cur.execute("SELECT count(email) FROM administrador WHERE email = %s GROUP BY email;", (user,))
            a = cur.fetchone()[0]

        else:
            cur.execute("SELECT count(username) FROM cliente WHERE username = %s GROUP BY nome;", (user,))
            c = cur.fetchone()[0]


        if (c == 0 and a == 0):
            print("Username ou PassWord incorretos.")


    if (a == 1):  # email do adm detectado
        s = 0
        while (s == 0):
            cur.execute("SELECT count(password) FROM administrador WHERE password = %s and email = %s;", (senha, user))
            s = cur.fetchone()[0]
            if (s == 0):
                print("Username ou Password incorretos.")
                user = input("USERNAME: ")
                senha = input("SENHA: ")
            else:
                print("ADM")
                return 0

    elif (c == 1):  # username do cliente detectado
        s = 0
        while (s == 0):
            cur.execute("SELECT count(password) FROM cliente WHERE password = %s and username = %s;", (senha, user))
            s = cur.fetchone()[0]
            if (s == 0):
                print("Username ou Password incorretos.")
                user = input("USERNAME: ")
                senha = input("SENHA: ")
            else:
                print("CLIENTE")
                return 1

