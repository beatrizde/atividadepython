# Faça um programa que verifique se uma letra digitada é "F ou M".
# Conforme a letra escrever.F - Feminino,M _Maculino,sexo invalido
sexo = (input("Digite a letra F ou M para masculino:"))

if sexo == "F" or  sexo == "f":
    print ("Feminino")
elif sexo == "M" or sexo == "m":
    print("masculino")

else:
  print("sexo invalido")

