numero = int(input('\033[035mDigite um número qualquer: \033[m'))
resultado = numero % 2
if resultado == 0:
    print(f'O número {numero} é \033[034mPAR!')
else:
    print(f'O número {numero} é \033[034mÍMPAR!')
