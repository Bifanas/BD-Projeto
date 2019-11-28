# É pedido o username do cliente e verifica se este está na base de dados.
# Se nao estiver é mostrado uma mensagem de erro.
# Se existir este username é solicitado o novo valo do saldo do cliente, somado ao saldo do anterior e atualizado.

def func(conn, cur):
    a = '1'
    while a != '0':
        nome = input("Insira o USERNAME do cliente: ")
        cur.execute("SELECT count(nome) FROM cliente WHERE username = %s;", (nome,))
        cont = cur.fetchone()[0]

        if(cont == 0):
            print("Não existe cliente com este username.")
        else:
            saldo = eval(input("Insira o saldo: "))
            cur.execute("SELECT saldo FROM cliente WHERE username = %s;", (nome,))
            saldo_anterior = cur.fetchone()[0]
            s_atual = saldo + saldo_anterior

            cur.execute("UPDATE cliente SET saldo = %s WHERE username = %s;", (s_atual, nome))
            conn.commit()

        a = input("Insere 0 para voltar: ")