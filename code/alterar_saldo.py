# É pedido o username do cliente e verifica se este está na base de dados.
# Se nao estiver é mostrado uma mensagem de erro.
# Se existir este username é solicitado o novo valo do saldo do cliente, somado ao saldo do anterior e atualizado.
def imprime(linha):
    print('       '.join(map(str, linha)))

def func(conn, cur):
    a = '1'
    while a != '0':

        #Procura o nome do cliente na base de dados
        nome = input("Insira o nome do cliente: ")
        cur.execute("SELECT count(nome) FROM cliente WHERE nome = %s;", (nome,))
        cont = cur.fetchone()[0]

        #Caso nao tenha encontrado
        if(cont == 0):
            print("Não existe cliente com este username.")

        #Caso tenha encontrado
        else:
            #Imprime no ecra os nomes encontrados e pede o id do cliente e o saldo
            cur.execute("SELECT id, nome, saldo FROM cliente WHERE nome = %s ORDER BY id;", (nome,))
            for linha in cur.fetchall():
                imprime(linha)
            n = eval(input("Digite o ID: "))
            saldo = eval(input("Insira o saldo: "))

            #Ve quanto saldo o cliente ja tinha e adiciona o novo saldo
            cur.execute("SELECT saldo FROM cliente WHERE id = %s;", (n,))
            saldo_anterior = cur.fetchone()[0]
            s_atual = saldo + saldo_anterior

            #Faz o update na tabela
            cur.execute("UPDATE cliente SET saldo = %s WHERE id = %s;", (s_atual, n))
            conn.commit()

        a = input("Insere 0 para voltar: ")