def leiaint(msg):
    while True:     
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print()
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


num = leiaint('Digite um valor: ')
print(f'O valor digitado foi {num}')