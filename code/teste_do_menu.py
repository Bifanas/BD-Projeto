import registo_cliente
import login

x = '0'
while (True):
    print('\n1 - Registar-se\n2 - Login')

    x = input('')

    if x == '1':  registo_cliente.func()

    elif x == '2':
        usuario = 2
        if (usuario == 1):
            x = '0'
            while (x != 5):
                print('1 - Carrinho\n2 - Pesquisar\n3 - Histórico de compras\n4 - Notificações\n5 - Logout')
                x = input('\n')

                if x == '1':  # Carrinho
                    print('Carrinho')
                elif x == '2':  # Pesquisa
                    print('Pesquisa')
                elif x == '3':  # Historico de compras
                    print('Historico de compras')
                elif x == '4':  # Notificacao
                    print('Notificacao')
                elif x == '5':  # Logout

                else:
                    print("Opcao nao valida")


        elif (usuario == 2):
            x = '0'
            while x != '8':

                print('Prima a opcao que desejar:\n\n1 - Adicionar álbum\n2-  Visualiza álbuns\n3 - Corrigir preço\n4 - Remover álbum\n5 - Notificar\n6 - Estatísticas\n7 - Alterar saldo\n8 - Logout')
                x = input('\n')

                if x == '1':  # Adiciona Album
                    print('Adiciona album')
                elif x == '2':  # Visualiza albuns
                    print('Visualiza albuns')
                elif x == '3':  # Corrigir preco
                    print('Corrigir preço')
                elif x == '4':  # Remover album
                    print('Remover album')
                elif x == '5':  # Notificar
                    print('Notificar')
                elif x == '6':  # Estatisticas
                    print('Estatisticas')
                elif x == '7':  # Alterar saldo
                    print('Alterar saldo')
                elif x == '8':  # logout
                    break
                else:
                    print("Opcao nao valida")


    else:
        print("Opcao nao valida")