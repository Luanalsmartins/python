maior = 0
posicao = 0

for i in range(100):
    N = int(input())
    if N > maior:
        maior = N
        posicao = i + 1
print(maior)
print(posicao)
