import registo_cliente
import login
import adicionar_album
import visualizar_albuns
import corrigir_preco
import remover_album
import estatisticas
import notificacao
import alterar_saldo
import pedido
import notificacao_cliente
import pesquisar
import historico_compras

import psycopg2

# vai importar todas as funcoes dos arquivos

conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
cur = conn.cursor()

# Menu inicial
# inicia o programa que fica ativo ate que o usuario feche-o

x = '0'  # inicializa o valor de x
while (True):
    print('1 - Registar-se\n2 - Login')
    # mostra as opcoes
    x = input('\n')
    # Obtem a escolha do cliente

    if x == '1':  # Registar-se
        registo_cliente.func(conn, cur)

    elif x == '2':  # Login
        usuario = '0'
        usuario, id = '1' \
                      '',1
        # A funcao login retorna o tipo de usuario
        # Retornar 1 para cliente e 0 para adm
        # -------------------------------------------------------------------------------------

        if (usuario == '1'):
            # Menu principal Cliente

            cur.execute("SELECT nome FROM cliente WHERE id = %s;", (id,))
            nome = cur.fetchone()[0]

            # Identifica o nome do cliente

            x = '0'  # inicializa o valor de x
            while x != '5':
                print('\nUsuario:', nome)
                print('1 - Carrinho\n2 - Pesquisar\n3 - Histórico de compras\n4 - Notificações\n5 - Logout')
                # Mostra as opcoes
                x = input('\n')
                # Obtem a escolha do cliente

                if x == '1':  # Carrinho
                    print('\nUsuario:', nome)
                    print('Carrinho')
                    pedido.func(conn, cur, id)
                elif x == '2':  # Pesquisa
                    print('\nUsuario:', nome)
                    print('Pesquisa')
                    pesquisar.func(conn,cur, id)
                elif x == '3':  # Historico de compras
                    print('\nUsuario:', nome)
                    print('Historico de compras')
                    historico_compras.func(conn,cur,id)
                elif x == '4':  # Notificacao
                    print('\nUsuario:', nome)
                    print('Notificacao')
                    notificacao_cliente.func(conn, cur, id)
                elif x == '5':  # Logout
                    print('Logout')
                else:
                    print("\nOpcao nao valida")

        # -------------------------------------------------------------------------------------
        elif (usuario == '0'):

            # Menu principla Admin

            x = '0'  # inicializa o valor de x
            while x != '8':
                print(
                    'Prima a opcao que desejar:\n\n1 - Adicionar álbum\n2-  Visualiza álbuns\n3 - Corrigir preço\n4 - Remover álbum\n5 - Notificar\n6 - Estatísticas\n7 - Alterar saldo\n8 - Logout')
                # Mostra as opcoes
                x = input('\n')
                # Obtem a escolha do cliente

                if x == '1':  # Adiciona Album
                    print('Adiciona album')
                    adicionar_album.func(conn, cur)

                elif x == '2':  # Visualiza albuns
                    print('Visualiza albuns')
                    visualizar_albuns.func(cur)

                elif x == '3':  # Corrigir preco
                    print('Corrigir preço')
                    corrigir_preco.func(conn, cur, id)

                elif x == '4':  # Remover album
                    print('Remover album')
                    remover_album.func(conn, cur)

                elif x == '5':  # Notificar
                    print('Notificar')
                    notificacao.func(conn, cur, id)

                elif x == '6':  # Estatisticas
                    print('Estatisticas')
                    estatisticas.func(cur)

                elif x == '7':  # Alterar saldo
                    print('Alterar saldo')
                    alterar_saldo.func(conn, cur)

                elif x == '8':  # logout
                    print("Logout")
                else:
                    print("Opcao nao valida")

        # -------------------------------------------------------------------------------------
    else:
        print("Opcao nao valida")