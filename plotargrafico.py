import matplotlib.pyplot

# criar lista para plotar (eixo x e y)
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
valores = [105235, 107697, 110256, 109236, 108859, 109986]

# esse comando diz para o python plotar o gráfico
matplotlib.pyplot.plot(meses, valores)

# diz para mostrar o gráfico, que já foi gerado mas está na memória
matplotlib.pyplot.show()


'''
*Os valores no nosso eixo Y são muito próximos um dos outros.* 
Por isso, qualquer mudança nos valores para mais, ou para 
menos, podem causar distorções no gráfico. Para evitar um pouco 
esse comportamento, podemos mudar os valores da base e do topo do eixo Y,
ou seja, podemos alterar seu limite (ylim()):


>> matplotlib.pyplot.plot(meses, valores)
>> matplotlib.pyplot.ylim(100000, 120000) //(aumentara o eixo y do gráfico, mostrando menos variação)
>> matplotlib.pyplot.show()
 
'''


'''
*DETALHANDO O GRÁFICO*

Podemos falar para o pyplot nomear o nosso gráfico, isto é, adicionar um título (title) a ele:

>> matplotlib.pyplot.title('Faturamento no primeiro semestre de 2017')

Podemos também pedir para o pyplot escrever quais os significados 
dos valores no eixo X e no eixo Y. Ou seja, podemos pedir
para ele rotular os dados desses eixos (xlabel, ylabel):

>> matplotlib.pyplot.xlabel('Meses')
>> matplotlib.pyplot.ylabel('Faturamento em R$')

'''


'''
SE USAR ESSE COMANDO:
>> import matplotlib.pyplot as plt

dá pra usar apelidos:
ao invés de "matplotlib.pyplot.show()", dá p usar "plt.show()"
'''
