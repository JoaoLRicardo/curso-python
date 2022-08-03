distancia = float(input('\033[035mQual é a distância da sua viagem? Km\033[m'))
print(f'Você está prestes a começar uma viagem de {distancia}Km.')
if distancia <= 200:
    preco = distancia * 0.50
    print(f'O custo de uma viagem de {distancia}Km será de R${preco:.2f}')
else:
    preco = (distancia - 200) * 0.45
    preco2 = preco + 100
    print(f'O custo de uma viagem de {distancia}Km será de R${preco2:.2f}')
