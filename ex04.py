notaA = float(input("Informe a primeira nota: "))
notaB = float(input("Informe a segunda nota: "))

#calculaMédia
mediafinal = (notaA + notaB)/2

#verificacao
if mediafinal >= 8:
    print("Média: %.1f - Aprovado com excelência" %mediafinal)
elif mediafinal >= 7:
    print("Média: %.1f - Aprovado" %mediafinal)
else:
    print("Média: %.1f - Reprovado" %mediafinal)