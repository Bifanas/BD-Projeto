import psycopg2
import funcaoData
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
cur = conn.cursor()


# REGISTO DO CLIENTE
# Os ciclos while servem para verificar se a variavel tem pelo menos 1 digito

def registo_cliente():
    a = 1
    b = 1
    while (a or b):
        a = 0
        user = input('Username: ')
        if(len(user) < 6):
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
        if (len(senha) < 8):
            a=1

    a=1
    while a:
        nome = input('Nome: ')
        a=0
        if (len(nome) < 1):
            a=1

    a=1
    while a:
        endereco = input('Endereco: ')
        a=0
        if(len(endereco) < 1):
            a=1

    a=1
    while a:
        email = input('Email: ')
        a=0
        if(len(email) < 1):
            a=1

    data = funcaoData.data()

    cur.execute("INSERT INTO cliente values (%s,%s,%s,%s,%s,%s,20)", (user, senha, nome, email, endereco, data))
    conn.commit()
