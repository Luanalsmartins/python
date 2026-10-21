s = 0
cont = 0
for c in range (0, 500, 3):
    if c%2 != 0:
        cont += 1
        s += c
print(f'A soma entre todos os {cont} números ímpares e múltiplos de 3 é: {s}')
print('FIM')