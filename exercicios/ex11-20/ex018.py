from math import sin, cos, tan, radians
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tang = tan(radians(angulo))
print(f'O ângulo de {angulo}º tem o SENO de {seno:.2f}')
print(f'O ângulo de {angulo}º tem o COSSENO de {cosseno:.2f}')
print(f'O ângulo de {angulo}º tem a TANGENTE de {tang:.2f}')
