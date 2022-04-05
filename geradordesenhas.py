import string
### contém a função que chama todo o alfabeto ###

from random import random, choice
### choice tem a função de escolher algo ###

valores = string.ascii_lowercase
### todo a alfabeto em letra mminúscula ###

tamanho = 5
### tamanho da senha ###

senha = ""

for i in range(tamanho):
    senha += choice(valores)
### para a senha no tamanho determinado (linha do 'for') ###
### para ir aplicando a escolha aleatória na senha dentro do tamanho de range ###

print(senha)
