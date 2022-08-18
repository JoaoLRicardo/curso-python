maioridadehomen = totmulher20 = somaidade = mediaidade = 0
nomevelho = ''

for p in range(1, 5):
    print(f'{p}ª PESSOA')
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    somaidade += idade
    if p == 1 and sexo in 'M':
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'M' and idade > maioridadehomen:
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade} anos.')
print(f'O homem mais velho tem {maioridadehomen} anos e se chama {nomevelho}.')
if totmulher20 > 2:
    print(f'Ao todo temos {totmulher20} mulheres com menos de 20 anos.')
else:
    print(f'Temos apenas {totmulher20} mulher com menos de 20 anos.')
