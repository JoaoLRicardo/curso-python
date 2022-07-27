def linha(msg):
    print('-' * 30)
    print(msg.center(30))
    print('-' * 30)


linha('ALGUEL DE CARROS')
km = float(input('Quantos Km o carro percorreu? '))
dias = int(input('Quantas diárias? '))
soma = (dias * 60) + (km * 0.15)
print(f'O preço total a pagar pelo aluguel é de R${soma:.2f}')
