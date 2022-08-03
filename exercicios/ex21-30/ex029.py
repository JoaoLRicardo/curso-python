velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('\33[031mMULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade - 80) * 7
    print(f'Você passou a {velocidade:.0f}Km/h e terá que pagar uma multa de \033[033mR${multa:.2f}!\033[m')
print('\033[032mTenha um bom dia! Dirija com segurança!')
