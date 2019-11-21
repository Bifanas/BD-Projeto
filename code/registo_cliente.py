import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
cur = conn.cursor()

# FORMATACAO DA DATA dd-mm-aaaa
def dataNascimento ():
    d = 0
    while(d<1 or d>31):
        dia = input('Insira o dia de nascimento: ')
        d = eval(dia)

    if(d<10):
        aux=dia
        dia = '0' + aux

    m = 0
    while (m < 1 or m > 12):
        mes = input('Insira o mes de nascimento: ')
        m = eval(mes)

    if(m<10):
        aux = mes
        mes = '0' + aux

    ano = input('Ano de nascimento: ')
    a = eval(ano)
    while (a < 1900):
        ano = input('Ano de nascimento: ')
        a = eval(ano)

    data = dia + '-'+ mes + '-' + ano

    return data

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

    data = dataNascimento()

    cur.execute("INSERT INTO cliente values (%s,%s,%s,%s,%s,%s,20)", (us, senha, nome, email, endereco, data))
    conn.commit()

cur.close()
conn.close()