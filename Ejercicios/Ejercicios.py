###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí

print("\nLuis" + "\nCaracas")

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí

print("\n", type(a), type(a), type(c), type(d), type(e), sep = " -- ") # sep define que tipo de separacion por comas queremos

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
x1 = int(1234)
x2 = float(1234)
print("\n", x1, type(x1), x2, type(x2), int(3.99)) # Siempre se queda con la parte entera sin redondear

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí

nombre = "Luis"
edad = 21
altura = 1.72

print(f"\nHola me llamo {nombre} y tengo {edad} años, mido {altura} metros") #Una forma de imprimir las legible

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

resultado = int(round(3.1416) / 2)
print("\nValor de pi aproximado: ", 3.1416)
print("Valor de pi redondeado: ", round(3.1416))
print("Division entera: ", resultado)