resp = 'S'
soma = c = media = maior = menor = 0
while resp in 'S':
    num = int(input('Digite um número: '))
    soma += num
    c += 1
    if c == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / c
print(f'Você digitou {c} números e a média foi {media}')
print(f'O maior valor foi{maior} e o menor foi {menor}')
