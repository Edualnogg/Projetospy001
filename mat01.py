###programa que calcula o dobro e o meio de um número inteiro qualquer###

###coloquei exemplos de {.f} para mostrar quantas casas decimais eu quero###

n = int(input("Digite um número inteiro qualquer: "))
d = 2*n
e = n/2
print("O dobro é {:1.2f} e seu meio {:f}".format(d, e))
