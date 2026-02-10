# Escreva um programa onde o usuário digite duas notas e ele mostre a média dass duas notas

# Solicita as notas e converte para float 
Nota1 = float(input ("Digite a nota do aluno 1: "))
Nota2 = float(input ("\nDigite a nota do aluno 2: "))

# Calcula a média
media = (Nota1 + Nota2) / 2 

# Exibe a média das notas com duas casas decimais 
print(f'A média das notas é: {media:.2f}')