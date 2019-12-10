def imprime(linha):
    print('       '.join(map(str, linha)))

def por_album(cur, id):
    # Imprime no ecra os albuns comprados e aguarda o utilizador digitar 0
    a='1'
    print("Álbuns Comprados:")
    cur.execute("SELECT album.nome FROM album, historico_c_album, historico_c,cliente WHERE historico_c.id = historico_c_album.historico_c_id and historico_c_album.album_id = album.id and cliente.id = %s ORDER BY album.nome ASC;",(id,))
    for linha in cur.fetchall():
        imprime(linha)
    while a != '0':
        a = input("Insere 0 para voltar: ")

#-------------------------------------------------------------------------------------------------------------

def por_musica(cur,id):
    # Imprime no ecra as músicas dos albuns comprados e aguarda o utilizador digitar 0
    a='1'
    print("Musicas Compradas:")
    cur.execute("SELECT distinct musica.musica, album.nome FROM musica, musica_album, album, historico_c_album, historico_c,cliente WHERE historico_c.id = historico_c_album.historico_c_id and historico_c_album.album_id = album.id and album.id = musica_album.album_id and musica_album.musica_id = musica.id and cliente.id = %s ORDER BY musica.musica ASC;",(id,))
    for linha in cur.fetchall():
        imprime(linha)
    while a != '0':
        a = input("Insere 0 para voltar: ")
#-------------------------------------------------------------------------------------------------------------

def por_grupo(cur,id):
    # Imprime no ecra os artistas dos albuns comprados e aguarda o utilizador digitar 0
    a='1'
    print("Artistas Comprados:")
    cur.execute("SELECT distinct artista.artista FROM artista, artista_album, album, historico_c_album, historico_c,cliente WHERE historico_c.id = historico_c_album.historico_c_id and historico_c_album.album_id = album.id and album.id = artista_album.album_id and artista_album.artista_id = artista.id and cliente.id = %s ORDER BY artista.artista ASC;",(id,))
    for linha in cur.fetchall():
        imprime(linha)
    while a != '0':
        a = input("\nInsere 0 para voltar: ")

#-------------------------------------------------------------------------------------------------------------

def por_genero(cur,id):
    # Imprime no ecra os generos dos albuns comprados e aguarda o utilizador digitar 0
    a='1'
    print("Generos Comprados:")
    cur.execute("SELECT distinct artista.artista FROM artista, artista_album, album, historico_c_album, historico_c,cliente WHERE historico_c.id = historico_c_album.historico_c_id and historico_c_album.album_id = album.id and album.id = artista_album.album_id and artista_album.artista_id = artista.id and cliente.id = %s ORDER BY artista.artista ASC;",(id,))
    for linha in cur.fetchall():
        imprime(linha)
    while a != '0':
        a = input("\nInsere 0 para voltar: ")

#-------------------------------------------------------------------------------------------------------------

def pedidos_anteriores(cur,id):
    a='1'
    while a != '0':
        print("Pedidos Anteriores:")

        cur.execute("SELECT count(historico_c.id) FROM cliente, historico_c WHERE cliente.id = historico_c.cliente_id and cliente.id = %s;",(id,))
        a = cur.fetchone()[0]
        b=1
        while b <= q:
            cur.execute("SELECT album.nome FROM cliente, historico_c_album, album WHERE cliente.id = %s and historico_c_album.historico_c_id = %s and historico_c_album.album_id = album.id order by nome ASC;", (id, b))
            g = cur.fetchone()[0]
            if(g is None):
                b+=1

            cur.execute("SELECT data_de_compra FROM cliente, historico_c WHERE cliente.id = historico_c.cliente_id and cliente.id = %s and historico_c.id=%s;",(id,b))
            data = cur.fetchone()[0]

            print("\nNumero do pedido: ", b, "   Data de Compra: ", data)
            cur.execute("SELECT album.nome, preco FROM cliente, historico_c_album, album WHERE cliente.id = %s and historico_c_album.historico_c_id = %s and historico_c_album.album_id = album.id order by nome ASC;",(id,b))
            print("Album     Preço")
            for linha in cur.fetchall():
                imprime(linha)

            cur.execute("SELECT SUM(preco) FROM cliente, historico_c_album, album WHERE cliente.id = %s and historico_c_album.historico_c_id = %s and historico_c_album.album_id = album.id;",(id, b))
            total = cur.fetchone()[0]
            print("Total do pedido: ", total)
            b+=1

        a = input("\nInsere 0 para voltar: ")

#-------------------------------------------------------------------------------------------------------------
def valorGenero(cur,id,nome):
    a=0