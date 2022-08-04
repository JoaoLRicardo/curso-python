def escreva(msg):
    tam = len(msg) + 4
    print(tam * '=')
    print(f'  {msg}')
    print(tam * '=')


escreva('EMPRÉSTIMO IMOBILIÁRIO')
casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos', end='')
print(f' a prestação será de R${prestacao:.2f}')
if prestacao < (salario * 30 / 100):
    print('Empréstimo APROVADO!')
else:
    print('Emprétimo NEGADO!')
