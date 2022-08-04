distancia = float(input('\033[035mQual é a distância da sua viagem? Km\033[m'))
print(f'Você está prestes a começar uma viagem de {distancia}Km.')
if distancia <= 200:
    tarifa = distancia * 0.50
    print(f'O custo de uma viagem de {distancia}Km será de R${tarifa:.2f}')
else:
    tarifa = (distancia - 200) * 0.45
    tarifa2 = tarifa + 100
    print(f'O custo de uma viagem de {distancia}Km será de R${tarifa2:.2f}')
