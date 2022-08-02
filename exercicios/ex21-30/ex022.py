from time import sleep


def linha(msg):
    print('-' * 30)
    print(msg.center(30))
    print('-' * 30)


linha('ANALISADOR DE NOMES')
nome = str(input('Digite seu nome completo: ')).strip().upper()
print('Analisando seu nome...')
sleep(2)
print(f'Prazer em conhece-lo {nome.title()}')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')
separa = nome.split()
print(f'Seu ultimo nome é {separa[-1]} e ele tem {len(separa[-1])} letras')
