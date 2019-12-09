import add_musica
import add_genero
import add_artista

# ADICIONAR ALBUM À BASE DE DADOS
def func(conn, cur):
    print('\nAdicionar album')
    a= '1'
    while a!= '0':
        # DADOS DO ALBUM PEDIDOS
        nome = input("Digite o nome do novo album: ")
        duracao = input("Duracao do Album: ")
        Stock = eval(input("Quantidade em stock: "))
        Preco = eval(input("Preco: "))
        ano = eval(input("Ano: "))

        # PROCURA O ULTIMO ID REGISTADO E ADICIONA O ALBUM NO PROXIMO ID
        cur.execute("SELECT MAX(id) FROM album")
        id_a = cur.fetchone()[0]
        id_a += 1
        cur.execute("INSERT INTO album values (%s,%s,%s,%s,%s,%s)", (id_a, nome, duracao, ano, Stock, Preco))
        conn.commit()

        # FUNCAO QUE PERMITE ADICIONAR MUSICA, ARTISTA E GENERO
        add_musica.adicionar_musica(conn, cur)
        add_genero.adicionar_genero(conn, cur)
        add_artista.adicionar_artista(conn, cur)