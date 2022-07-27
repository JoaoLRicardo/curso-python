def linha(msg):
    print('-' * 30)
    print(msg.center(30))
    print('-' * 30)


linha('CONVERSOR DE MEDIDA')
metros = float(input('Digite uma distância em metros: '))
km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000
print(f'A media de {metros:.2f}m corresponde a:')
print(f'{km:.4f}km \n{hm:.2f}hm \n{dam:.2f}dam \n{dm:.0f}dm \n{cm:.0f}cm \n{mm:.0f}mm')
