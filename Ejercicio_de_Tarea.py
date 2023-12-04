# Este programa le pedira al usuario ingresar un año y el programa le dira si el año es bisiesto o no

print("----------------------------COMPROBADOR DE AÑOS BISIESTOS---------------------")

# ENTRADA

año = int(input("Escriba un año y le dire si es bisiesto: "))

# SALIDA

if año % 4 != 0:
    print(f"El año {año} no es bisiesto, porque no es multiplo de 4")
elif año % 4 == 0 and año % 100 != 0:
    print(f"El año {año} es bisiesto, porque es multiplo de 4 y no es multiplo de 100")
elif año % 100 == 0 and año % 400 != 0:
    print(f"El año {año} no es bisiesto, porque es multiplo de 100 y no es multiplo de 400")
else:
    print(f"El año {año} es bisiesto, porque es multiplo de 400")

