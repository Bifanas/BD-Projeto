def imprime(linha):\
    print(' - '.join(map(str, linha)))

def por_album(cur):

    #imprime albuns por ordem ascendente
    cur.execute("SELECT id, nome FROM album ORDER BY nome ASC")
    for linha in cur.fetchall():
        imprime(linha)

    #Caso o cliente queira ver a descricao de algum album
    r = input("Deseja ver os detalhes de algum album?[s/n]")
    while (r == 's' or r == 'S'):

        #Album que seja mostrado as descricoes
        i = eval(input("Digite o id do album"))
        cur.execute("SELECT count(id) FROM album WHERE id = %s;", (i,))
        q = cur.fetchone()[0]

        #Caso nao encontre o album
        if (q == 0):
            print("Nao ha este album.")
            r = input("Deseja ver os detalhes de algum album?[s/n]")

        #Caso ache o album
        else:
            #Imprime as especificacoes do album
            cur.execute("SELECT id, nome, duracao, ano, stock, preco  FROM album WHERE id = %s;", (i,))
            for linha in cur.fetchall():
                imprime(linha)

            #imprime alteracoes de preco
            cur.execute("SELECT preco  FROM album WHERE id = %s;", (i,))
            for linha in cur.fetchall():
                imprime(linha)

        r = input("\nDeseja ver os detalhes de algum outro album?[s/n]")