import ordena_historico

def func(conn, cur,id):
    x = '0'
    while x != '4':
        print('1 - Ordenar por Album\n2 - Ordenar por Musica\n3 - Ordenar por Genero Musical\n4 - Ordenar por Grupo\n5 - Retornar')
        # Mostra as opcoes
        x = input('\n')

        if x == '1':
            print('Ordenar por album')
            ordena_historico.por_album(conn, cur, id)


        elif x == '2':
            print('Ordenar por musica')
            ordena_historico.por_musica(conn, cur, id)

        elif x == '3':
            print('Ordenar por genero')
            ordena_historico.por_genero(conn, cur, id)

        elif x == '4':
            print('Ordenar por grupo')
            ordena_historico.por_grupo(conn, cur, id)

        elif x == '5':
            print('Retornar')

        else:
            print("\nOpcao nao valida")