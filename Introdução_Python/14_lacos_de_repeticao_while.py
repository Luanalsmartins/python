# Laço de repetição executa alguma coisa várias vezes enquanto a condição for verdadeira
# While significa enquanto 
# Se usa i de incrementado 

i = 0

while i < 10: 
    print(i)
    if i % 2 == 1:
        i = i + 2
        continue
    i = i + 1

'''i = 0
    while i < 10: 
    print(i)
    if i >= 2: 
        break # interrompe o laço de repetição mesmo a condição do while sendo verdadeira 
    i = i + 1 '''
    
 
'''i = 0    # Atribuindo valor a variável i
j = 0 

while i < 10 and j < 30: 
    print('Olá, tudo bem?') 
    print('Como vai você?')
    i = i + 1
    j = j + 10'''
