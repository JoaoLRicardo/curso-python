def escreva(msg):
    tam = len(msg) + 4
    print(tam * '=')
    print(f'  {msg}')
    print(tam * '=')


escreva('CONVERSOR DE BASES NUMÉRICAS')
while True:
    num = input('Digite um número inteiro: ')
    if num.isdigit():
        num = int(num)        
        break
    else:
        print()
        print('Por favor digite um número inteiro.')

while True:
    print('''Escolha uma das bases para conversão:
            [1] converter para BINÁRIO
            [2] converter para OCTAL
            [3] converter para HEXADECIMAL
            ''')

    opcao = input('Sua opção: ')
    if opcao.isdigit():
        opcao = int(opcao)
        if opcao == 1:
            print(f'{num} convertido para BINÁRIO é {bin(num) [2:]}')
            break
        elif opcao == 2:
            print(f'{num} convertido para OCTAL é {oct(num) [2:]}')
            break
        elif opcao == 3:
            print(f'{num} convertido para HEXADECIMAL é {hex(num) [2:]}')  
            break              
        else:
            print('Opção inválida.')
            print()
    else:
        print()
        print('Digite uma das opções disponíveis por gentileza.')
