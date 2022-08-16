n1 = float(input('Primeira NOTA: '))
n2 = float(input('Segunda NOTA: '))
media = (n1 + n2) / 2
print(f'Tirando {n1} e {n2}, a média do aluno é {media:.1f}')
if media < 5:
    print('REPROVADO!')
elif 7 > media >= 5:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')
