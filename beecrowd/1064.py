valores = []

while len(valores) < 6:
    valor = input()
    try:valores.append(float(valor))
    except ValueError:
        print()

contagem_positivos = 0
for valor in valores:
    if valor > 0:
        contagem_positivos += 1

media = 0
for valor in valores:
    if valor > 0:
        media += valor / 4


print(f'{contagem_positivos} valores positivos')
print(f'{media:.1f}')