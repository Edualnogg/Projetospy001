### geração de senha mais complexa ###
import string
from random import random, choice

valores = string.ascii_lowercase + string.ascii_uppercase + \
    string.digits + string.punctuation
### nesse caso, considerei maiúsculas e minúsculas ###
### todos os números de 0 a 9 ###
### caracteres especiais ###

tamanho = 7
senha = ""

for i in range(tamanho):
    senha += choice(valores)

print(senha)

### se eu  utilizar o comando 'seed'(semente), ou seja, a senha será gerada pela mesma semente, portanto se repetirá ###
