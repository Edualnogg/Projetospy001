# utilizando o comando 'for' e 'for in range'
'''
listas = ['Erisson', 'Eduardo', 'Almeida', 'Nogueira']
for i in listas:
    print(i)
else:
    print('Bejamin Rolla')

'''


'''
# for (variável qualquer) in (variável)
# para ir de 0 a 6 //// (inicia, termina, de quanto em quanto)
for i in range(0, 6):
    print(i)

'''


'''

n = int(input('Digite algum número: '))
for i in range(0, n+1):
    print(i)

'''


'''

# para ir adicionando
for i in range(0, 3):
    n = input('Digite algo: ')
print('FIM')

'''


# para fazer uma soma
s = 0
for i in range(0, 4):
    n = int(input('Digite algo: '))
    s += n
print('O somatório dos dados é {}.'.format(s))
