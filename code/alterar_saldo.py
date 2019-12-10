# É pedido o nome do cliente e verifica se este está na base de dados.
# Se nao estiver é mostrado uma mensagem de erro.
# Se existir este username é solicitado o novo valo do saldo do cliente, somado ao saldo do anterior e atualizado.

def func(conn, cur):
    print("\n")
    print('ALTERAR SALDO')

    # Enquanto o adm nao inserir 0 para voltar ao menu ficará alterando saldo
    a = 1
    while a != '0':

        # Enquanto o adm nao inserir o nome correto ficara pedindo o nome do cliente
        b = 1
        while b:

            # Procura o nome do cliente na base de dados
            nome = input("Insira o nome do cliente: ")
            cont=0
            cur.execute("SELECT count(nome) FROM cliente WHERE nome = %s;", (nome,))
            cont = cur.fetchone()[0]

            # Caso nao tenha encontrado
            if (cont == 0):
                print("Não existe cliente com este nome.")
                b=1
                z = '0'
                z = input("Prima 0 para sair ou 1 para tentar novamente: ")
                if z == '0':
                    return

            #Caso tenha encontrado
            else:

                #Caso tenha mais que um
                if (cont != 1):

                    # Imprime no ecra os nomes encontrados e pede o id do cliente e o saldo
                    cur.execute("SELECT id, nome, saldo FROM cliente WHERE nome LIKE %s ORDER BY id;", (nome,))
                    for linha in cur.fetchall():
                        print("ID:", linha[0], " | Nome:", linha[1], " | Saldo: ", linha[2])

                    # Verifica se digitou o id certo
                    i = eval(input("Insira o ID: "))
                    cur.execute("SELECT count(*) FROM cliente WHERE id = %s and nome = %s;", (i, nome))
                    f = cur.fetchone()[0]
                    while (f == 0):
                        z = '0'
                        z = input("Prima 0 para sair ou 1 para tentar novamente: ")
                        if z == '0':
                            return
                        i = eval(input("Insira o ID: "))
                        cur.execute("SELECT count(*) FROM cliente WHERE id = %s and nome = %s;", (i, nome))
                        f = cur.fetchone()[0]
                        b=0

                # Existe só um
                else:
                    cur.execute("SELECT id FROM cliente WHERE nome = %s;", (nome,))
                    i = cur.fetchone()[0]
                    b=0

        #Valor do saldo que quer adicionar
        s = 0
        while(s == 0):
            saldo = input("Insira o saldo: ")
            if(saldo >= '' and saldo <= '/' or saldo >= ':' or saldo == None ):
                s = 0
            else:
                s = eval(saldo)

        #Ve quanto saldo o cliente ja tinha e adiciona o novo saldo
        cur.execute("SELECT saldo FROM cliente WHERE id = %s;", (i,))
        saldo_anterior = cur.fetchone()[0]
        s_atual = s + saldo_anterior

        #Faz o update na tabela
        cur.execute("UPDATE cliente SET saldo = %s WHERE id = %s;", (s_atual, i))
        conn.commit()

        a = input("Insira 0 para voltar: ")