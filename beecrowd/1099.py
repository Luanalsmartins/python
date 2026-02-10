def soma_impares(x, y):
    soma = 0
    for i in range(x + 1, y):
        if i % 2 != 0:
            soma += i
    return soma

N = int(input())

for i in range(N):
    x, y = input().split()
    x = int(x)
    y = int(y)
    if x > y:
        x,y = y,x
    soma = soma_impares (x, y)
    print(soma)