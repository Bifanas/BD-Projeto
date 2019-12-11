#Vai importar todas as funcoes dos arquivos
#Funcoes do menu
import registo_cliente
import login
#Funcoes ADM
import adicionar_album
import visualizar_albuns
import corrigir_preco
import remover_album
import notificacao
import estatisticas
import alterar_saldo
#Funcoes CLIENTE
import pedido
import pesquisar
import historico_compras
import notificacao_cliente

import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
cur = conn.cursor()

# Menu inicial
# inicia o programa que fica ativo ate que o usuario feche-o

x = '0'  # inicializa o valor de x
while (True):
    print('\n')
    print("MENU INICIAL")
    print('1 - Registar-se\n2 - Login')
    # mostra as opcoes
    x = input('')
    # Obtem a escolha do cliente

    if x == '1':  # Registar-se
        registo_cliente.func(conn, cur)

    elif x == '2':  # Login
        usuario = '0'
        usuario, id = '1',1 #login.func(cur)

        # A funcao login retorna o tipo de usuario1
        # Retornar 1 para cliente e 0 para adm
        # -------------------------------------------------------------------------------------

        if (usuario == '1'):
            # Menu principal Cliente

            cur.execute("SELECT nome FROM cliente WHERE id = %s;", (id,))
            nome = cur.fetchone()[0]

            # Identifica o nome do cliente

            x = '0'  # inicializa o valor de x
            while x != '5':
                print('\n')
                print('Usuário:', nome)
                print("MENU PRINCIPAL")
                print('1 - Carrinho\n2 - Pesquisar\n3 - Histórico de compras\n4 - Notificações\n5 - Logout')
                # Mostra as opcoes
                x = input('')
                # Obtem a escolha do cliente

                if x == '1':  # Carrinho
                    print('\nUsuario:', nome)
                    print('CARRINHO')
                    pedido.func(conn, cur, id)
                elif x == '2':  # Pesquisa
                    print('\nUsuario:', nome)
                    print('Pesquisa')
                    pesquisar.func(conn,cur, id)
                elif x == '3':  # Historico de compras
                    historico_compras.func(cur,id, nome)
                elif x == '4':  # Notificacao
                    notificacao_cliente.func(conn, cur, id, nome)
                elif x == '5':  # Logout
                    print('Logout')
                else:
                    print("\nOpção não válida.")

        # -------------------------------------------------------------------------------------
        elif (usuario == '0'):

            # Menu principla Admin

            x = '0'  # inicializa o valor de x
            while x != '8':
                print('\n')
                print("MENU PRINCIPAL")
                print('Prima a opção que desejar:\n1 - Adicionar álbum\n2-  Visualizar álbuns\n3 - Corrigir preço\n4 - Remover álbum\n5 - Notificar\n6 - Estatísticas\n7 - Alterar saldo\n8 - Logout')
                # Mostra as opcoes
                x = input('')
                # Obtem a escolha do cliente

                if x == '1':  # Adiciona Album
                    adicionar_album.func(conn, cur)

                elif x == '2':  # Visualiza albuns em stock
                    visualizar_albuns.func(cur)

                elif x == '3':  # Corrigir preco
                    corrigir_preco.func(conn, cur, id)

                elif x == '4':  # Remover album
                    remover_album.func(conn, cur)

                elif x == '5':  # Notificar
                    notificacao.func(conn, cur, id)

                elif x == '6':  # Estatisticas
                    estatisticas.func(cur)

                elif x == '7':  # Alterar saldo
                    alterar_saldo.func(conn, cur)

                elif x == '8':  # logout
                    print('\n')
                    print("Logout")

                else:
                    print('\n')
                    print("Opção não válida")

        # -------------------------------------------------------------------------------------
    else:
        print("Opção não válida")
