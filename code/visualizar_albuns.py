# A funcao imprime serve para dar um espaco entre cada informacao sobre o album
# A funcao fucn mostra todos os albuns disponiveis em stock

def imprime(linha):
    print('   '.join(map(str, linha)))

def func(cur):
    print('\nVisualiza albuns:')
    a = '1'
    #Procura todos albuns disponiveis em stock e mostra no ecra
    cur.execute("SELECT * FROM album WHERE stock > 0 ORDER BY ID;")
    print ("ID  Nome Duração Data Stock Preço")
    for linha in cur.fetchall():
        imprime(linha)
    print(" ")

    #Espera pelo utilizador primir 0 para voltar ao menu
    while a != '0':
        a =input("Insere 0 para voltar: ")

    print("\n")