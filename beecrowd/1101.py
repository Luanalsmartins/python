def sequencia (m, n):
    soma = 0
    if m > n:
        m, n = n, m
    for i in range (m, n + 1):
        print(f'{i}', end=' ')
        soma += i
    print(f'Sum={soma}')

while True:
    m, n = input().split()
    m = int(m)
    n = int(n)
    if m <= 0 or n <= 0:
        break
    sequencia(m, n)