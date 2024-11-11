num1= float(input("Digite o primeiro número:"))
num2= float(input("Digite o segundo número:"))
num3= float(input("Digite o terceiro número:"))

if  num1 >= num2 > num3:
    print(f"maior numero: {num1}")
elif num2 > num1:
    print(f"o maior número:{num2}")
elif num3 > num2:
    print(f"o maior número:{num3}")
    
else:
    print(" Qual é o maior número")