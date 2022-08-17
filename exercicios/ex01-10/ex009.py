def linha(msg):
    print('-' * 30)
    print(msg.center(30))
    print('-' * 30)


linha('TABUADA')
n = int(input('Digite um número para saber a sua tabuada: '))
for c in range(1, 11):
    t = n * c
    print(f'{n} x {c:2} = {t:2}')
