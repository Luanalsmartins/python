vc = float(input('Preço das compras R$'))
pagamento = int(input('Para escolher a consição de pagamento digite o respectivo número sendo: \n1 - À vista (dinheiro/cheque);\n2 - Cartão débito;\n3 - Parcelado em 2x;\n4 - Parcelado 3x ou mais.\nQual é a opção? '))

if pagamento == 1:
    total = vc - (vc*0.10)
    print(f'O valor a ser pago é de R${total:.2f}')
elif pagamento == 2:
    total = vc - (vc*0.05)
    print(f'O valor a ser pago é de R${total:.2f}')
elif pagamento == 3:
    print(f'Sua compra será parcelada em 2x de {(vc/2):.2f}')
    print(f'O valor a ser pago é de R${vc:.2f}')
elif pagamento == 4:
    total = vc + (vc*0.20)
    qp = int(input('Quantas parcelas? '))
    vp = total / qp
    print(f'Sua compra será parcelada em {qp}x de R${vp:.2f} COM JUROS.')
    print(f'sua compra de {vc:.2f} vai custar R${total:.2f}')
else:
    print('Opção de pagamento inválida. Tente novamente!')