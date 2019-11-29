import datetime

def func(conn,cur,id):
    a = '1'
    while a != '0':
        cur.execute("SELECT count(notificacao_id) FROM c_entrada WHERE cliente_id = %s and mensagem_lida = false;", (id,))
        msg = cur.fetchone()[0]

        for i in range(0, msg+1):
            print("\nMensagem nao lida:")
            cur.execute("SELECT mensagem FROM notificacao, c_entrada WHERE cliente_id = 3 and mensagem_lida = false and c_entrada.notificacao_id=notificacao.id;", (id,))
            print( cur.fetchone()[i])




