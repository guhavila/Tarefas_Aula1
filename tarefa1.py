salário = float(input('qual o seu salário:'))
vendas = float(input('quanto vc ganhou em venda:'))
comissão = vendas * 0.06
saláriofinal = comissão + salário
print('seu salário com uma comissão de 6 por cento, ficaria:{0:.2f}' .format(saláriofinal))

