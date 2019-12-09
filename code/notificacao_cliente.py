def imprime(linha):\
    print(' '.join(map(str, linha)))


def func(conn,cur,id):
    x = '0'  # inicializa o valor de x
    while x != '3':
        print('1 - Ler Novas Mensagens\n2 - Ler Antigas Mensagens\n3 - Voltar')
        x = input('')

        if x == '1':
            novas_msg(conn, cur, id)

        elif x == '2':
            antigas_msg(cur, id)
        elif x == '3':
            print("Retornar")

        else:
            print("\nOpcao nao valida")

def novas_msg(conn, cur,id):
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
        print("\n")

    else:
        print("Não há novas mensagens\n")

#Mensagem lidas
def antigas_msg(cur,id):
    cur.execute("SELECT count(mensagem) FROM notificacao, c_entrada WHERE cliente_id = %s and mensagem_lida = true and c_entrada.notificacao_id=notificacao.id;",(id,))
    l = cur.fetchone()[0]

    if(l != 0):
        # Imprime no ecra todas as mensagens ja lidas
        print("Mensagens lida:")
        cur.execute("SELECT mensagem FROM notificacao, c_entrada WHERE cliente_id = %s and mensagem_lida = true and c_entrada.notificacao_id=notificacao.id;",(id,))
        for linha in cur.fetchall():
            imprime(linha)
        print("\n")

    else:
        print("Não há antigas mensagens.\n")
