# A soma de dois números  e a divisao entre eles.


def  soma(n1,n2):
    return n1 +n2

def produtos(n1,n2):
    return n1 * n2

def restodivisao(n1,n2):
    return n1 % n2


def separarResultados(texto):
    print("------------------------ O resultado de "+ texto+"--------------------------------")

print("Olá, seja bem vido ao programa de calculos")
separarResultados("soma")
print( "O resultado da soma entre os números 5 e 10 é "+str(soma(5,10)))
separarResultados("Multipçicação")
print("Entre os números 5 e 10 é " +str(produtos(5,10)))
separarResultados("Resto da divisão")
print("Entre os números 5 e 10 é " +str(restodivisao(5,10)))
