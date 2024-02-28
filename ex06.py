qtd = 0
soma = 0
media = 0
valor = float(input("Digite um valor: "))

while (valor > 0.0):
    soma = soma + valor
    qtd = qtd + 1

    valor= float(input("Digite um valor: "))

#caso seja inserido um valor negativo, o laço encerra

media = soma/qtd
print("\nTotal da soma: %s" %soma + "\nQuantidade de valores digitados: %s" %qtd +
      "\nMédia dos valores: %s" %media)