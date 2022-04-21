# ANALISANDO TEXTOS


# o '.strip' irá eliminar os epaços antes e depois do nome, mas não entre.
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))

# o '- nome.count' faz desconsiderar os espaços
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))


# para contar apenas as letras do  primeiro nome
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
# ou
separa = nome.split()
# o comando acima irá saparar o nome criando  uma lista
print('Seu primeiro nome tem {} letras'.format(len(separa[0])))
