def meutostring(meu_jogo):
    meu_jogo_string = '['
    for dezena in meu_jogo:
        meu_jogo_string += ' {:02}'.format(dezena)

    return meu_jogo_string + ']'


def confere(sorteio, meu_jogo):
    cont = 0
    for dezena_sorte in sorteio:
        for dezena_jogo in meu_jogo:
            cont += 1 if dezena_sorte == dezena_jogo else 0

    return cont


def confere_todos(sorteio, meus_jogos):
    somas = [0, 0, 0]
    jogo = 1
    for meu_jogo in meus_jogos:
        qtde_dezena = confere(sorteio, meu_jogo)
        meu = meutostring(meu_jogo)
        if qtde_dezena == 6:
            print('Jogo{:003}: {} : Parabéns você é milionário'.format(jogo, meu))
            somas[0] += 1
        elif qtde_dezena == 5:
            print(
                'Jogo{:003}: {} : Parabéns você fez uma quina'.format(jogo, meu))
            somas[1] += 1
        elif qtde_dezena == 4:
            print(
                'Jogo{:003}: {} : Parabéns você fez uma quadra'.format(jogo, meu))
            somas[2] += 1
        else:
            print('Jogo{:003}: {} : Você acertou {} dezenas'.format(
                jogo, meu, qtde_dezena))
        jogo += 1

    print("\nRelatório Final")
    print("Sena:{}\nQuina:{}\nQuadra:{}".format(somas[0], somas[1], somas[2]))
