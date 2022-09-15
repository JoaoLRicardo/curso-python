matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for li in range(0, 3):
    for c in range(0, 3):
        matriz[li][c] = int(input(f'Digite um valor para [{li}, {c}]: '))
print('-=' * 30)
for li in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[li][c]:^5}]', end='')
    print()
