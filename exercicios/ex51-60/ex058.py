from random import randint
computador = randint(0, 10)
print()
print('-=' * 33)
print('Sou seu computador... acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi...')
print('-=' * 33)
print()
acertou = False
c = 0
while not acertou:
    while True:
        jogador = input('Qual é seu palpite? ')
        if jogador.isdigit():
            jogador = int(jogador)
            c += 1
            break
        else:
            print('\033[31mJogada inválida digite um número entre 0 e 10.\033[m')
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente novamente.')
            print()
        elif jogador > computador:
            print('Menos...Tente novamente.')
            print()
print()
print(f'\033[32mAcertou com {c} tentativas. Parabéns!\033[m')
