salario = float(input('Qual é o salário do funcionário? R$'))
aum = salario + (salario * (15 / 100))
print(f'O funcionário que recebia R${salario:.2f}, com aumento de 15% irá receber R${aum:.2f}')
