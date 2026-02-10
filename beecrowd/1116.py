N = int(input())

for i in range(N):
    x, y = input().split()
    x = int(x)
    y = int(y)

    if y == 0:
        print('divisao impossivel')
    elif x > y or y > x:
        divisão = x / y
        print(divisão)
    