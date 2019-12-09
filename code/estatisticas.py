def imprime(linha):
    print('    '.join(map(str, linha)))

def func(cur):
    print('\nEstatisticas')
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
        if(d is None):
            d=0
        print("VALOR TOTAL DAS VENDAS: ", d)

        cur.execute("SELECT nome, count(historico_c_album.album_id) FROM  historico_c_album, album WHERE album.id = historico_c_album.album_id GROUP BY nome ORDER BY count(nome) DESC;")
        print("ALBUM MAIS VENDIDO E QUANTIDADE: ", cur.fetchall()[0])

        #Duas estatisticas extra

        cur.execute("SELECT count(id) FROM artista;")
        e = cur.fetchone()[0]
        print("TOTAL DE ARTISTAS: ", e)

        cur.execute("SELECT count(genero.id) FROM genero;")
        f = cur.fetchone()[0]
        print("TOTAL DE GENEROS: ", f)

        cur.execute("SELECT genero_id, tipo_genero ,stock from genero, album, album_genero where genero.id = album_genero.genero_id and album_genero.album_id = album.id order by genero_id asc")
        print("TOTAL DE DISCOS POR GENERO MUSICAL: ")
        stock = [0]*f #inicializa um array vazio com a quantidade de generos
        genero = ['vazio']*f #inicialisa um array vasio com a quantidade de nomes
        for linha in cur.fetchall():
            y = linha[0]-1 #genero id
            w = linha[2]   #quantidade no stock
            z = stock[y]   # quantidade anterior
            stock[y]= z + w # adiciona o valor de stock no designado genero
            genero[y]= linha [1] # nome do genero
        for x in range(f):
            print('O genero', genero[x], 'tem', stock[x], 'discos em stock') # imprime os valores

        a = input("\nInsere 0 para voltar: ")