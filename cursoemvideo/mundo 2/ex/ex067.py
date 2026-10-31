c = tabuada = 1

while True:
    n = int(input('Quer ver a tabuaba de qual valor? '))
    print('-'*50)
    if n < 0:
        break
    for c in range (1, 11):
        print(f'{n} x {c} = {n*c}')
        c += 1
    print('-'*50)
print('Programa tabuada encerrado. Volte sempre!')