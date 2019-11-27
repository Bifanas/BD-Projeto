import psycopg2
import funcaoData

# REGISTO DO CLIENTE
# São pedidos ao usuario que insira seus dados como username, password, nome, email e data de nascimento
# Para o username e o email é verificado se existe outro usuario que ja tenha inserido certo dado e tambem é verificado se o campo nao esta vazio
# Para a senha e o nome so verifica se o campo nao está vazio
# Para a data de nascimento é chamado a funcaoData que recolhe as informacoes e organiza no formato.

def func(conn,cur):
    print("----------------------------------------------------------------------------------")
    print("Registar-se")

    a = 1
    b = 1

    while (a or b):
        a = 0
        user = input('Username: ')
        if(len(user) < 0):
            print('Insira um Username com pelo menos 6 caracteres')
            a = 1

        #verifica se o username ja foi escolhido por outro usuario
        cur.execute("SELECT count(username) FROM cliente WHERE username = %s;", (user,))
        cont = cur.fetchone()[0]
        b = 0
        if (cont != 0):
            print('Insira outro Username')
            b = 1

    a=1
    while a:
        senha = input('Password: ')
        a=0
        if (len(senha) < 0):
            a=1

    a=1
    while a:
        nome = input('Nome: ')
        a=0
        if (len(nome) < 1):
            a=1

    a=1
    b=1
    while a or b:
        email = input('Email: ')
        a=0
        if(len(email) < 1):
            a=1

        cur.execute("SELECT count(username) FROM cliente WHERE email = %s;", (email,))
        cont = cur.fetchone()[0]

        b = 0
        if (cont != 0):
            print('Insira outro email. ')
            b = 1

    data = funcaoData.data()
    print("Cliente Registado.")
    print("----------------------------------------------------------------------------------")
    cur.execute("INSERT INTO cliente values (%s,%s,%s,%s,%s,20)", (user, senha, nome, email, data))
    conn.commit()