def ordem(x, y):
    x = int(x)
    y = int(y)
    if x > y:
        print(f'Decrescente')
    elif x < y:
        print(f'Crescente')


while True:
    x, y = input().split()
    if x == y:
        break
    ordem(x,y)
