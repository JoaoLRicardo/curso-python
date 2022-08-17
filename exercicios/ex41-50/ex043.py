def escreva(msg):
    tam = len(msg) + 4
    print(tam * '=')
    print(f'  {msg}')
    print(tam * '=')


escreva('CALCULADORA DE IMC')
print()
peso = float(input('Qual é o seu peso?(Kg) '))
altura = float(input('Qual é a sua altura?(m) '))
imc = peso / (altura ** 2)
print()
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de peso NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE, atenção!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
