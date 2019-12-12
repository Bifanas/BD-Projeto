import funcaoData
# REGISTO DO CLIENTE
# São pedidos ao usuario que insira seus dados como nome, password, email e data de nascimento
# Para o email é verificado se existe outro usuario que ja tenha inserido certo dado e tambem é verificado se o campo nao esta vazio
# Para a senha e o nome so verifica se o campo nao está vazio
# Para a data de nascimento é chamado a funcaoData que recolhe as informacoes e organiza no formato.

def func(conn,cur):
    print("\n")
    print("REGISTAR-SE")
    a = 1
    b = 1

    a=1
    while a:
        nome = input('Nome: ')
        a=0
        if (len(nome) < 1):
            a=1

    a = 1
    while a:
        senha = input('Password: ')
        a = 0
        if (len(senha) < 4):
            print("Password fraca, insira outra")
            a = 1

    a=1
    b=1
    while a or b:
        email = input('Email: ')
        a=0
        if(len(email) < 5):
            a=1

        cur.execute("SELECT count(id) FROM cliente WHERE email = %s;", (email,))
        cont = cur.fetchone()[0]

        b = 0
        if (cont != 0):
            print('Insira outro email. ')
            b = 1

    print("Data de nascimento:")
    data = funcaoData.data()

    #Verfica se existe cliente registado
    cur.execute("SELECT count(id) FROM cliente;")
    k = cur.fetchone()[0]
    if(k == 0):
        k=1

    else:
        k+=1

    print("\n")
    print("CONFIRMAÇÃO DOS DADOS INSERIDOS")
    print("Nome:", nome)
    print("Email:", email)
    print("Data de Nascimento:", data)
    print("1 - Confirmar\n2 - Corrigir\n3 - Voltar")
    a = input('')

    if(a == '1'):
        cur.execute("INSERT INTO cliente (id, nome, password, email, data_nascimento, saldo) values (%s,%s,%s,%s,%s,20)", (k,nome,senha, email, data))
        conn.commit()
        print("Cliente Registado.")

    elif(a == '2'):
        func(conn,cur)

    elif(a == '3'):
        return

    else:
        print("Opção não válida.")