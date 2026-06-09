palavra = input("Digite um texto")
# O comando len(length = Comprimento), ou seja,
# conta a quantidade de caracteres em uma
# coleção
qtd_palavra = len(palavra)
print(qtd_palavra)
cont = 0
while cont < qtd_palavra:
    print(f"A {cont+1}ª letra é {palavra[cont]}")
    cont+=1
