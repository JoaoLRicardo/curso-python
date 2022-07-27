soma = media = 0
for c in range(1, 3):
    n = float(input(f'Digite qual foi a {c}ª nota do aluno: '))
    soma += n
    media = soma / 2
print(f'A soma das notas digitadas é {media:.2f}')
