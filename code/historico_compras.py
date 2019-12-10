import ordena_historico

def func(cur,id, nome):
    x = '0'
    while x != '7':
        print('\n')
        print('Usuário:', nome)
        print("HISTÓRICO DE COMPRAS")
        print('1 - Ordenar por Álbum\n2 - Ordenar por Música\n3 - Ordenar por Gênero Musical\n4 - Ordenar por Grupo\n5 - Pedidos Anteriores\n6 - Valor Gasto por Gênero Musical\n7 - Voltar')
        x = input('')


        if x == '1':
            ordena_historico.por_album(cur, id,nome)

        elif x == '2':
            ordena_historico.por_musica(cur, id,nome)

        elif x == '3':
            ordena_historico.por_genero(cur, id,nome)

        elif x == '4':
            ordena_historico.por_grupo(cur, id,nome)

        elif x == '5':
            ordena_historico.pedidos_anteriores(cur, id,nome)


        elif x == '6':
            ordena_hostorico.valorGenero(cur,id,nome)

        elif x == '7':
            print('\n')
            print("Voltar")

        else:
            print('\n')
            print("Opção não válida")