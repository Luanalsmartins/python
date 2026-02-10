entrada1 = input().split()
cod_peca_1 = int(entrada1[0])
numero_peca_1 = int(entrada1[1])
valor_unit_peca_1 = float(entrada1[2])

entrada2 = input().split()
cod_peca_2 = int(entrada2[0])
numero_peca_2 = int(entrada2[1])
valor_unit_peca_2 = float(entrada2[2])

valor_total = (numero_peca_1 * valor_unit_peca_1) + (numero_peca_2 * valor_unit_peca_2)

print(f'VALOR A PAGAR: R$ {valor_total:.2f}')