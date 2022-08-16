from random import randint
from time import sleep


itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)
print('''Suas opções: 
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')

while True:
    jogador = input('Qual é a sua jogada? ')
    if jogador.isdigit():
        jogador = int(jogador)
    if jogador == 0 or jogador == 1 or jogador == 2:
        break
    else:
        print()
        print('Jogada inválida!')
        print('''Suas opções: 
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')

print()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POO!!!')
print()
print('-=' * 14)
print(f'   Computador jogou {itens[computador]}')
print(f'   Jogador jogou {itens[jogador]}')
print('-=' * 14)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
print('-=' * 14)
