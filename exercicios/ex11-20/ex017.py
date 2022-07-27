import math
def linha(msg):
    print('-' * 30)
    print(msg.center(30))
    print('-' * 30)


linha('CALCULO DE HIPOTENUSA')
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print(f'A hipotenusa vai medir {hi:.2f}')
