# Identificador nome e uma lista de nomes

nomes = ["Messias", "Emanuel", "Miguel", "João"]

# Imprimir a lista
print(nomes)

# Verificar o tipo de dado
print(type(nomes))

# tamannho da lista
 print(nomes)

 #impresao ddo tipos dados
 print(type(nomes))

 # tamanho da lista
 print(len(nomes))

 # imprimir os itens da lista

 print(nomes[0])
 print(nomes[1])
 print(nomes[2])
print(nomes[3])

# Lista de frutas
frutas = ["pêra", "uva", "maçã", "kiwi"]
print(frutas)

# Alterando o elemento que está na posição 1
frutas[1] = "abacate"
print(frutas)

frutas.insert(2, 'morango')
print(frutas)
frutas.insert(5,'chuchu') # nao e fruta
del frutas[5]
print(frutas)
frutas.insert(5, 'melancia')
print(frutas)
print(f'o que e o frutas.index{}')
del frutas[frutas.index('melancia')]
print(frutas)

frutas.remove('kiwi')
print(frutas)
frutas.insert(10,'ameixa')
print()


