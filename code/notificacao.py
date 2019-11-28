import datetime

def func(conn,cur,id):
    a = '1'
    while a != '0':
        now= datetime.datetime.now()

        msg= input("Digite a mensagem: ")
        data = (str(now.day) + '-' + str(now.month) + '-' + str(now.year) + ' ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second))

        cur.execute("INSERT INTO notificacao (administrador_id, mensagem, data) values (%s,%s,%s);", (id, msg, data, ))
        conn.commit()

        a = input("Insere 0 para voltar: ")