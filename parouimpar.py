 ### Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR ###

numero = int(input('Me diga um número qualquer: '))

### Em Python, o operador resto é o sinal de porcentagem ( % ) ###

''' 
O operador resto é surpreendentemente útil. 
Por exemplo, você pode verificar se um número é divisível por outro—se x % y é zero,
então x é divisível por y. Além disso, você pode extrair o dígito ou dígitos 
mais à direita de um número: x % 10 resulta no dígito mais à direita de x (unidade).
De forma similar, x % 100 retorna os últimos dois dígitos (dezena e unidade)

'''
resultado = numero % 2
if resultado == 0:
    print('O número {} é PAR!'.format(numero))
else:
    print('O número {} é IMPAR!'.format(numero))

### o resto é EX: 10/3 = 3,33... portanto o 10%3 = 1; pq 3 x 3 = 9  e 10-9 = 1 ||que é o resto|| ###
