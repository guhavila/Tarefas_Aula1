quantidade_lampada_Incandescentes = float(input("Quantas lampadas Incandescentes vao ser substituidas?")) #input para receber informaões
potencia_Lampadas = float(input("Qual a potencida de cada lampada Incandescentes?")) #input para receber informaões
lampada_ligada_Horas = float(input("Qual a quantidade de horas que cada lampada Incandescentes fica ligada?")) #input para receber informaões

def economia_diaria(potencia_Lampadas):#função para calcular a economia diaria

    economia = (potencia_Lampadas * 0.2) / 1000 # Calcula a economia diária em kWh
    return economia

economia_dia = economia_diaria(potencia_Lampadas)
print(f"A Economia Diaria é: {economia_dia:.4f} kWh")

def economia_mensal(economia_diaria): #função para calcular a economia mensal

    economia2 = (economia_diaria * 30) # Assume que um mês tem 30 dias
    return economia2

economia_mes = economia_mensal(economia_dia) 
print(f"A economia mensal é {economia_mes:.4f} kWh")

def economia_anual(economia_diaria): #função para calcular a economia anual

    economia3 = (economia_diaria * 365) # Assume um ano com 365 dias
    return economia3

economia_ano = economia_anual(economia_dia)
print(f"A economia anual é {economia_ano:.4f} kWh")


