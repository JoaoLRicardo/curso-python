def escreva(msg):
    tam = len(msg) + 4
    print(tam * '=')
    print(f'  {msg}')
    print(tam * '=')


times = ('Palmeiras', 'Fluminense', 'Flamengo', 'Corinthians', 'Internacional',
         'Athletico-PR', 'Atlético-MG', 'Santos', 'América-MG', 'Bragantino',
         'Goiás', 'São Paulo', 'Fortaleza', 'Botafogo', 'Ceará', 'Cuiabá',
         'Avaí', 'Coritiba', 'Atlético-GO', 'Juventude')
escreva('CLASSIFICAÇÃO BRASILEIRAO SÉRIE A')
c = 0
for t in times:
    c += 1
    if c < 5:
        print(f'\033[32m{c}º {t}')
    if 5 <= c <= 15:
        print(f'\033[m{c}º {t}')
    if c > 16:
        print(f'\033[31m{c}º {t}')
print('\033[m')
print(f'Os 5 primeiros são {times[0:5]}')
print(f'Os 4 últimos são {times[-4:]}')
