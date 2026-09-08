Aparelho = input ("aparelho: ")
Potencia = float (input ("Qual a potencia do aparelho?: "))
Tempo = float (input ("Tempo medio de uso: "))


# calculo 

consumo_mensal = (Potencia * Tempo * 30) / 1000
Custo = consumo_mensal * 0.75

#resultado  

print ("\n------consumo estimado------")
print (f"Consumo estimado do aparelho: {consumo_mensal} Kh/mes")
print (f"Custo estimado: R${Custo:.2f}")