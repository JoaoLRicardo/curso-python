opcao = 0
while True:
    n1 = input('Primeiro valor: ')
    if n1.isdigit():
        n1 = int(n1)
        break
    else:
        print('\033[31mValor inválido!\033[m')
while True:
    n2 = input('Segundo valor: ')
    if n2.isdigit():
        n2 = int(n2)
        break
    else:
        print('\033[31mValor inválido!\033[m')


while opcao != 5:
    print('''
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
''')
    opcao = input('Qual é a sua opção? ')
    if opcao.isdigit():
        opcao = int(opcao)
        if opcao == 1:
            soma = n1 + n2
            print(f'A soma entre {n1} e {n2} é {soma}')
            
        elif opcao == 2:
            mult = n1 * n2
            print(f'O resultado de {n1} x {n2} é {mult}')
            
        elif opcao == 3:
            if n1 > n2:
                maior = n1
            else:
                maior = n2
            print(f'Entre {n1} e {n2} o maior valor é {maior}')
            
        elif opcao == 4:
            print('Informe novos números: ')
            while True:
                n1 = input('Primeiro valor: ')
                if n1.isdigit():
                    n1 = int(n1)
                    break
                else:
                    print('\033[31mValor inválido!\033[m')
            while True:
                n2 = input('Segundo valor: ')
                if n2.isdigit():
                    n2 = int(n2)
                    break
                else:
                    print('\033[31mValor inválido!\033[m')

        elif opcao == 5:
            print('Finalizando...')        
        else:        
            print('\033[31mOpção inválida!\033[m')     
print('Volte sempre!')
