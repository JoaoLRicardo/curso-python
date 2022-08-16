from datetime import date


def escreva(msg):
    tam = len(msg) + 4
    print(tam * '=')
    print(f'  {msg}')
    print(tam * '=')


escreva('CLASSIFICAÇÃO DE ATLETAS')
atual = date.today().year
while True:
    nascimento = input('Ano de nascimento: ')
    if nascimento.isdigit() and len(nascimento) == 4:
        nascimento = int(nascimento)
        break
    else:
        print(f'Por favor digite um ano válido exemplo: {date.today().year}.')
        print()
idade = atual - nascimento
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
