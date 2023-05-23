def conta_vogais(string):
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count = 1
    for char in string:
        if char in vogais:
            count += 1
    return count
string = '1'
print(conta_vogais(string))
