x, y = input().split()
x = int(x)
y = int(y)

num = 1

while num <= y:
    for i in range (x):
        if num <= y:
            if i == x - 1:
                print(f'{num}', end='')
            else:
                print(f'{num}', end=' ')
            num+=1
    print()