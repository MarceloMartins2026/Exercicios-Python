n1 = input("Digite um número: ")
n2 = input("Digite outro número: ")

# Para realizar as operações aritméticas, será
# necessário converter as variáveis n1 e n2 em
# ipos numéricos, que podem ser: int ou float

n1 = int(n1)
n2 = int(n2)

soma = n1 + n2
subtrair = n1 - n2
multiplicar = n1 * n2
dividir = n1 / n2

print(f"A soma entre os números {n1} e {n2} é {soma}")
print(f"A subtração entre os números {n1} e {n2} é {subtrair}")
print(f"A multiplicação entre os números {n1} e {n2} é {multiplicar}")
print(f"A divisão entre os números {n1} e {n2} é {dividir}")

