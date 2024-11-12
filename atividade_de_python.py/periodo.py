periodo = input("Digite M-matutino, V-vespetino ou N-noturno:")
periodo = periodo.lower()

if periodo == "m":
    print("Bom dia!")
elif periodo == "v":
    print("Boa tarde!")
elif periodo == "n":
    print(" Boa norte!")
else:
    print("valor invalido")
