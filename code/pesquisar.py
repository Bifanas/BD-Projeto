import ordena_pesquisa

def func(conn,cur,id, nome):
    x = '0'
    while x != '5':
        print("\n")
        print('Usuario:', nome)
        print("ORDENAR POR:")
        print('1 - Album\n2 - Musica\n3 - Genero Musical\n4 - Grupo\n5 - Retornar')
        # Mostra as opcoes
        x = input('')

        if x == '1':
            ordena_pesquisa.por_album(conn,cur,id, nome)

        elif x == '2':
            ordena_pesquisa.por_musica(conn,cur,id, nome)

        elif x == '3':
            ordena_pesquisa.por_genero(conn, cur, id, nome)

        elif x == '4':
            ordena_pesquisa.por_grupo(conn,cur,id, nome)

        elif x == '5':
            print('\n')
            print("Voltar")

        else:
            print('\n')
            print("Opção não válida")

