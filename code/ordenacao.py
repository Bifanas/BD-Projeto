import operacoes_carrinho

def imprime(linha):
    print(' - '.join(map(str, linha)))

def por_album(conn,cur, id):

    #imprime albuns por ordem ascendente
    cur.execute("SELECT id, nome FROM album ORDER BY nome ASC")
    for linha in cur.fetchall():
        imprime(linha)

    #Caso o cliente queira ver a descricao de algum album
    r = input("Deseja ver os detalhes de algum album?[s/n]")
    while (r == 's' or r == 'S'):

        #Album que seja mostrado as descricoes
        i = eval(input("Digite o id do album: "))
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

            print("Preços anteriores: ")
            #imprime alteracoes de preco
            cur.execute("SELECT preco  FROM historico_a WHERE album_id = %s;", (i,))
            for linha in cur.fetchall():
                imprime(linha)

            cur.execute("SELECT preco FROM album WHERE id = %s;", (i,))
            print("Preço atual:")
            print(cur.fetchone()[0])

        r = input("\nDeseja ver os detalhes de algum outro album?[s/n]")

    j = input("\nDeseja adicionar algum album no carrinho?[s/n]")
    while (j == 's' or j == 'S'):
        operacoes_carrinho.add(conn, cur, id)
        j = input("\nDeseja adicionar algum album no carrinho?[s/n]")

#-------------------------------------------------------------------------------------------------------------

def por_musica(conn,cur,id):
    #imprime musica por ordem ascendente
    cur.execute("SELECT album.id, musica, album.nome FROM musica, album, musica_album WHERE musica.id=musica_album.musica_id and musica_album.album_id = album.id ORDER BY musica.id ASC")
    for linha in cur.fetchall():
        imprime(linha)

    j = input("\nDeseja adicionar algum album no carrinho?[s/n]")
    if(j =='s' or j =='S'):
        operacoes_carrinho.add(conn,cur,id)

#-------------------------------------------------------------------------------------------------------------

def por_grupo(conn,cur,id):
    #imprime artista por ordem ascendente
    cur.execute("SELECT album.id, artista, album.nome FROM artista, album, artista_album WHERE artista.id=artista_album.artista_id and artista_album.album_id = album.id ORDER BY artista.id ASC")
    for linha in cur.fetchall():
        imprime(linha)

    j = input("\nDeseja adicionar algum album no carrinho?[s/n]")
    if(j =='s' or j =='S'):
        operacoes_carrinho.add(conn,cur,id)

#-------------------------------------------------------------------------------------------------------------

def por_genero(conn,cur,id):
    #imprime genero por ordem ascendente
    cur.execute("SELECT album.id, tipo_genero, album.nome FROM genero, album, album_genero WHERE genero.id=album_genero.genero_id and album_genero.album_id = album.id ORDER BY genero.id ASC")
    for linha in cur.fetchall():
        imprime(linha)

    j = input("\nDeseja adicionar algum album no carrinho?[s/n]")
    if(j =='s' or j =='S'):
        operacoes_carrinho.add(conn,cur,id)

