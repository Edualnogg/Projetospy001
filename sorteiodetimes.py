### sorteio entre 3 times ###


from random import choice, random


t1 = input("Time 1: ")
t2 = input("Time 2: ")
t3 = input("time 3: ")


def sort():
    s = choice([t1, t2, t3])
    s1 = choice([t1, t2, t3])
    if s != s1:
        h = print('O jogo é entre',s, 'X',s1)
    else:
        s = choice([t1, t2, t3])
        s1 = choice([t1, t2, t3])

sort()
