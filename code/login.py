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
                return '0', id


        elif(c[0] != 0):
            cur.execute("SELECT count(email) FROM cliente WHERE password = %s and email = %s;", (senha, email))
            t = cur.fetchone()[0]

            if (t == 0):
                print("\nEmail ou Password incorretos.")
                b=1

            else:
                b=0
                cur.execute("SELECT id FROM cliente WHERE password = %s and email = %s;",(senha, email))
                id = cur.fetchone()[0]
                return '1', id

        else: #Da opcao ao cliente para sair do meunu login
            print("Email ou PassWord incorretos.\n")
            z ='0'
            z = input("\nPrima 0 para sair ou 1 para tentar novamente ")
            if z=='0':
                return '2', None
            else:
                b=1

        print("----------------------------------------------------------------------------------")