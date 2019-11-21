#menprincipal

#Menu1
import switch as switch

x = '0'
print('Prima a opcao que desejar:\n\n1 - Adicionar álbum\n2-  Visualiza álbuns\n3 - Corrigir preço\n4 - Remover álbum\n5 - Notificar\n6 - Estatísticas\n7 -Alterar saldo\n8 - Logout')

while x!='8':
    x = input('\n')
    if x == '0':
        print("imprime 0",x)
    elif x == '1':
        print("imprime 1",x)
    elif x == 2:
        print("imprime 2",x)
    else:
        print("imprime outra coisa", 'x')
