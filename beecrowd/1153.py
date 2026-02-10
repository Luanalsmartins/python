N = int(input())

resultado = 1
count = 1

while count <= N:
    resultado *= count
    count += 1

print(resultado)