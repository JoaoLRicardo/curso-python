sexo = str(input('Informe seu sexo:[M/F] ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo:[M/F] ')).upper().strip()[0]
if sexo == 'M':
    sexo = 'Masculino'
if sexo == 'F':
    sexo = 'Feminino'
print(f'Sexo {sexo} registrado com sucesso')
