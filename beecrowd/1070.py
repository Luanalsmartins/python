x = int(input())

contagem_impares = 0

while contagem_impares < 6:
    if x % 2 != 0:
        print(x)
        x += 2
    else:
        x += 1
        print(x)
        x += 2
    contagem_impares += 1