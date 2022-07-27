def linha(msg):
    print((len(msg) + 2) * '-')
    print(f'{msg:^2}')
    print((len(msg) + 2) * '-')


linha('CONVERSOR DE MEDIDA')
metros = float(input('Digite uma distância em metros: '))
c = metros / 100
ml = metros / 1000
