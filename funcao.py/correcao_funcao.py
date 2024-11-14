# Exercicio  de funções
def soma(numero1,numero2):
    return numero1 + numero2




# Exercício de função dois
def convertercCelFah(tempCelsius):
    fah = 1.8 * tempCelsius + 32
    return fah




# Exercio de função três 
def parimpar(numero):
    if numero % 2 == 0:
        return"par"
    else:
        return "impar"
    
# Exercício de função  quatro 
def inverter(texto):
    tam = len(texto)
    # Criar uma variavel que devolve o texto invertido
    txt_invertido=""
    for i in range(tam-1,-1,-1):
        txt_invertido += texto[i]
    return txt_invertido


# Exercício de função quinto
def palindromo(palavra):
    palavra = palavra.lower()
    cp_palavra = palavra
    if cp_palavra==inverter(palavra):
        return "É um palíndromo"
    else: 
        return " Não é um palindromo"

# Exercicio de função 6
def media(lista_numeros):
    resultado =0
    for i in lista_numeros:
        resultado += i
    return resultado / len(lista_numeros)


#exercicio de função 7
def lista_pares(lista_numeros):
    lst_pares = []
    for i in lista_numeros:
        if i % 2 == 0:
            lst_pares.append(i)
    return lst_pares

