#import funcoes
#vai importar todas as funcoes do arquivo funcoes.py

#Menu inicial
#inicia o programa que fica ativo ate que o usuario feche-o

x = '0' #inicializa o valor de x

while (True):
    print('1 - Registar-se\n2 - Login')
    #mostra as opcoes
    x = input('\n')
    # Obtem a escolha do cliente

    if x == '1': #Registar-se
        print('funcoes.Registar()')
    elif x == '2': #Login
        print('funcoes.login()')
        usuario = funcoes.login()
        #A funcao login retorna o tipo de usuario

        usuario = tipo_de_usuario

        #-------------------------------------------------------------------------------------
 
        if (usuario == cliente)

                #Menu principal Cliente

                x = '0' #inicializa o valor de x
                while x!='5':

                    print('1 - Carrinho\n2 - Pesquisar\n3 - Histórico de compras\n4 - Notificações\n5 - Logout')
                    #Mostra as opcoes
                    x = input('\n')
                    #Obtem a escolha do cliente

                    if x == '1': #Carrinho
                        print('Carrinho')
                    elif x == '2': #Pesquisa
                        print('Pesquisa')
                    elif x == '3': #Historico de compras
                        print('Historico de compras')
                    elif x == '4': #Notificacao
                        print('Notificacao')
                    elif x == '5': #Logout
                        print('Logout')
                    else:
                        print("Opcao nao valida")

        #-------------------------------------------------------------------------------------
        elif(usuario == administrador)

                #Menu principla Admin

                x = '0' #inicializa o valor de x
                while x!='8':

                    print('Prima a opcao que desejar:\n\n1 - Adicionar álbum\n2-  Visualiza álbuns\n3 - Corrigir preço\n4 - Remover álbum\n5 - Notificar\n6 - Estatísticas\n7 - Alterar saldo\n8 - Logout')
                    #Mostra as opcoes
                    x = input('\n')
                    # Obtem a escolha do cliente

                    if x == '1': #Adiciona Album
                        print('Adiciona album')
                    elif x == '2': #Visualiza albuns
                        print('Visualiza albuns')
                    elif x == '3': #Corrigir preco
                        print('Corrigir preço')
                    elif x == '4': #Remover album
                        print('Remover album')
                    elif x == '5': #Notificar
                        print('Notificar')
                    elif x == '6': #Estatisticas
                        print('Estatisticas')
                    elif x == '7': #Alterar saldo
                        print('Alterar saldo')
                    elif x == '8': #logout
                        print("Logout")
                    else:
                        print("Opcao nao valida")

        #-------------------------------------------------------------------------------------
    else:
        print("Opcao nao valida")