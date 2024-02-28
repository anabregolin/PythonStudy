#abre arquivo ou cria, caso não exista ainda
arquivo = open('arqText.txt','w')

arquivo.write('Curso Python \n')
arquivo.write('Aula prática')
arquivo.close()

#lendo arquivo
leitura = open('arqText.txt','r')
print(leitura.read())
leitura.close()