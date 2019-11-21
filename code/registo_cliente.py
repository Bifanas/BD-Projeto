import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
cur = conn.cursor()

# INCOMPLETO

# FORMATACAO DA DATA
def dataNascimento ():
    d = 0
    while(d<1 or d>31):
        dia = input('Insira o dia de nascimento: ')

        if(dia[0] == '0' and dia[1] == '\0'):
            dia = input('Insira o dia de nascimento: ')
        elif(dia[0] == '0' and dia[1] != None):
            d = eval(dia[1])

        else:
            d = eval(dia)

    m = 0
    while (m < 1 or m > 12):
        mes = input('Insira novamente o mes de nascimento: ')
        m = eval(mes)

    ano = input('Ano de nascimento: ')
    a = eval(ano)
    while (a < 1900):
        ano = input('Ano de nascimento: ')
        a = eval(ano)
    data = dia + '-'+ mes + '-' + ano

    return data

# REGISTO DO CLIENTE
# Os ciclos while servem para fazer a verificacao da variavel
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

registo_cliente()

cur.close()
conn.close()