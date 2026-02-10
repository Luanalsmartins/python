while True:
    x = int(input())
    if x == 0:
        break
    num = 1

    for i in range (x):
        if i == x - 1:
            print(f'{num}', end='')
        else:
            print(f'{num}', end=' ')
        num+=1
    print()