import csv
import lib.gera_sessenta as sessenta


def cinco_partes(result):
    qp = []
    qp.append(result[0:12])
    qp.append(result[12:24])
    qp.append(result[24:36])
    qp.append(result[36:48])
    qp.append(result[48:60])
    return sessenta.matrix_string(qp)


def show(result):
    print('-' * 90)
    sessenta.print_lista(cinco_partes(result)[0])
    sessenta.print_lista(cinco_partes(result)[1])
    sessenta.print_lista(cinco_partes(result)[2])
    sessenta.print_lista(cinco_partes(result)[3])
    sessenta.print_lista(cinco_partes(result)[4])


def matriz_geradora():
    return [
        [1, 2, 3,  4,  5,  6],
        [1, 2, 3,  4,  7,  8],
        [1, 2, 3,  4,  9, 10],
        [1, 2, 3,  4, 11, 12],
        [1, 2, 5,  6,  7,  8],
        [1, 2, 5,  6,  9, 10],
        [1, 2, 5,  6, 11, 12],
        [1, 2, 7,  8,  9, 10],
        [1, 2, 7,  8, 11, 12],
        [1, 2, 9, 10, 11, 12],
        [3, 4, 5,  6,  7,  8],
        [3, 4, 5,  6,  9, 10],
        [3, 4, 5,  6, 11, 12],
        [3, 4, 7,  8,  9, 10],
        [3, 4, 7,  8, 11, 12],
        [3, 4, 9, 10, 11, 12],
        [5, 6, 7,  8,  9, 10],
        [5, 6, 7,  8, 11, 12],
        [5, 6, 9, 10, 11, 12],
        [7, 8, 9, 10, 11, 12],

    ]


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
