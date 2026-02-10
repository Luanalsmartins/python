valores = []

while len(valores) < 5:
    valor = input()
    try: valores.append(float(valor))
    except ValueError:
       print()

contagem_pares = 0
contagem_impares = 0
contagem_positivos = 0
contagem_negativos = 0

for valor in valores:
    if valor % 2 == 0:
        contagem_pares += 1
    elif valor % 2 == 1:
        contagem_impares += 1
    
    if valor > 0:
        contagem_positivos += 1
    elif valor < 0:
        contagem_negativos += 1

print(f'{contagem_pares} valor(es) par(es)')
print(f'{contagem_impares} valor(es) impar(es)')
print(f'{contagem_positivos} valor(es) positivo(s)')
print(f'{contagem_negativos} valor(es) negativo(s)')
