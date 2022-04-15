# sorteio para confronto

import random


t1 = input('Time: ')
t2 = input('Time: ')
t3 = input('Time: ')
t4 = input('Time: ')

times = [t1, t2, t3, t4]


def selectRandom(times):
    return random.choice(times)
print('O confronto é entre: ', selectRandom(times))

