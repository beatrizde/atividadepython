numeros = []
for v in range(0,5):
    s = int(input("informe o valor:"))
    numeros.append(s)

# adicionar os números a lista

numeros.append(5)

m = numeros[0]
for n in numeros:
    if n > maior:
        m = n
print("O maior número é",maior)