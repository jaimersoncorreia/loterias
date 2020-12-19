from random import randint


def gera_sessenta():
    result = []
    while len(result) != 60:
        r = randint(1, 60)
        if r not in result:
            result.append(r)
    return result


def soma_lista(lista):
    soma = 0
    for n in lista:
        soma += int(n)
    return soma/12


def cont_par(lista):
    cont = 0
    for n in lista:
        cont += 1 if int(n) % 2 == 0 else 0
    return cont


def cont_impar(lista):
    cont = 0
    for n in lista:
        cont += 1 if int(n) % 2 == 1 else 0
    return cont


def print_lista(lista):
    print('{}'.format(lista))
    print('|Qtde Números:{}\t|Média:{}\t|Qtde par:{:02.0f}\t|Qtde impar:{:02.0f}'.format(
        len(lista), soma_lista(lista), cont_par(lista), cont_impar(lista)))
    print('-' * 90)


def para_string(sequencia):
    transformado = []
    for seq in sequencia:
        transformado.append('{:02.0f}'.format(seq))
    return transformado


def matrix_string(matrix):
    m = []
    for vetor in matrix:
        m.append(para_string(vetor))
    return m
