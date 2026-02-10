N = int(input())
num = 1

for i in range (N):
    print(f'{num} {num*num} {num*num*num}')
    print(f'{num} {num*num+1} {num*num*num+1}')
    num += 1
