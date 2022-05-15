from random import randint
from time import sleep
from defs import microfone
from defs.voz import maquina_voz

def jogo():
    itens = ('pedra', 'papel', 'tesoura')

    computador = randint(0,2)
    opcoes_jogadas = [0, 1, 2]
    maquina_voz('Vamos jogar Jokenpo!!!')
    sleep(0.5)
    print('-=-'*15)
    print('''Faça sua jogada :
    [0] Pedra
    [1] Papel
    [2] Tesoura''')
    print('-=-'*15)
    maquina_voz('faça sua jogada', printAtivo=False)
    sleep(0.5)
    maquina_voz('Digite 0 para pedra', printAtivo=False)
    sleep(0.5)
    maquina_voz('Digite 1 para papel', printAtivo=False)
    sleep(0.5)
    maquina_voz('Digite 2 para tesoura', printAtivo=False)
    sleep(0.5)
    maquina_voz('Qual a sua jogada? ')
    jogador = int(microfone.abrir_mic())
    sleep(1)
    maquina_voz('JO')
    sleep(1)
    maquina_voz('KEN')
    sleep(1)
    maquina_voz('PO')
    sleep(1)
    print('-=-'*15)
    maquina_voz(f'Computador jogou: {itens[computador].upper()}')
    maquina_voz(f'Jogador jogou: {itens[jogador].upper()}')
    print('-=-'*15)
    sleep(1)
    maquina_voz('PROCESSANDO...')
    sleep(3)
    jogadas = [
        {
            0: 'EMPATE',
            1: 'JOGADOR GANHOU',
            2: 'COMPUTADOR GANHOU'
        },
        {
            0: 'COMPUTADOR GANHOU',
            1: 'EMPATE',
            2: 'JOGADOR GANHOU'
        },
        {
            0: 'JOGADOR GANHOU',
            1: 'COMPUTADOR GANHOU',
            2: 'EMPATE'
        }
    ]
    if jogador in opcoes_jogadas:
        resultado = jogadas[computador][jogador]
        maquina_voz(resultado)
    else:
        maquina_voz('opção invalida')