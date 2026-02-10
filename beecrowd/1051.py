salario = float(input())

imposto = 1000.00 * 0.08

if salario >= 0.00 and salario <= 2000.00:
    print('Isento')
elif salario > 2000.00 and salario <= 3000.00:
    total_imposto = (salario - 2000) * 0.08
    print(f'R$ {total_imposto:.2f}')
elif salario > 3000.00 and salario <= 4500.00:
    total_imposto = (salario - 3000.00) * 0.18 + imposto
    print(f'R$ {total_imposto:.2f}')
elif salario > 4500.00:
    total_imposto = ((salario - 4500.00) * 0.28) + (1500.00 * 0.18) + imposto
    print(f'R$ {total_imposto:.2f}')