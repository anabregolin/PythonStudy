A = input("Informe um valor para a variável A: ")
B = input("Informe um valor para a variável B: ")

if (A>B):
    aux = A
    A = B
    B = aux
    print("\nO valor da variável A, agora, é: %s" %A)
    print("O valor da variável B, agora, é: %s" %B)
else:
    print("A é menor que B. Não houve alterações.")