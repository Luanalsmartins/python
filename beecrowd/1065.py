valores = []

while len(valores) < 5:
    valor = input()
    try: valores.append(float(valor))
    except ValueError:
        print()

contagem_pares = 0
for valor in valores:
    if valor % 2 == 0:
        contagem_pares += 1

print(f'{contagem_pares} valores pares')