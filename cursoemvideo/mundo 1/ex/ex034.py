salario = float(input('Digite o valor do salário: '))

if salario > 1250: 
    s_aumentado = salario + (salario*0.10)
    print(f'Seu salaŕio teve um aumento de 10% e agora é R${s_aumentado:.2f}')
else:
    s_aumentado = salario + (salario*0.15)
    print(f'Seu salário teve um aumento de 15% e agora é R${s_aumentado:.2f}')