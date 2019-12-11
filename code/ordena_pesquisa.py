import operacoes_carrinho

def por_album(conn,cur, id, nome):
    print('\n')
    print('Usuario:', nome)
    print('ORDERNAR POR ÁLBUM')

    # imprime albuns por ordem ascendente
    cur.execute("SELECT id, nome FROM album ORDER BY nome ASC")
    for linha in cur.fetchall():
        print("ID:", linha[0], " | Nome:", linha[1])

    r = '0'
    while (r != '3'):

        #Caso o cliente queira ver a descricao de algum album
        print("\nDeseja ver os detalhes de algum album?")
        print("1 - SIM\n2 - NAO\n3 - VOLTAR")
        r = input('')

        if (r == '1'):

            # Album que seja mostrado as descricoes
            i = input("\nDigite o id do álbum: ")
            while(i[0] < '1' or i[0] > '9'):
                i = input("Digite o id do álbum: ")

            i= eval(i)

            cur.execute("SELECT count(id) FROM album WHERE id = %s;", (i,))
            q = cur.fetchone()[0]

            # Caso nao encontre o album
            if (q == 0):
                print("\nNao há este álbum.")


            # Caso ache o album
            else:
                print('')
                # Imprime as especificacoes do album
                cur.execute("SELECT id, nome, duracao, ano, stock, preco  FROM album WHERE id = %s;", (i,))
                for linha in cur.fetchall():
                    print("Nome:", linha[1], " | Duração:", linha[2], " | Ano:", linha[3]," | Stock:", linha[4], " | Preço:", linha[5])

                cur.execute("SELECT musica.musica from  album, musica_album, musica  where album.id = musica_album.album_id  and musica_album.musica_id = musica.id  and album.id = %s;",(i,))
                print("Musicas do álbum:")
                for linha in cur.fetchall():
                    print(" ", linha[0])

                cur.execute("SELECT artista.artista from  album, artista_album, artista  where album.id = artista_album.album_id  and artista_album.artista_id = artista.id  and album.id = %s;",(i,))
                print("Artistas do álbum:")
                for linha in cur.fetchall():
                    print(" ", linha[0])

                cur.execute("SELECT tipo_genero from  album, album_genero, genero  where album.id = album_genero.album_id  and album_genero.genero_id = genero.id  and album.id = %s;",(i,))
                print("Generos do álbum:")
                for linha in cur.fetchall():
                    print(" ", linha[0])

                cur.execute("SELECT count(preco)  FROM historico_a WHERE album_id = %s;", (i,))
                a = cur.fetchone()[0]
                if (a != 0):
                    print("Preços anteriores: ")
                    # imprime alteracoes de preco
                    cur.execute("SELECT preco  FROM historico_a WHERE album_id = %s;", (i,))
                    for linha in cur.fetchall():
                        print(linha[0])

                print("\nDeseja adicionar album no carrinho?")
                print("1 - SIM\n2 - NAO")
                j = input('')
                if (j != '1' or j != '2'):
                    print("\nOpção não válida.")
                j = '0'
                if (j == '1'):
                    operacoes_carrinho.add(conn, cur, id, nome)


        elif (r == '2'):
            print("\nDeseja adicionar album no carrinho?")
            print("1 - SIM\n2 - NAO")
            j = input('')

            if (j == '1'):
                operacoes_carrinho.add(conn, cur, id, nome)

            elif(j == '2'):
                return

            else:
                print("Opção não válida.")

        elif (r == '3'):
            print("Voltar")

        else:
            print("Opção não válida.")
#-------------------------------------------------------------------------------------------------------------

def por_musica(conn,cur,id, nome):
    print('\n')
    print('Usuario:', nome)
    print('ORDENAR POR MÚSICA')
    #imprime musica por ordem ascendente
    cur.execute("SELECT musica, album.nome FROM musica, album, musica_album WHERE musica.id=musica_album.musica_id and musica_album.album_id = album.id ORDER BY musica.id ASC")
    for linha in cur.fetchall():
        print("Nome:", linha[0], " | Álbum:", linha[1])

    print("\nDeseja adicionar algum album no carrinho?")
    print("1 - SIM\n2 - NAO")
    j = input('')
    if(j =='1'):
        operacoes_carrinho.add(conn,cur,id)

    elif(j == '2'):
        return

    else:
        print("Opção não válida.")

#-------------------------------------------------------------------------------------------------------------

def por_grupo(conn,cur,id, nome):
    print('\n')
    print('Usuario:', nome)
    print('ORDENAR POR GRUPO')
    #imprime artista por ordem ascendente
    cur.execute("SELECT artista, album.nome FROM artista, album, artista_album WHERE artista.id=artista_album.artista_id and artista_album.album_id = album.id ORDER BY artista.id ASC")
    for linha in cur.fetchall():
        print("Artista:", linha[0], " | Álbum:", linha[1])

    print("\nDeseja adicionar algum album no carrinho?")
    print("1 - SIM\n2 - NAO")
    j = input('')
    if (j == '1'):
        operacoes_carrinho.add(conn, cur, id)

    elif (j == '2'):
        return

    else:
        print("Opção não válida.")


#-------------------------------------------------------------------------------------------------------------

def por_genero(conn,cur,id, nome):
    print('\n')
    print('Usuario:', nome)
    print('ORDENAR POR GENERO')
    #imprime genero por ordem ascendente
    cur.execute("SELECT tipo_genero, album.nome FROM genero, album, album_genero WHERE genero.id=album_genero.genero_id and album_genero.album_id = album.id ORDER BY genero.id ASC")
    for linha in cur.fetchall():
        print("Genero:", linha[0], " | Álbum:", linha[1])

    print("\nDeseja adicionar algum album no carrinho?")
    print("1 - SIM\n2 - NAO")
    j = input('')
    if (j == '1'):
        operacoes_carrinho.add(conn, cur, id)

    elif (j == '2'):
        return

    else:
        print("Opção não válida.")

