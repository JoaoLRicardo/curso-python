from random import shuffle
n1 = str(input('Primeiro aluno: ')).title().strip()
n2 = str(input('Segundo aluno: ')).title().strip()
n3 = str(input('Terceiro aluno: ')).title().strip()
n4 = str(input('Quarto aluno: ')).title().strip()
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem escolhida será ')
print(lista)
