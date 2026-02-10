idade_start = 0
idade = 0
count = 0

while True:
    idade = int(input())
    if idade >= 0: 
        idade_start += idade
        count += 1

    else: 
        idade_media = idade_start / count
        print(f'{idade_media:.2f}')
        break

