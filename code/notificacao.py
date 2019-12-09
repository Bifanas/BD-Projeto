import datetime

def func(conn,cur,id):
    print('\n')
    print('NOTIFICAR')

    # Enquanto o adm nao inserir 0 para voltar ao menu ficará enviando mensagens
    a = '1'
    while a != '0':

        #Registado a mensagem e a data de envio
        msg = input("Digite a mensagem: ")
        now = datetime.datetime.now()
        data = (str(now.day) + '-' + str(now.month) + '-' + str(now.year) + ' ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second))

        #Verfica se existe notificacao_ID registado
        cur.execute("SELECT count(id) FROM notificacao;")
        k = cur.fetchone()[0]
        if (k == 0):
            k = 1

        else:
            k += 1

       #Insere a notificacao na base de dados
        cur.execute("INSERT INTO notificacao (id, mensagem, data, administrador_id) values (%s,%s,%s,%s);", (k, msg, data, id))
        conn.commit()

        #Regista o id da mensagem
        cur.execute("SELECT id FROM notificacao WHERE data = %s;", (data,))
        idM = cur.fetchone()[0]

        #Conta quantos clientes estao registados
        cur.execute("SELECT count(id) FROM cliente;")
        ncliente = cur.fetchone()[0]

        #Envia
        for i in range(1,ncliente+1):
            cur.execute("INSERT INTO c_entrada values ('0',%s,%s);", (idM,i))
            conn.commit()

        a = input("Insira 0 para voltar: ")