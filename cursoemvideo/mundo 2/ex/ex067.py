n = 0
c = tabuada = 1

while True:
    n = int(input('Quer ver a tabuaba de qual valor? '))
    print('-'*50)
    if n < 0:
        break
    for c in range (1, 11):
        tabuada = n*c
        print(f'{n} x {c} = {tabuada}')
        c += 1
    print('-'*50)
print('Programa tabuada encerrado. Volte sempre!')