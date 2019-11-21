import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=satanasreina")
cur = conn.cursor()

 # REGISTO DO CLIENTE
 # Os ciclos while servem para fazer a verificacao da variavel

def registo():

    us = input('Username: ')
    while(len(us) < 8):
        us = input('Insira o Username com pelo menos 8 digitos: ')

    senha = input('Senha: ')
    while(len(senha) < 8):
        senha = input('Insira a Password com pelo menos 8 digitos: ')

    nome = input('Nome: ')
    while (len(nome) < 8):
        nome = input('Insira o Nome com pelo menos 8 digitos: ')

    endereco = input('Endereco: ')
    while(len(endereco) < 8):
        endereco = input('Insira o Endereco com pelo menos 8 digitos: ')

    email = input('Email: ')
    while(len(email) < 8):
        email = input('Insira o Email com pelo menos 8 digitos: ')

    dia = input('Dia de nascimento: ')
    d=eval(dia)
    while(d<1 or d>31):
        dia = input('Dia de nascimento: ')
        d = eval(dia)

    mes = input('Mes de nascimento: ')
    m = eval(mes)
    while (m < 1 or m > 12):
        mes = input('Mes de nascimento: ')
        m = eval(mes)

    ano = input('Ano de nascimento: ')
    a = eval(ano)
    while (a < 1900 ):
        ano = input('Ano de nascimento: ')
        a = eval(ano)

    data = dia + '-' + mes + '-' + ano
    cur.execute("INSERT INTO cliente values (%s,%s,%s,%s,%s,%s,20)", (us, senha, nome, email, endereco, data))
    conn.commit()

cur.close()
conn.close()