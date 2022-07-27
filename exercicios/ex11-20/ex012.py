preco = float(input('Digite o preço do produto:R$'))
desconto = preco - (preco * (5 / 100))
print(f'O produto que custava R${preco:.2f},com 5% de desconto fica R${desconto:.2f}')
