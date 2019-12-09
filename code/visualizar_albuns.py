
def func(cur):
    #Conta quantos albuns há registados
    cur.execute("SELECT count(*) FROM album WHERE stock > 0;")
    q = cur.fetchone()[0]

    if(q == 0):
        print("\n")
        print("Não há álbuns registados.")

    else:
        # Procura todos albuns disponiveis em stock e mostra no ecra
        print('\nÁlbuns em Stock:')
        cur.execute("SELECT * FROM album WHERE stock > 0 ORDER BY ID;")
        for linha in cur.fetchall():
            print("ID:", linha[0], " | Nome:", linha[1], " | Duração: ", linha[2], " | Data:", linha[3], " | Stock: ", linha[4], " | Preço: ", linha[5])

    a='1'
    while a != '0':
        a = input("Insere 0 para voltar: ")

    print("\n")