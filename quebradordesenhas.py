### esse programa pode ser usado para tentar descobrir uma senha pela força bruta, ou seja, tenttando todas combinação possíveis ###
### não está pegando ###


from math import comb
import string
import sys
import time
### serve p dar o tempo p achar a senha ###
from datetime import timedelta
from itertools import combinations_with_replacement
# essa função da todas as combinações de um tamanho x que eu passo, da lista que eu passei como entrada
# e devolve todas as combinações, incluindo repetição de caracteres
from random import seed, random


def main(args):

    valores = string.ascii_letters
    #valores += string.digits
    #valores += string.punctuation
    tamanho = 3


### esse código abaixo serve para dar o tempo para gerar a senha ###
#    ini_t = time.time()
#    gerar_senhas(valores, tamanho)
#    fin_t = time.time()
#    print("Tempo: " + str((fin_t - ini_t) + "s"))


### esse código serve para gerar as combinações das senhas ###
def gerar_senhas(valores, tamanho):
    comb = combinations_with_replacement(valores, tamanho)
    print(len(list(comb)))


if __name__ == '__main__':
    main(sys.argv[1:])


print(list(comb))
