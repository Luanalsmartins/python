alcool = 0
gasolina = 0
diesel = 0

while True: 
    x = int(input())
    if x == 1:
        alcool += 1
    elif x == 2:
        gasolina += 1
    elif x == 3:
        diesel += 1
    elif x == 4:
        break

print('MUITO OBRIGADO')
print(f'Alcool: {alcool}')
print(f'Gasolina: {gasolina}')
print(f'Diesel: {diesel}')