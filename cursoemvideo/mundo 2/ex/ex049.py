n = int(input('Digite um número para ver sua tabuada: '))

for c in range (1, 10+1):
    print(f'{n} x {c:2} = {c*n}')