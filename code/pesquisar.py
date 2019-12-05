import ordena_pesquisa
def imprime(linha):\
    print(' - '.join(map(str, linha)))

def func(conn,cur,id):
    x = '0'
    while x != '5':
        print("Ordenar por:")
        print('1 - Album\n2 - Musica\n3 - Genero Musical\n4 - Grupo\n5 - Retornar')
        # Mostra as opcoes
        x = input('\n')

        if x == '1':
            print('Ordenar por album')
            ordena_pesquisa.por_album(conn,cur,id)


        elif x == '2':
            print('Ordenar por musica')
            ordena_pesquisa.por_musica(conn,cur,id)

        elif x == '3':
            print('Ordenar por genero')
            ordena_pesquisa.por_genero(conn, cur, id)

        elif x == '4':
            print('Ordenar por grupo')
            ordena_pesquisa.por_grupo(conn,cur,id)

        elif x == '5':
            print('Retornar')

        else:
            print("\nOpcao nao valida")

