# Variables
numero = int(input("Introduzca los numeros de su DNI: "))
letrasDNI = "TRWAGMYFPDXBNJZSQVHLCKE"

# Código
numletra = numero % 23
letra = letrasDNI[numletra]
print(f"Su DNI es: {numero}{letra}")

Registro = open("Registro_DNI.txt","a+",encoding="UTF-8")
Registro.write("El DNI introducido es: " + str(numero) + str(letra) + "\n")
Registro.close()

# Luismdelacy
