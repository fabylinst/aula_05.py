palavra = input("Digite uma palavra: ")

# Inverte a string digitada
palavra_invertida = palavra[::-1]

# Verifica se a palavra invertida é igual à palavra original

if palavra == palavra_invertida:
    print("A palavra é um palíndromo!")
else:
    print("A palavra não é um palíndromo.")