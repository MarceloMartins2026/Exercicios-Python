qtd = 0
for a in range(1950,2027):
    if a % 4 == 0:
        print(f"O ano {a} é bissexto")
        qtd+=1
print("-------------------------------------------")
print(f"A quantidade de anos bissextos é {qtd}")
