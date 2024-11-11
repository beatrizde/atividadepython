alimentos = ["Maça","Arroz","Feijão"]
categoria = ("Grão","Frutas","Legumes")
pessoa = {"Nome":"Paula","idade":"38","Altura":"1.65"}

print(alimentos)
print(type(alimentos))
print(len(alimentos))
# adicionar mais um alimento
alimentos.append("Macarrão")
print(alimentos)
print(len(alimentos))


print(categoria)
print(type(categoria))
print(len(categoria))

print(pessoa)
print(type(pessoa))
print(len(pessoa))
# Adicionar um item a pessoa
# adicionar uma nova chave com seu respecytivo valor 
# está sendo adicionado a chave email com o valor 
# email da pessoa
pessoa["email"]="paula@gmail.com"
print(pessoa)
print(len(pessoa))


