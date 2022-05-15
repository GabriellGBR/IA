def jogo():
    from random import randint
    from time import sleep
    import pyttsx3
    import microfone
    maquina = pyttsx3.init()
    voices = maquina.getProperty('voices')
    maquina.setProperty('voice', voices[-2].id)
    itens = ('pedra', 'papel', 'tesoura')

    computador = randint(0,2)

    print('Vamos jogar Jokenpo!!!')
    maquina.say('Vamos jogar Jokenpo!!!')
    maquina.runAndWait()
    sleep(0.5)
    print('-=-'*15)
    print('''Faça sua jogada :
    [0] Pedra
    [1] Papel
    [2] Tesoura''')
    print('-=-'*15)
    maquina.say('faça sua jogada')
    maquina.runAndWait()
    sleep(0.5)
    maquina.say('Digite 0 para pedra')
    maquina.runAndWait()
    sleep(0.5)
    maquina.say('Digite 1 para papel')
    maquina.runAndWait()
    sleep(0.5)
    maquina.say('Digite 2 para tesoura')
    maquina.runAndWait()
    sleep(0.5)
    print('Qual a sua jogada? ')
    maquina.say('Qual a sua jogada? ')
    maquina.runAndWait()
    jogador = int(microfone.abrir_mic())
    sleep(1)
    print('JO')
    maquina.say('JO')
    maquina.runAndWait()
    sleep(1)
    print('KEN')
    maquina.say('KEN')
    maquina.runAndWait()
    sleep(1)
    print('PO')
    maquina.say('PO')
    maquina.runAndWait()
    sleep(1)
    print('-=-'*15)
    print(f'Computador jogou: {itens[computador].upper()}')
    maquina.say(f'Computador jogou {itens[computador].upper()}')
    maquina.runAndWait()
    print(f'Jogador jogou: {itens[jogador].upper()}')
    maquina.say(f'Jogador jogou: {itens[jogador].upper()}')
    print('-=-'*15)
    sleep(1)
    print('PROCESSANDO...')
    maquina.say('PROCESSANDO...')
    maquina.runAndWait()
    sleep(3)
    if computador == 0:
        if jogador == 0:
            print('EMPATE')
            maquina.say('EMPATE')
        elif jogador == 1:
            print('JOGADOR GANHOU')
            maquina.say('JOGADOR GANHOU')
        elif jogador == 2:
            print('COMPUTADOR GANHOU')
            maquina.say('COMPUTADOR GANHOU')
        else:
            print('OPCAO ESCOLHIDA INVALIDA')
            maquina.say('OPÇÃO ESCOLHIDA INVALIDA')
    elif computador == 1:
        if jogador == 0:
            print('COMPUTADOR GANHOU')
            maquina.say('COMPUTADOR GANHOU')
        elif jogador == 1:
            print('EMPATE')
            maquina.say('EMPATE')
        elif jogador == 2:
            print('JOGADOR GANHOU')
            maquina.say('JOGADOR GANHOU')
        else:
            print('OPCAO ESCOLHIDA INVALIDA')
            maquina.say('OPÇÃO ESCOLHIDA INVALIDA')
    elif computador == 2:
        if jogador == 0:
            print('JOGADOR GANHOU')
            maquina.say('JOGADOR GANHOU')
        elif jogador == 1:
            print('COMPUTADOR GANHOU')
            maquina.say('COMPUTADOR GANHOU')
        elif jogador == 2:
            print('EMPATE')
            maquina.say('EMPATE')
        else:
            print('OPCAO ESCOLHIDA INVALIDA')
            maquina.say('OPÇÃO ESCOLHIDA INVALIDA')
    maquina.runAndWait()


jogo()