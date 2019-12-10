def func(conn,cur,id,nome):
    x = '0'  # inicializa o valor de x
    while x != '3':
        print('\n')
        print('Usuário:', nome)
        print('NOTIFICAÇÕES')
        print('1 - Ler Novas Mensagens\n2 - Ler Antigas Mensagens\n3 - Voltar')
        x = input('')

        if x == '1':
            novas_msg(conn, cur, id, nome)

        elif x == '2':
            antigas_msg(cur, id, nome)
        elif x == '3':
            print('\n')
            print("VOLTAR")

        else:
            print('\n')
            print("Opção não válida")

def novas_msg(conn, cur,id, nome):
    #Verifica se há novas mensagens
    cur.execute("SELECT count(mensagem) FROM notificacao, c_entrada WHERE cliente_id = %s and mensagem_lida = false and c_entrada.notificacao_id=notificacao.id;", (id,))
    q = cur.fetchone()[0]

    #Mensagens novas
    if(q > 0):

        # Imprime no ecra as mensagens novas e atualiza elas para lidas
        print('\n')
        print('Usuário:', nome)
        print("MENSAGENS NÃO LIDAS\n")
        cur.execute("SELECT mensagem, data FROM notificacao, c_entrada WHERE cliente_id = %s and mensagem_lida = false and c_entrada.notificacao_id=notificacao.id;",(id,))
        for linha in cur.fetchall():
            print("Data:", linha[1])
            print("Mensagem:", linha[0])
            print('')



        cur.execute("UPDATE c_entrada SET mensagem_lida = true WHERE cliente_id = %s and mensagem_lida = false;",(id, ))
        conn.commit()


    else:
        print("Não há novas mensagens")

#Mensagem lidas
def antigas_msg(cur,id, nome):
    cur.execute("SELECT count(mensagem) FROM notificacao, c_entrada WHERE cliente_id = %s and mensagem_lida = true and c_entrada.notificacao_id=notificacao.id;",(id,))
    l = cur.fetchone()[0]

    if(l != 0):
        # Imprime no ecra todas as mensagens ja lidas
        print('\n')
        print('Usuário:', nome)
        print("MENSAGENS NÃO LIDAS\n")
        cur.execute("SELECT mensagem, data FROM notificacao, c_entrada WHERE cliente_id = %s and mensagem_lida = true and c_entrada.notificacao_id=notificacao.id;",(id,))
        for linha in cur.fetchall():
            print("Data:", linha[1])
            print("Mensagem:", linha[0])
            print('')

    else:
        print("Não há mensagens antigas.")
