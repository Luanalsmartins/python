n = int(input('Digite um número para ver o seu fatorial: '))
fatorial = 1

while n > 1:
    print(f'{n} x ', end='')
    fatorial *= n
    n -= 1
    if n == 1:
        print(f'{n} = {fatorial}')