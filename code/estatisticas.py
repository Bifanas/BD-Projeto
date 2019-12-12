def func(cur):
    print("\n")
    print("ESTATÍSTICAS")

    # TOTAL CLIENTES
    cur.execute("SELECT count(*) FROM cliente;")
    a = cur.fetchone()[0]
    print("\nTotal de Clientes: ", a)

    # TOTAL DE DISCOS
    cur.execute("SELECT count(id) FROM album;")
    b = cur.fetchone()[0]
    print("\nTotal de Discos: ", b)

    # VALOR TOTAL DOS DISCOS EM STOCK
    cur.execute("SELECT SUM(preco) FROM album WHERE  stock > 0;")
    c = cur.fetchone()[0]
    if (c is None):
        c = 0
    print("\nValor Total de Discos em Stock: ", c)

    # VALOR TOTAL DAS VENDAS
    cur.execute("SELECT SUM (preco) FROM historico_c_album, album WHERE album.id = historico_c_album.album_id;")
    d = cur.fetchone()[0]
    if (d is None):
        d = 0
    print("\nValor Total das Vendas: ", d)


    # TOTAL DE DISCOS POR GENERO MUSICAL

    #procedimento q foi pedido
    cur.execute("SELECT quantidade_generos();")
    f = cur.fetchone()[0]
    print("\nTotal de Gêneros: ", f)

    cur.execute("SELECT genero_id, tipo_genero ,stock from genero, album, album_genero where genero.id = album_genero.genero_id and album_genero.album_id = album.id order by genero_id asc")
    print("\nTotal de Discos Por Gênero Musical: ")
    stock = [0] * f  # inicializa um array vazio com a quantidade de generos
    genero = ['vazio'] * f  # inicialisa um array vasio com a quantidade de nomes
    for linha in cur.fetchall():
        y = linha[0] - 1  # genero id
        w = linha[2]  # quantidade no stock
        z = stock[y]  # quantidade anterior
        stock[y] = z + w  # adiciona o valor de stock no designado genero
        genero[y] = linha[1]  # nome do genero
    for x in range(f):
        print(' . O gênero', genero[x], 'tem', stock[x], 'discos em stock')  # imprime os valores

    # ESTATISTICAS EXTRAS:

    # ALBUNS MAIS VENDIDOS E QUANTIDADE
    print("\nÁlbum Mais Vendido e Quantidade: ")
    cur.execute("SELECT nome, count(historico_c_album.album_id) FROM  historico_c_album, album WHERE album.id = historico_c_album.album_id GROUP BY nome ORDER BY count(nome) DESC;")
    linha = cur.fetchone()
    print(" . Nome:", linha[0], " | Quant:", linha[1])


    # ALBUNS QUE NAO TEM EM STOCK
    print("\nÁlbuns Indisponíveis : ")
    cur.execute("SELECT * FROM album WHERE stock = 0 ORDER BY ID;")
    for linha in cur.fetchall():
        print(" . ID:", linha[0], " | Nome:", linha[1], " | Stock: ", linha[4], " | Preço: ", linha[5])

    print('')
    # Enquanto o adm nao inserir 0 para voltar ao menu ficará vendo as estatisticas
    a = '1'
    while a != '0':
        a = input("Insira 0 para voltar: ")