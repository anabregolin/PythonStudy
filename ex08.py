def calculaMedia(n1, n2):
    media = (n1+n2)/2

    print("\nPrimeira nota: ", nota1, "\nSegunda nota: ", nota2)
    print("Média: ", media, "\nResultado: ", end="") #end = próximo print na mesma linha
    if media >= 7:
        print ("Aprovado")
    else:
        print ("Reprovado")

def lerNota():
    nota = float(input("Insira a nota do aluno(a): "))
    return nota

nota1 = lerNota()
nota2 = lerNota()

media = calculaMedia(nota1, nota2)



