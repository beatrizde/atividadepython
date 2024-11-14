

# Exercício de função quinto

def palindromo(palavra):
    palavra = palavra.lower()
    cp_palavra = palavra
    if cp_palavra==inverter(palavra):
        return "É um palíndromo"
    else: 
        return " Não é um palindromo"
