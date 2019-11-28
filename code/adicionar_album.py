import add_MGA
import datetime
# ADICIONAR ALBUM À BASE DE DADOS
# Verifica se o nome e o tempo nao sao nulos
# É Pedido a data de lancamento, stock atual e o preco do album


def func(conn, cur):
    a= '1'
    while a!= '0':

        nome = input("Digite o nome do novo album: ")
        duracao = input("Duracao do Album: ")
        ano = eval(input("Ano: "))
        Stock = eval(input("Quantidade em stock: "))
        Preco = eval(input("Preco: "))

        cur.execute("INSERT INTO album (nome, duracao, ano, stock, preco) values (%s,%s,%s,%s,%s)", (nome, duracao, ano, Stock, Preco))
        conn.commit()

        add_MGA.adicionar_musica(conn, cur, )
        add_MGA.adicionar_artista(conn, cur)
        add_MGA.adicionar_genero(conn, cur)

        a = input("Insere 0 para voltar: ")
        print("----------------------------------------------------------------------------------")