salario = float(input('Qual é o salário do funcionário? R$'))
if salario > 1250:
    aumento = (salario * 10 / 100) + salario
else:
    aumento = (salario * 15 / 100) + salario
print(f'Quem ganhava R${salario:.2f} passa a receber R${aumento:.2f} com aumento.')
