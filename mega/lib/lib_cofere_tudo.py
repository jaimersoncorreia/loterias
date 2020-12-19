def meutostring(meu_jogo):
    meu_jogo_string = '['
    for dezena in meu_jogo:
        meu_jogo_string += ' {:02}'.format(dezena)

    return meu_jogo_string + ']'


def confere_dezena(sorteio, meu_jogo):
    qtde = 0
    for dezena_sorte in sorteio:
        for dezena_jogo in meu_jogo:
            qtde += 1 if dezena_sorte == dezena_jogo else 0
    return qtde


def confere_todos(sorteio, meus_jogos):
    vetor_qtde_dezena = []
    for meu_jogo in meus_jogos:
        vetor_qtde_dezena.append(confere_dezena(sorteio, meu_jogo))
    return vetor_qtde_dezena


def confere_full(meus_jogos, megasena):
    somas = [0, 0, 0]
    for mega in megasena:
        strdez = []
        for dezena in mega:
            strdez.append("{:02}".format(dezena))

        sorteio = list(map(int, strdez))
        j = confere_todos(sorteio, meus_jogos)
        sena = j.count(6)
        quina = j.count(5)
        quadra = j.count(4)

        print("{}\tSena:{}, Quina:{}, Quadra:{}".format(
            strdez, sena, quina, quadra))

        somas[0] += sena
        somas[1] += quina
        somas[2] += quadra
    print("\n\nRelatório")
    print("Total:\tSena:{}, Quina:{}, Quadra:{}".format(
        somas[0], somas[1], somas[2]))
