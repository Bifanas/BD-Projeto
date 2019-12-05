def imprime(linha):
    print(' - '.join(map(str, linha)))

def por_album(cur, id):
    a='1'
    while a != '0':
        print("Albuns Comprados:")

        cur.execute("SELECT album.nome FROM album, historico_c_album, historico_c,cliente WHERE historico_c.id = historico_c_album.historico_c_id and historico_c_album.album_id = album.id and cliente.id = %s ORDER BY album.nome ASC;",(id,))
        for linha in cur.fetchall():
            imprime(linha)
        a = input("\nInsere 0 para voltar: ")

#-------------------------------------------------------------------------------------------------------------

def por_musica(cur,id):
    a='1'
    while a != '0':
        print("Musicas Compradas:")
        print("MUSICAS - ARTISTAS")

        cur.execute("SELECT distinct musica.musica, artista.artista FROM artista, artista_album, musica, musica_album, album, historico_c_album, historico_c,cliente WHERE historico_c.id = historico_c_album.historico_c_id and historico_c_album.album_id = album.id and album.id = musica_album.album_id and musica_album.musica_id = musica.id and album.id = artista_album.album_id and artista_album.artista_id = artista.id and cliente.id = %s ORDER BY musica.musica ASC;",(id,))
        for linha in cur.fetchall():
            imprime(linha)
        a = input("\nInsere 0 para voltar: ")
#-------------------------------------------------------------------------------------------------------------

def por_grupo(cur,id):
    a='1'
    while a != '0':
        print("Artistas Comprados:")

        cur.execute("SELECT distinct artista.artista FROM artista, artista_album, album, historico_c_album, historico_c,cliente WHERE historico_c.id = historico_c_album.historico_c_id and historico_c_album.album_id = album.id and album.id = artista_album.album_id and artista_album.artista_id = artista.id and cliente.id = %s ORDER BY artista.artista ASC;",(id,))
        for linha in cur.fetchall():
            imprime(linha)
        a = input("\nInsere 0 para voltar: ")

#-------------------------------------------------------------------------------------------------------------

def por_genero(cur,id):
    a='1'
    while a != '0':
        print("Generos Comprados:")

        cur.execute("SELECT distinct artista.artista FROM artista, artista_album, album, historico_c_album, historico_c,cliente WHERE historico_c.id = historico_c_album.historico_c_id and historico_c_album.album_id = album.id and album.id = artista_album.album_id and artista_album.artista_id = artista.id and cliente.id = %s ORDER BY artista.artista ASC;",(id,))
        for linha in cur.fetchall():
            imprime(linha)
        a = input("\nInsere 0 para voltar: ")