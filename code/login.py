def func(cur):
    a = 1
    b = 1
    while a:
        print("----------------------------------------------------------------------------------")
        print("Login")

        while b:
            email = input("\nEmail: ")
            senha = input("Senha: ")

            cur.execute("SELECT count(email) FROM administrador WHERE email = %s;", (email,))
            a = cur.fetchone()

            cur.execute("SELECT count(email) FROM cliente WHERE email = %s;", (email,))
            c = cur.fetchone()
            b=0


        if(a[0] == 1 ):
            cur.execute("SELECT count(email) FROM administrador WHERE password = %s and email = %s;",(senha, email))
            s = cur.fetchone()[0]
            if (s == 0):
                print("\nEmail ou Password incorretos.")
                b=1

            else:
                b=0
                cur.execute("SELECT id FROM administrador WHERE password = %s and email = %s;",(senha, email))
                id = cur.fetchone()[0]
                return (0, id)


        elif(c[0] != 0):
            cur.execute("SELECT count(email) FROM cliente WHERE password = %s and email = %s;", (senha, email))
            t = cur.fetchone()[0]

            if (t == 0):
                print("\nEmail ou Password incorretos.")
                b=1

            else:
                b=0
                cur.execute("SELECT nome FROM cliente WHERE password = %s and email = %s;",(senha, email))
                nome = cur.fetchone()[0]
                return (1, nome)


        else:
            print("Email ou PassWord incorretos.\n")

    print("----------------------------------------------------------------------------------")








