N = int(input()) # quantidade de valores que serão lidos

dentro_intervalo = 0
fora_intervalo = 0

for _ in range(N):
    X = int(input())
    if 10 <= X <= 20:
        dentro_intervalo += 1
    else:
        fora_intervalo +=1

print(f'{dentro_intervalo} in')
print(f'{fora_intervalo} out')