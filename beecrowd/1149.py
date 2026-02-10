'''A, N = map(int, input().split())

while N <= 0:
    N = int(input())

total = 0

for i in range (N):
    total += A + i 

print(f'{total}')'''

# Lê todos os valores de uma vez
entrada = list(map(int, input().split()))

# O primeiro valor é A
a = entrada[0]

# Procurar o primeiro valor válido de N (positivo)
for n in entrada[1:]:
    if n > 0:
        break

total = 0

# Calcula a soma de A + i para i variando de 0 até N-1
for i in range(n):
    total += a + i

# Imprime o resultado final
print(total)
