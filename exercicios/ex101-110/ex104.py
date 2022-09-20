def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg).strip())
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


# PROGRAMA PRINCIPAL
num = leiaint('Digite um número: ')
print(f'\033[32mVocê digitou o número {num}\033[m')
