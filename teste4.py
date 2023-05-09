from random import randint

with open('numeros_aleatorios.text','w', encoding= 'utf -8') as fs:
    for n in range(100):
        fs.write(str(randint(1000, 100000)) + '\n')
        
