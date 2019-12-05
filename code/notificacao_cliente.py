def imprime(linha):\
    print(' '.join(map(str, linha)))


def func(conn,cur,id):
    a = '1'
    while a != '0':

        #Verifica se há novas mensagens
        cur.execute("SELECT count(mensagem) FROM notificacao, c_entrada WHERE cliente_id = %s and mensagem_lida = false and c_entrada.notificacao_id=notificacao.id;", (id,))
        q = cur.fetchone()[0]

        #Mensagens novas
        if(q > 0):

            # Imprime no ecra as mensagens novas e atualiza elas para lidas
            print("Mensagens nao lida:")
            cur.execute("SELECT mensagem FROM notificacao, c_entrada WHERE cliente_id = %s and mensagem_lida = false and c_entrada.notificacao_id=notificacao.id;",(id,))
            for linha in cur.fetchall():
                imprime(linha)

            cur.execute("UPDATE c_entrada SET mensagem_lida = true WHERE cliente_id = %s and mensagem_lida = false;",(id, ))
            conn.commit()

        #Mensagem lidas
        else:

            # Imprime no ecra todas as mensagens ja lidas
            print("Mensagens lida:")
            cur.execute("SELECT mensagem FROM notificacao, c_entrada WHERE cliente_id = %s and mensagem_lida = true and c_entrada.notificacao_id=notificacao.id;",(id,))

            for linha in cur.fetchall():
                imprime(linha)

        a = input("Insere 0 para voltar: ")
