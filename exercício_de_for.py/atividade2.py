# Faça um programa que leia 5 números e informe a soma e a media dos números

numeros = []


for n in range(5):
    n = int(input("Digite um valor"))
    numeros.append(n)
# exibir os úmeros adicinado
    print(numeros)
# variavel da soma
soma = 0
for i in numeros:
    soma+=i
#exibir a soam
print("A  soma dos valores é:"+str(soma))
print("A media dos valores é:"+str(soma/len(numeros)))











