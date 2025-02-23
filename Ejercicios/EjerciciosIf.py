# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

print("\nEjercicio 1:")
num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))

if num1 > num2:
	print(f"El numero {num1} es mayor que {num2}")
elif num2 > num1:
	print(f"El numero {num2} es mayor que {num1}")
else:
	print(f"Los numeros son iguales")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

print("\nEjercicio 2:")
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
op = input("Ingrese la operacion(+, -, *, /): ")

if op == "+":
	print("La suma es: ", num1 + num2)
elif op == "-":
	print("La resta es: ", num1 - num2)
elif op == "*":
	print("La multiplicación es: ", num1 * num2)
elif op == "/":
	if num2 == 0:
		print("No se puede dividir entre cero")
	else:
		print("El resultado de la division es: ", num1 / num2)
else:
	print("Operación invalida")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

print("\nEjercicio 3:")
anio = int(input("Ingrese un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
	print("El año es bisiesto")
else:
	print("El año no es bisiesto")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

print("\nEjercicio 4:")
edad = int(input("Ingrese una edad: "))

if 0 <= edad <= 2:
	print("Es un bebé")
elif 3 <= edad <= 12:
	print("Es un niño")
elif 13 <= edad <= 17:
	print("Es un adolescente")
elif 18 <= edad <= 64:
	print("Es un adulto")
elif edad >= 65:
	print("Es un adulto mayor")
else:
	print("Edad invalida")