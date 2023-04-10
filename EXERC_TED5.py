#1.R-
for i in range(1000, 2001):
    if i % 11 == 5:
        print(i)

#2.R-

# Laço externo para percorrer de 1 a 10
for i in range(1, 11):
    print(f"Tabuada do {i}:")
    # Laço interno para percorrer de 1 a 10 e mostrar o resultado da multiplicação
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print()  # Pula uma linha para separar as tabuadas

#3.R-

# Criando a lista de amigos
amigos = ["bia", "neto", "Pedro", "ligia"]

# Acessando cada elemento da lista e exibindo o nome de cada amigo
for amigo in amigos:
    print(amigo)

#4.R-

# Solicita que o usuário digite um número
numero = int(input("Digite um número para ver sua tabuada: "))

# Laço para imprimir a tabuada
for i in range(1, 11):
    print(f"{numero} x {i} = {numero*i}")


#5.R-

# Criando a lista de amigos
amigos = ["bia", "neto", "Pedro", "ligia"]


# Percorrendo a lista de amigos e exibindo uma saudação personalizada para cada um
for amigo in amigos:
    print(f"Olá {amigo}, como vai você?")

#6.R-

# Criação da lista de convidados
convidados = ["nattan", "paloma", "denis", "Jennifer", "ligia"]

# Envio dos convites para cada convidado
for convidado in convidados:
    print(f"Olá {convidado}, você está convidado para um jantar em minha casa no próximo sábado!")

# Simulação da desistência de um convidado
print(f"\nInfelizmente, {convidados[1]} não poderá comparecer ao jantar.\n")

# Remoção do convidado que não poderá comparecer e adição de um novo convidado
convidados.remove("ligia")
convidados.append("nattan")

# Exibição dos novos convites
for convidado in convidados:
    print(f"Olá {convidado}, você está convidado para um jantar em minha casa no próximo sábado!")

#7.R-

# Criando a lista de amigos
amigos =  ["bia", "neto", "Pedro", "ligia"]
# Percorrendo a lista de amigos e exibindo uma saudação personalizada para cada um
for amigo in amigos:
    print(f"Olá {amigo}, como vai você?")

