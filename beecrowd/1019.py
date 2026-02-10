def converter_tempo(segundos):
    horas = segundos // 3600
    segundos_restantes = segundos % 3600
    minutos = segundos_restantes // 60
    segundos_finais = segundos_restantes % 60
    return f'{horas}:{minutos}:{segundos_finais}' 

N = int(input())

resultado = converter_tempo(N)
print(resultado)

'''segundos = int(input())

horas = segundos//3600
segundos %= 3600
minutos = segundos//60
segundos %= 60

print(f"{horas}:{minutos}:{segundos}")'''