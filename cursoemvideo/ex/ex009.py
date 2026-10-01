num = int(input("Digite um número para ver sua tabuada: "))
cont = 1
print('-' * 12)
while (cont <= 10):
    resultado = num*cont
    print("{} X {:2} = {}".format(num, cont, resultado))
    cont += 1
print('-' * 12)
