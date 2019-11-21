import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
cur = conn.cursor()

 # REGISTO DO CLIENTE
 # Os ciclos while servem para fazer a verificacao da variavel

def registo_cliente():

    us = input('Username: ')
    while(len(us) < 8):
        us = input('Insira o Username com pelo menos 8 digitos: ')

    cur.execute("SELECT count(username) FROM cliente WHERE username = %s;",(us,))
    a = cur.fetchone()[0]
    while (a != 0):
        us = input('Insira outro Username: ')
        cur.execute("SELECT count(username) FROM cliente WHERE username = %s;", (us,))
        a = cur.fetchone()[0]


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
    if(dia[0] == '0'):
        d=eval(dia[1])
    else:
        d=eval(dia)
    while(d<1 or d>31):
        dia = input('Dia de nascimento: ')
        d = eval(dia)
        if(dia[0] == '0'):
            d=eval(dia[1])
        else:
            d=eval(dia)

    mes = input('Mes de nascimento: ')
    if(mes[0] == '0'):
        m = eval(mes[1])
    else:
        m = eval(mes)
    while (m < 1 or m > 12):
        mes = input('Mes de nascimento: ')
        m = eval(mes)
        if(dia[0] == '0'):
            d=eval(dia[1])
        else:
            d=eval(dia)

    ano = input('Ano de nascimento: ')
    if(ano[0] == 0):
        a = eval(ano[1])
    else:
        a = eval(ano)

    while (a < 1900 ):
        ano = input('Ano de nascimento: ')
        a = eval(ano)
        if (ano[0] == 0):
            a = eval(ano[1])
        else:
            a = eval(ano)


    data = dia + '-' + mes + '-' + ano
    cur.execute("INSERT INTO cliente values (%s,%s,%s,%s,%s,%s,20)", (us, senha, nome, email, endereco, data))
    conn.commit()

registo_cliente()

cur.close()
conn.close()