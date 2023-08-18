preço = float(input('qual o preço do produto?'))
desconto = float(input('qual o percentual de desconto do seu produto?'))
porcentagem = desconto/100
preço2 = porcentagem * preço
preçofinal = preço - preço2
print('o seu preço final ficará {0:.2f}' .format(preçofinal))
