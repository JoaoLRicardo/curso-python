def escreva(msg):
    tam = len(msg) + 4
    print(tam * '=')
    print(f'  {msg}')
    print(tam * '=')


escreva('Gerador de PA')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
tot = 0
mais = 10
while mais != 0:
    tot += mais
    while cont <= tot:
        print(f'{termo} → ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {tot} termos mostrados.')
