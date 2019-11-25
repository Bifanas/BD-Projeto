import psycopg2
import funcaoData
import add_MGA

conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
cur = conn.cursor()

# ADICIONAR ALBUM À BASE DE DADOS
# Verifica se o nome e o tempo nao sao nulos
# É Pedido a data de lancamento, stock atual e o preco do album


def func():
    a=1
    while a:

        nome = input("Digite o nome do novo album: ")
        Tempo = input("Duracao do Album: ")

        print("Data de Lançamento:")
        data = funcaoData.data()
        Stock = eval(input("Quantidade em stock: "))
        Preco = eval(input("Preco: "))

        cur.execute("INSERT INTO album values (6,%s,%s,%s,%s,%s)", (nome, Tempo, data, Stock, Preco))
        cur.execute("INSERT INTO historico_a values (%s,%s,6)", (Preco, Stock))
        conn.commit()

        add_MGA.adicionar_musica()
        add_MGA.adicionar_genero()
        add_MGA.adicionar_artista()

