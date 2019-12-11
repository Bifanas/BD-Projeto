def por_album(cur, id,nome):
    # Imprime no ecra os albuns comprados e aguarda o utilizador digitar 0
    print("\n")
    print('Usuario:', nome)
    print("ÁLBUNS COMRADOS")
    cur.execute("SELECT album.nome, preco, data_de_compra FROM album, historico_c_album, historico_c,cliente WHERE historico_c.id = historico_c_album.historico_c_id and historico_c_album.album_id = album.id and cliente.id = %s ORDER BY data_de_compra ASC;",(id,))
    for linha in cur.fetchall():
        print("Nome do Álbum:", linha[0], " | Preço:", linha[1], " | Data de Compra:", linha[2])

    a = '1'
    while a != '0':
        a = input("Insira 0 para voltar: ")

#-------------------------------------------------------------------------------------------------------------

def por_musica(cur,id,nome):
    # Imprime no ecra as músicas dos albuns comprados e aguarda o utilizador digitar 0
    print("\n")
    print('Usuario:', nome)
    print("MÚSICAS COMPRADAS")
    cur.execute("SELECT distinct musica.musica, album.nome, data_de_compra FROM musica, musica_album, album, historico_c_album, historico_c,cliente WHERE historico_c.id = historico_c_album.historico_c_id and historico_c_album.album_id = album.id and album.id = musica_album.album_id and musica_album.musica_id = musica.id and cliente.id = %s ORDER BY data_de_compra ASC;",(id,))
    for linha in cur.fetchall():
        print("Nome da Música:", linha[0], " | Álbum:", linha[1], " | Data de Compra:", linha[2])

    a='1'
    while a != '0':
        a = input("Insira 0 para voltar: ")
#-------------------------------------------------------------------------------------------------------------

def por_grupo(cur,id,nome):
    # Imprime no ecra os artistas dos albuns comprados e aguarda o utilizador digitar 0
    print("\n")
    print('Usuario:', nome)
    print("ARTISTAS COMPRADOS")
    cur.execute("SELECT artista.artista, album.nome, data_de_compra FROM artista, artista_album, album, historico_c_album, historico_c,cliente WHERE historico_c.id = historico_c_album.historico_c_id and historico_c_album.album_id = album.id and album.id = artista_album.album_id and artista_album.artista_id = artista.id and cliente.id = %s ORDER BY data_de_compra ASC;",(id,))
    for linha in cur.fetchall():
        print("Nome do Artista:", linha[0], " | Álbum:", linha[1], " | Data de Compra:", linha[2])

    a = '1'
    while a != '0':
        a = input("Insira 0 para voltar: ")

#-------------------------------------------------------------------------------------------------------------

def por_genero(cur,id, nome):
    # Imprime no ecra os generos dos albuns comprados e aguarda o utilizador digitar 0
    print("\n")
    print('Usuario:', nome)
    print("GENEROS COMPRADOS")
    cur.execute("SELECT tipo_genero, album.nome, data_de_compra from genero, album, album_genero, historico_c_album, historico_c, cliente where cliente.id = %s and cliente.id = historico_c.cliente_id and historico_c.id = historico_c_album.historico_c_id and historico_c_album.album_id = album.id and album.id = album_genero.album_id and album_genero.genero_id = genero.id group by tipo_genero, album.nome, data_de_compra ORDER BY data_de_compra asc;",(id,))
    for linha in cur.fetchall():
        print("Nome do Gênero:", linha[0], " | Álbum:", linha[1], " | Data de Compra:", linha[2])
    a = '1'
    while a != '0':
        a = input("Insira 0 para voltar: ")

#-------------------------------------------------------------------------------------------------------------

def pedidos_anteriores(cur,id,nome):
    print("\n")
    print('Usuario:', nome)
    print("PEDIDOS ANTERIORES")

    cur.execute("SELECT count(historico_c.id) FROM cliente, historico_c WHERE cliente.id = historico_c.cliente_id and cliente.id = %s;",(id,))
    q = cur.fetchone()[0]
    b = 1

    while b <= q:

        cur.execute("SELECT album.nome FROM cliente, historico_c_album, album WHERE cliente.id = %s and historico_c_album.historico_c_id = %s and historico_c_album.album_id = album.id order by nome ASC;",(id, b))
        g = cur.fetchone()[0]
        if (g is None):
            b += 1

        cur.execute("SELECT data_de_compra FROM cliente, historico_c WHERE cliente.id = historico_c.cliente_id and cliente.id = %s and historico_c.id=%s;",(id, b))
        data = cur.fetchone()[0]

        print("\nNumero do pedido: ", b, "   Data de Compra: ", data)
        cur.execute("SELECT album.nome, preco FROM cliente, historico_c_album, album WHERE cliente.id = %s and historico_c_album.historico_c_id = %s and historico_c_album.album_id = album.id order by nome ASC;",(id, b))
        for linha in cur.fetchall():
            print("Álbum:", linha[0], "    Preço:", linha[1])

        cur.execute("SELECT SUM(preco) FROM cliente, historico_c_album, album WHERE cliente.id = %s and historico_c_album.historico_c_id = %s and historico_c_album.album_id = album.id;",(id, b))
        total = cur.fetchone()[0]
        print("TOTAL DO PEDIDO: ", total)
        b += 1

    a = '1'
    while a != '0':
        a = input("Insira 0 para voltar: ")

#-------------------------------------------------------------------------------------------------------------
def valorGenero(cur,id,nome):
    print("\n")
    print('Usuario:', nome)
    print("VALOR GASTO POR GENERO MUSICAL ")
    cur.execute("SELECT (count(genero_id) * preco), tipo_genero from genero, album, album_genero, historico_c_album, historico_c, cliente where cliente.id = %s and cliente.id = historico_c.cliente_id and historico_c.id = historico_c_album.historico_c_id and historico_c_album.album_id = album.id and album.id = album_genero.album_id and album_genero.genero_id = genero.id group by tipo_genero, preco;",(id,))
    for linha in cur.fetchall():
        print(linha[1], '-', linha[0])

    a='1'
    while a != '0':
        a = input("Insira 0 para voltar: ")