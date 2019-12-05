def imprime(linha):
    print('    '.join(map(str, linha)))

def func(cur):
    a = '1'
    while a != '0':
        cur.execute("SELECT count(*) FROM cliente;")
        a = cur.fetchone()[0]
        print("\nTOTAL DE CLIENTES: ", a)

        cur.execute("SELECT count(id) FROM album;")
        b = cur.fetchone()[0]
        print("TOTAL DE DISCOS: ", b)

        cur.execute("SELECT SUM(preco) FROM album WHERE  stock > 0;")
        c = cur.fetchone()[0]
        print("VALOR TOTAL DOS DISCOS EM STOCK: ", c)

        cur.execute("SELECT SUM (preco) FROM historico_c_album, album WHERE album.id = historico_c_album.album_id;")
        d = cur.fetchone()[0]
        print("VALOR TOTAL DAS VENDAS: ", d)

        cur.execute("SELECT count(id) FROM artista;")
        e = cur.fetchone()[0]
        print("TOTAL DE ARTISTAS: ", e)

        #AJUDA top 5, quantidade
        cur.execute("SELECT nome FROM  historico_c_album, album WHERE album.id = historico_c_album.album_id GROUP BY nome ORDER BY count(nome) DESC;")
        print("ALBUNS MAIS VENDIDOS: ")
        for linha in cur.fetchall():
            imprime(linha)

        #AJUDA
        cur.execute("SELECT distinct tipo_genero, stock from genero, album, album_genero where genero.id = album_genero.genero_id and album_genero.album_id = album.id;")
        print("TOTAL DE DISCOS POR GENERO MUSICAL: ")
        for linha in cur.fetchall():
            imprime(linha)



        a = input("\nInsere 0 para voltar: ")