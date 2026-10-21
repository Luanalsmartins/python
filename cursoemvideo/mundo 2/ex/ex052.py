n = int(input('Digite um número e veja se ele é primo: '))
s = 0

for c in range (1, n+1):
    if n%c == 0:
        print('\033[33m', end='')
        s += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
print(f'\n\033[mO número {n} foi divisível {s} vezes.')
if s == 2:
    print(f'{n} é um número primo.')
else:
    print(f'{n} não é um número primo.') 