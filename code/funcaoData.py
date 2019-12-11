# FORMATACAO DA DATA:
def data():
    # DIA: entra no ciclo e fica pedindo o dia de nascimento ate que este esteja entre 1 e 31
    #      no if verifica se o numero digitado comeca ou nao com 0
    #      se comecar com 0, verifica-se se existe um numero seguinte ao 0, caso exista este numero é registado. Se nao existir outro numero é dado que d é igual a 0 e recomeca o ciclo
    #      se o numero nao comecar com 0, o proximo if verifica se este numero é abaixo do 10 e entao salva um 0 na sua frente.
    #
    # O MESMO OCORRE PARA O MES


    d = 0
    while(d<1 or d>31):
        dia = input('Dia: ')
        a = 0
        #verifica se o usuario nao digitou nada diferente de numero
        if(dia >= '' and dia <= '/' or dia >= ':' or dia == None ):
            d=0

        else:
            if(dia[0] == '0'):
                if(len(dia) != 2):
                 d=0
                else:
                    if(dia[1] >= '1' and dia[1] <= '9' ):
                        a = dia[1]
                        d = eval(a)

            else:
                d = eval(dia)

    if(d<10 and a == 0):
        aux=dia
        dia = '0' + aux


    m = 0
    while (m < 1 or m > 12):
        mes = input('Mes: ')
        b = 0

        # verifica se o usuario nao digitou nada diferente de numero
        if (mes >= '' and mes <= '/' or mes >= ':' or mes == None):
            m = 0

        else:
            if(mes[0] == '0'):
                if(len(mes) != 2):
                    m=0

                else:
                    if(mes[1] >= '1' and mes <= '9'):
                        b = mes[1]
                        m = eval(b)

            else:
                m = eval(mes)

    if(m<10 and b == 0):
        aux = mes
        mes = '0' + aux

    a = 0
    while(a < 1900 or a > 2019):
        ano = input('Ano: ')
        if(len(ano) != 4):
            a = 0
        else:
            a = eval(ano)


    data = dia + '-'+ mes + '-' + ano
    return data
