import math

# criar um programa que calcule as componentes x e y de um vetor

# y = sen0 . r        x = cos0 . r

h = float(input('Qual o valor do vetor primário(do DCL)? '))
t = float(input('Qual o valor do angulo?'))

cos = math.cos(t)
sen = math.sin(t)

y = sen * h
x = cos * h

print(f'A componente y é {y:.2f} e a x {x:.2f}')
