from random import randint
from time import sleep


def escreva(msg):
    tam = len(msg) + 4
    print(tam * '=')
    print(f'  {msg}')
    print(tam * '=')


itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)
print()
print('{:^40}'.format(' \033[32mJO\033[35mKEN\033[36mPOO!\033[m '))
print()
print('''\033[33mSuas opções: 
[1] PEDRA
[2] PAPEL
[3] TESOURA
''')

while True:
    jogador = input('\033[35mQual é a sua jogada? ')
    if jogador.isdigit():
        jogador = int(jogador) - 1
    if jogador == 0 or jogador == 1 or jogador == 2:
        break
    else:
        print()
        print('\033[31mJogada inválida!\033[m')
        print('''\033[33mSuas opções: 
[1] PEDRA
[2] PAPEL
[3] TESOURA
''')

print()
print('{:^25}'.format('\033[32mJO'))
sleep(1)
print('{:^26}'.format('\033[35mKEN'))
sleep(1)
print('{:^32}'.format('\033[36mPOO!!!\033[m'))
print()
print('\033[33m-=' * 12)
print(f'\033[31mComputador\033[m jogou \033[33m{itens[computador]}')
print(f'\033[32mJogador\033[m jogou \033[33m{itens[jogador]}')
print('\033[33m-=' * 12)

if computador == 0:
    if jogador == 0:
        print('\033[33m')
        escreva('EMPATE')
        print('\033[m')
    elif jogador == 1:
        print('\033[32m')
        escreva('JOGADOR VENCEU')
        print('\033[m')
    elif jogador == 2:
        print('\033[31m')
        escreva('COMPUTADOR VENCEU')
        print('\033[m')
elif computador == 1:
    if jogador == 0:
        print('\033[31m')
        escreva('COMPUTADOR VENCEU')
        print('\033[m')
    elif jogador == 1:
        print('\033[33m')
        escreva('EMPATE')
        print('\033[m')
    elif jogador == 2:
        print('\033[32m')
        escreva('JOGADOR VENCEU')
        print('\033[m')
elif computador == 2:
    if jogador == 0:
        print('\033[32m')
        escreva('JOGADOR VENCEU')
        print('\033[m')
    elif jogador == 1:
        print('\033[31m')
        escreva('COMPUTADOR VENCEU')
        print('\033[m')
    elif jogador == 2:
        print('\033[33m')
        escreva('EMPATE')
        print('\033[m')
