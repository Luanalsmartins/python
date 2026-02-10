N = int(input())
par = 0
impar = 0
positivo = 0
negativo = 0

for _ in range(N):
    X = int(input())
    if X == 0:
        print('NULL')
        continue
    if X % 2 == 0:
        print('EVEN ', end='')
    if X % 2 != 0:
        print('ODD ', end='')
    if X > 0:
        print('POSITIVE')
    if X < 0: 
        print('NEGATIVE')
