import csv
import lib.gera_sessenta as sessenta


def quatro_partes(result):
    qp = []
    qp.append(result[0:15])
    qp.append(result[15:30])
    qp.append(result[30:45])
    qp.append(result[45:60])
    return sessenta.matrix_string(qp)


def show(result):
    print('-' * 90)
    sessenta.print_lista(quatro_partes(result)[0])
    sessenta.print_lista(quatro_partes(result)[1])
    sessenta.print_lista(quatro_partes(result)[2])
    sessenta.print_lista(quatro_partes(result)[3])


def matriz_geradora():
    return [[1, 2, 3, 4, 5, 6],
            [1, 2, 3, 7, 8, 9],
            [1, 2, 3, 10, 11, 12],
            [1, 2, 3, 13, 14, 15],
            [4, 5, 6, 7, 8, 9],
            [4, 5, 6, 10, 11, 12],
            [4, 5, 6, 13, 14, 15],
            [7, 8, 9, 10, 11, 12],
            [7, 8, 9, 13, 14, 15],
            [10, 11, 12, 13, 14, 15]]


def gera_sena(vetor_base, lista):
    sena = []
    for n in vetor_base:
        sena.append(lista[n-1])
    sena.sort()
    return sena


def grava_partes(nome_arquivo, parte):
    with open(nome_arquivo, 'w') as salva_csv:
        grava = csv.writer(salva_csv)
        grava.writerows(parte)
    salva_csv.close()
    print('Gravado como "{}"'.format(nome_arquivo))
