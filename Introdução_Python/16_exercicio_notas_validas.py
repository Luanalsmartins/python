# Escreva umm programa que receba as notas de um aluno (0 - 10), 
# caso a nota digitada esteja fora desse intervalo peça para o professor digitar novamente 

while True:
    nota = float(input('Digite a nota do aluno: '))
    if nota >= 0 and nota <= 10:
        print(f'Nota armazenada com sucesso: {nota:.2f}')
        break
    
    print('Nota inválida, digite novamente')