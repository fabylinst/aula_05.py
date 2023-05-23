def calcula_fatorial(numero):
    if numero < 0:
        return None  # Fatorial não está definido para números negativos
    elif numero == 0 or numero == 1:
        return 1  # O fatorial de 0 e 1 é 1
    else:
        fatorial = 1
        for i in range(2, numero + 1):
            fatorial *= i
        return fatorial

numero = 5
print(calcula_fatorial(numero))

def converte_tempo(tempo_segundos):
    horas = tempo_segundos // 3600
    minutos = (tempo_segundos % 3600) // 60
    segundos = tempo_segundos % 60

    tempo_formatado = "{:02d}:{:02d}:{:02d}".format(horas, minutos, segundos)
    return tempo_formatado
