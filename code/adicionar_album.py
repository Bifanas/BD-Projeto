import add_musica
import add_genero
import add_artista
import corrigir_stock

# ADICIONAR ALBUM À BASE DE DADOS
def func(conn, cur):
    x = '0'
    while x != '6':
        print('\n')
        print('ADICIONAR ÁLBUM')

        print('Prima a opção que desejar:\n1 - Novo álbum\n2-  Álbum existente\n3 - Adicionar música\n4 - Adicionar gênero\n5 - Adicionar artista\n6 - Voltar')
        x = input('')

        if x == '1':
            add_album(conn,cur)

        elif x == '2':
            corrigir_stock.func(conn, cur)

        elif x == '3':
            add_musica.adicionar_musica(conn, cur)

        elif x == '4':
            add_genero.adicionar_genero(conn, cur)

        elif x == '5':
            add_artista.adicionar_artista(conn, cur)

        elif x == '6':
            print('\n')
            print("Voltar")

        else:
            print('\n')
            print("Opção não válida")


def add_album(conn,cur):
    # DADOS DO ALBUM PEDIDOS
    print("\n")
    print("NOVO ÁLBUM")
    nome = input("Digite o nome do novo álbum: ")
    duracao = input("Duração do Album: ")

    # Valor do stock que quer adicionar
    s = 0
    while (s == 0):
        stock = input("Quantidade em stock: ")
        if (stock >= '' and stock <= '/' or stock >= ':' or stock == None):
            s = 0
        else:
            s = eval(stock)

    # Valor do saldo que quer adicionar
    p = 0
    while (p == 0):
        preco= input("Preço: ")
        if (preco >= '' and preco <= '/' or preco >= ':' or preco == None):
            p = 0
        else:
            p = eval(preco)

    #Ano de lancamento do album
    a = 0
    while (a < 1000):
        ano = input('Ano: ')
        if (len(ano) != 4):
            a = 0
        else:
            a = eval(ano)

    # PROCURA O ULTIMO ID REGISTADO E ADICIONA O ALBUM NO PROXIMO ID
    cur.execute("SELECT MAX(id) FROM album")
    id_a = cur.fetchone()[0]

    # VERIFICA SE NAO TEM NENHUM ALBUM REGISTADO
    if (id_a is None):
        id_a = 0
    id_a += 1
    cur.execute("INSERT INTO album values (%s,%s,%s,%s,%s,%s)", (id_a, nome, duracao, a, s, p))
    conn.commit()




