total = 0
print('\033[32m{:^40}'.format('\033[32m LOJAS GUANABARA '))
preco = float(input('\033[mPreço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro 
[2] à vista cartão
[3] parcelado no cartão
''')
while True:
    menu1 = input('Qual a forma de pagamento? ').strip()
    if menu1.isnumeric():
        menu1 = int(menu1)
    if menu1 == 1 or menu1 == 2 or menu1 == 3:
        break
    else:
        print()
        print('\033[31mOpção inválida!\033[m')
        print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro 10% desconto
[2] à vista cartão 5% desconto
[3] parcelado no cartão
''')
if menu1 == 1:
    total = preco - (preco * 10 / 100)
elif menu1 == 2:
    total = preco - (preco * 5 / 100)
elif menu1 == 3:
    while True:
        print('''PARCELAMENTO
[1] até 6x sem juros 
[2] até 10x com 5% de juros
[3] acima de 10x com 15% de juros
    ''')
        menu2 = input('Qual a forma de pagamento? ').strip()
        if menu2.isnumeric():
            menu2 = int(menu2)
        if menu2 == 1:
            totparc = input('Quantas parcelas? ').strip()
            if totparc.isnumeric():
                totparc = int(totparc)
                if totparc == 0:
                    totparc = 1
            parcela = preco / totparc
            if 1 <= totparc <= 6:
                total = preco
                print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} sem juros')
                break
            if 6 < totparc <= 10:
                total = (preco + (preco * 5 / 100))
                parcela = total / totparc
                print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} com 5% de juros')
                break
            if totparc > 10:
                total = (preco + (preco * 15 / 100))
                parcela = total / totparc
                print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} com 15% de juros')
                break
        if menu2 == 2:
            totparc = input('Quantas parcelas? ').strip()
            if totparc.isnumeric():
                totparc = int(totparc)
            parcela = preco / totparc
            if 1 <= totparc <= 6:
                total = preco
                print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} sem juros')
                break
            if 6 < totparc <= 10:
                total = (preco + (preco * 5 / 100))
                parcela = total / totparc
                print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} com 5% de juros')
                break
            if totparc > 10:
                total = (preco + (preco * 15 / 100))
                parcela = total / totparc
                print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} com 15% de juros')
                break
        if menu2 == 3:
            totparc = input('Quantas parcelas? ').strip()
            if totparc.isnumeric():
                totparc = int(totparc)
            parcela = preco / totparc
            if 1 <= totparc <= 6:
                total = preco
                print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} sem juros')
                break
            if 6 < totparc <= 10:
                total = (preco + (preco * 5 / 100))
                parcela = total / totparc
                print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} com 5% de juros')
                break
            if totparc > 10:
                total = (preco + (preco * 15 / 100))
                parcela = total / totparc
                print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} com 15% de juros')
                break
        else:
            print()
            print('\033[31mOpção inválida!\033[m')
print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.')
