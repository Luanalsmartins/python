#------------------------ MANIPULANDO TEXTO ------------------------#
frase = 'Curso em video Python' 

# FATIAMENTO #
print(frase[9]) #Identifica o caractere número 9 
print(frase[9:13]) #Identifica os caracteres de 9 a 12 
print(frase[9:21]) #Identifica os caracteres de 9 a 20
print(frase[9:21:2]) #Identifica os caracteres de 9 a 20, mostrando 1 a cada 2 caracteres
print(frase[:5]) #Identifica os caracteres do começo ao 5 
print(frase[15:]) #Identifca os caracteres de 15 até o final 
print(frase[9::3]) #Identifica os caracteres de 9 até o final, mostrando 1 a cada 3 caracteres

# ANÁLISE #
print(len(frase)) #Mostra quantos caracteres a string tem 
print(frase.count('o')) #Mostra quantos caracteres 'o' tem na string 
print(frase.count('o',0,13)) #Mostra quantos caracteres 'o' tem na string do caractere 0 ao 12
print(frase.find('deo')) #Mostra em qual posição começou o 'deo'
print(frase.find('Android')) #Quando não encontra na frase, aparece o valor -1
print('Curso' in frase) #Retorna True ou False 

# TRANSFORMAÇÃO #
print(frase.replace('Python', 'Android')) #Substitui uma palavra existente na frase por outra palavra 
print(frase.upper()) #Método que transforma todas as letras em maiúsculas
print(frase.lower()) #Método que transforma todas as letras em minúsculas
print(frase.capitalize()) #Todos os caracteres ficam minúsculos menos a primeira letra
print(frase.title()) #Todas as primeiras letras ficarão em maiúsculo (letras que vem depois dos espaços)

frase = '   Aprenda Python  '
print(frase.strip()) #Remove os espaços em branco no começo e no final da frase
print(frase.rstrip()) #Remove somente os espaços em branco do final da frase
print(frase.lstrip()) #Remove somente os espaços em branco do começo da frase

frase = 'Curso em video Python' 

# DIVISÃO #
print(frase.split()) #Divide as palavras da frase gerando uma lista com elas separadas 
frase_separada = frase.split()
print(frase_separada[0]) #Mostra a primeira palavra da lista
print(frase_separada[2][3]) #Mostra a quarta letra da palavra na posição 2 da lista 

# JUNÇÃO #
print('-'.join(frase_separada)) #Junta a frase com um '-' entre as palavras