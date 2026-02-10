def nota_valida():
    nota = float(input())
    while True:
        if nota < 0 or nota > 10:
            print('nota invalida')
            nota = float(input())
        else: 
            return nota
        

nota1 = nota_valida()
nota2 = nota_valida()
media_nota = (nota1 + nota2) / 2
print(f'media = {media_nota:.2f}')


while True:
    print('novo calculo (1-sim 2-nao)')
    x = int(input())
    if x == 1:
        nota1 = nota_valida()
        nota2 = nota_valida()
        media_nota = (nota1 + nota2) / 2
        print(f'media = {media_nota:.2f}')
    elif x == 2:
        break
