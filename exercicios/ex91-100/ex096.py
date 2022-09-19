def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m²')


def escreva(msg):
    tam = len(msg) + 4
    print(tam * '=')
    print(f'  {msg}')
    print(tam * '=')



# PROGRAMA PRINCIPAL
escreva('Controle de Terrenos')
print()
l = float(input('LARGURA(m): '))
c = float(input('COMPRIMENTO(m): '))
area(l, c)
