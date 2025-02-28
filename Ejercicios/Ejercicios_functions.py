# Ejercicios
# Volver a los ejercicios anteriores
# y convertirlos en funciones
# e intentar utilizar todos los casos y conceptos
# que hemos visto hasta ahora

def imprimir_nums(inicio, fin, paso = 1):
  """Imprime los numeros desde un rango(inicio, fin) sin incluir
  el final, con un paso especifico"""
  # 👆 Este comentario se muestra al poner el cursor sobre la funcion
  # Ademas, defininos el parametro "paso" como 1 para tenerlo por defecto en ese
  # valor en caso de no necesitar que se especifique como argumento al llamar la funcion
  for i in range(inicio, fin, paso):
    print(i, end=" ")
  print()

def factorial(numero):
  """Retorna el factorial del numero"""
  factorial = 1
  for i in range(1, numero+1):
    factorial *= i
  return factorial

def tabla_multiplicar(numero):
  """Muesta la tabla de multiplicar del numero hasta 10"""
  for i in range(1, 11):
    print(f"{numero} x {i} = {i*numero}")

def nums_primos_hasta_N(N):
  """Imprime los numeros primos hasta el N recibido como argumento"""
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

def media_de_una_lista(lista):
  """Se recibe una lista como argumento y retorna la suma de los elementos
  entre la cantidad de estos"""
  suma = 0
  for elemento in lista:
    suma += elemento
  return suma / len(lista)

def max_elemento(lista):
  """Retorna el maximo elemento de una lista"""
  maximo = 0
  for elemento in lista:
    if elemento > maximo:
      maximo = elemento
  return maximo

def filtrar_palabras(lista_de_palabras, tamaño_palabra):
  """Retorna una lista con las palabras que sean mayores al tamaño proporcionado"""
  palabras_filtradas = [palabra for palabra in lista_de_palabras if len(palabra) > tamaño_palabra]
  return palabras_filtradas

def contar_palabras(lista_palabras, letra):
  """Recibe una lista de palabras y una letra y cuenta cuantas palabras
  inician con esa letra"""
  count = 0
  for palabra in lista_palabras:
    if palabra.lower().startswith(letra):
      count += 1
  return count

def suma_en_un_rango(inicio, fin):
  """Calcula la suma de los numeros en el rango especificado sin incluir el fin"""
  suma = 0
  for i in range(inicio, fin):
    suma += i
  return suma

# Ejercicios resueltos con funciones:

# Ejercicio While 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.

imprimir_nums(10, 0, -1)

# Ejercicio While 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número.
# Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.

print(factorial(int(input("Ingrese un numero: "))))

# Ejercicio While 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.

tabla_multiplicar(int(input("Ingrese un numero: ")))

# Ejercicio While 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.

nums_primos_hasta_N(int(input("Ingrese un numero entero: ")))

# Ejercicio For 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.

imprimir_nums(2, 21, 2)

# Ejercicio For 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.

print(media_de_una_lista([10, 20, 30, 40, 50]))

# Ejercicio For 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.

print(max_elemento([15, 5, 25, 10, 20]))

# Ejercicio For 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.

print(filtrar_palabras(["casa", "arbol", "sol", "elefante", "luna"], 5))

# Ejercicio For 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).

letra = input("Introduzca una letra: ").lower()
print(contar_palabras(["casa", "arbol", "sol", "elefante", "luna", "coche"], letra))

# Ejercicio Range 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().

imprimir_nums(1, 11)

# Ejercicio Range 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().

imprimir_nums(1, 21, 2)

# Ejercicio Range 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().

imprimir_nums(5, 51, 5)

# Ejercicio Range 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().

imprimir_nums(10, 0, -1)

# Ejercicio Range 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().

print(suma_en_un_rango(1, 101))

# Ejercicio Range 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().

tabla_multiplicar(int(input("Ingrese un numero: ")))