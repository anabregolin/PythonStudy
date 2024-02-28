print('Hello World!')

nome1 = input('Insira o seu nome: ')
idade1 = int(input('Insira a sua idade: '))

nome2 = 'ana'
idade2 = 20

comparacao1 = nome2 == nome1
comparacao2 = idade1 == idade2

print("\nNome %s" %nome1 + " Idade: %d" %idade1 +
      "\n\nO nome condiz com a constante 'ana'?: %r" %comparacao1 +
      "\nA idade condiz com a constante '20'?: %r" %comparacao2)

if comparacao1 == True and comparacao2 == True:
    print("\n- Ambas condições são equivalentes às constantes.")
elif comparacao1 == False and comparacao2 == False:
    print("\n- Ambas condições são divergentes às constantes.")
else:
    print("\n- Apenas uma condição é equivalente às constantes.")
