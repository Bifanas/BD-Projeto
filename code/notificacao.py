import datetime

def func(conn,cur,id):
    a = '1'
    while a != '0':
        now= datetime.datetime.now()

        msg= input("Digite a mensagem: ")
        data = (str(now.day) + '-' + str(now.month) + '-' + str(now.year) + ' ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second))

        cur.execute("INSERT INTO notificacao (administrador_id, mensagem, data) values (%s,%s,%s);", (id, msg, data, ))
        conn.commit()

        cur.execute("SELECT id FROM notificacao WHERE data = %s;", (data,))
        idM = cur.fetchone()[0]

        cur.execute("SELECT count(id) FROM cliente;")
        ncliente = cur.fetchone()[0]

        for i in range(1,ncliente+1):
            cur.execute("INSERT INTO c_entrada values ('0',%s,%s);", (idM,i))
            conn.commit()

        a = input("Insere 0 para voltar: ")