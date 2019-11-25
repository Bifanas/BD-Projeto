import psycopg2
import funcaoData
import add_MGA

conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
cur = conn.cursor()

# ADICIONAR ALBUM À BASE DE DADOS
# Verifica se o nome e o tempo nao sao nulos
# É Pedido a data de lancamento, stock atual e o preco do album


def adicionar_album():
    a=1
    while a:

        while a:
            nome = input("Digite o nome do novo album: ")
            if (len(nome) != None):
                a = 0

        while a:
            Tempo = input("Duracao do Album: ")
            if (len(Tempo) != None):
                a = 0

        print("Data de Lançamento:")
        data = funcaoData.data()

        Stock = eval(input("Quantidade em stock: "))

        Preco = eval(input("Preco: "))

        cur.execute("INSERT INTO album values (%s,%s,%s,%s,%s,%s)", (nome, Tempo, data, Stock, Preco))
        cur.execute("INSERT INTO historico_a values (%s,%s,%s)", (Preco, Stock, albumID))
        conn.commit()

