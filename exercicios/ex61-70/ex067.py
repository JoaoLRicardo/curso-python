while True:
    num = int(input('Quer ver a tabuada de qual valor [0 para SAIR]? '))
    print()
    if num == 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c:2} = {num * c:2}')
    print()
print('PROGAMA TABUADA ENCERRADO COM SUCESSO.')
