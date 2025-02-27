# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")

count = 10
while count >= 1:
  print(count, end = " ")
  count -= 1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")

count = 1
suma = 0
while count <= 20:
  if count % 2 == 0:
    suma += count
  count += 1
print(f"La suma de los numeros pares hasta 20 es: {suma}")

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número.
# Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")

numero = int(input("Introduzca un numero entero positivo: "))
factorial = 1
while numero > 0:
  factorial *= numero
  numero -= 1
print(f"El factorial del numero es: {factorial}")

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")

contraseña = input("Introduzca una contraseña: ")
while len(contraseña) < 8:
  print("La contraseña debe tener 8 caracteres")
  contraseña = input("Introduza una contraseña: ")
else:
  print("Contraseña valida")

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

numero = int(input("Introduzca un numero: "))
count = 1
while count <= 10:
  print(f"{numero}x{count} = ", numero * count)
  count += 1

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")

N = int(input("Introduzca un numero entero positivo: "))
numero = 2
while numero <= N:
  es_primo = True
  divisor = 2
  while divisor < numero:
    if numero % divisor == 0:
      es_primo = False
      break
    divisor += 1
  if es_primo:
    print(f"El numero {numero} es primo")
  numero += 1