texto = "Quinta"
#  o comando [len]ele mostrar a quantidade de caracteres por exemplo (quinta) tem 6 letras 
# Para ter  o ultimo elemento tenque colocar o len -1
tm= len(texto)
# O comando [tm] ele mostrar o tamanho
print(tm)
print(texto[0])
print(texto[5])
print(texto[6-1])
print(texto[tm-1])
for i in texto:
    print(i)
for i in range(0,5):
    print(texto[i])

print("---------------------------")

# O ultimo numero -1 ele vai diminuino de tras para frente
# p penultimo numero -1 ele vai diminuir a letras quando
for i in range(5,-1,-1):
    print(texto[i])