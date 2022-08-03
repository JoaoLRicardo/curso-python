n = str(input('Digite seu nome completo: ')).strip().title()
nome = n.split()
print(f'Prazer em conhece-lo {n}')
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[-1]}')

