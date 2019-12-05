# A funcao imprime serve para dar um espaco entre cada informacao sobre o album
# A funcao fucn mostra todos os albuns disponiveis em stock

def imprime(linha):
    print('   '.join(map(str, linha)))

def func(cur):
    a = '1'
    cur.execute("SELECT * FROM album WHERE stock > 0 ORDER BY ID;")
    print ("ID-NOME-DURACAO-DATA-STOCK-PRECO")
    for linha in cur.fetchall():
        imprime(linha)
    while a != '0':
        a =input("Insere 0 para voltar: ")
