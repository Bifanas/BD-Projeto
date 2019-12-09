import ordena_historico

def func(cur,id):
    x = '0'
    while x != '4':
        print('\n1 - Ordenar por Album\n2 - Ordenar por Musica\n3 - Ordenar por Genero Musical\n4 - Ordenar por Grupo\n5 - Pedidos Anteriores\n6 - Valor Gasto por Genero Musical\n7 - Retornar')
        x = input('\n')

        cur.execute("SELECT nome FROM cliente WHERE id = %s;", (id,))
        nome = cur.fetchone()[0]

        if x == '1':
            print('\nUsuario:', nome)
            ordena_historico.por_album(cur, id)


        elif x == '2':
            print('\nUsuario:', nome)
            ordena_historico.por_musica(cur, id)

        elif x == '3':
            print('\nUsuario:', nome)
            ordena_historico.por_genero(cur, id)

        elif x == '4':
            print('\nUsuario:', nome)
            ordena_historico.por_grupo(cur, id)

        elif x == '5':
            print('\nUsuario:', nome)
            ordena_historico.pedidos_anteriores(cur, id)

        elif x == '6':
            print('\nUsuario:', nome)
            ordena_historico.distincao(cur,id)

        elif x == '7':
            print('\nRetornar')

        else:
            print("\nOpcao nao valida")