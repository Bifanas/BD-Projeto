import psycopg2
import funcaoData
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
cur = conn.cursor()


# REGISTO DO CLIENTE
# Os ciclos while servem para verificar se a variavel tem pelo menos 8 digitos

def registo_cliente():
    us = input('Username: ')
    while (len(us) < 8):
        us = input('Insira o Username com pelo menos 8 digitos: ')

    cur.execute("SELECT count(username) FROM cliente WHERE username = %s;", (us,))
    a = cur.fetchone()[0]
    while (a != 0):
        us = input('Insira outro Username: ')
        cur.execute("SELECT count(username) FROM cliente WHERE username = %s;", (us,))
        a = cur.fetchone()[0]

    senha = input('Senha: ')
    while (len(senha) < 8):
        senha = input('Insira a Password com pelo menos 8 digitos: ')

    nome = input('Nome: ')
    while (len(nome) < 8):
        nome = input('Insira o Nome com pelo menos 8 digitos: ')

    endereco = input('Endereco: ')
    while (len(endereco) < 8):
        endereco = input('Insira o Endereco com pelo menos 8 digitos: ')

    email = input('Email: ')
    while (len(email) < 8):
        email = input('Insira o Email com pelo menos 8 digitos: ')

    data = funcaoData.data()

    cur.execute("INSERT INTO cliente values (%s,%s,%s,%s,%s,%s,20)", (us, senha, nome, email, endereco, data))
    conn.commit()
