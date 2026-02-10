N = int(input())


for i in range(N):
    a, b, c = input().split()
    a = float(a)
    b = float(b)
    c = float(c)
    media_ponderada = (a*2 + b*3 + c*5) / 10
    print(f'{media_ponderada:.1f}')