import ordenacao
def imprime(linha):\
    print(' - '.join(map(str, linha)))

def func(conn,cur,id):
    x = '0'
    while x != '4':
        print("Ordenar por:")
        print('1 - Album\n2 - Musica\n3 - Genero Musical\n4 - Retornar')
        # Mostra as opcoes
        x = input('\n')

        if x == '1':
            print('Ordenar por album')
            ordenacao.por_album(cur)



        elif x == '2':
            print('Ordenar por musica')

        elif x == '3':
            print('Ordenar por genero')

        elif x == '4':
            print('Retornar')

        else:
            print("\nOpcao nao valida")


    print("ALBUNS:")

