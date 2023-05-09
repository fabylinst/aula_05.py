with open('Moby-Dick.txt','r', encoding='utf-8') as fs:
    for linha in fs:
        print(linha.rstrip())

