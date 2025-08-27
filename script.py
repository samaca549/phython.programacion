# 1. Pedir un número y mostrarlo
texto = input("Escriba un número del 1 al 10: ")
print("Usted escribió:", texto)

# 2. Realizar tabla de multiplicar del número que el usuario ingrese (sin función)
numero = int(input("Digite un número: "))
for i in range(1, 11):
    operacion = i * numero
    print(f"{numero} x {i} = {operacion}")

# 2b. Lo mismo pero con función
numero = int(input("\nDigite otro número para la tabla (con función): "))

def multiplicacion(n):
    for i in range(1, 11):
        operacion = i * n
        print(f"{n} x {i} = {operacion}")

multiplicacion(numero)

# 3. Usar una función para obtener el factorial de un número
numerofactorial = int(input("\nDigite un número para obtener el factorial: "))

def factorial(n):
    operacion = 1
    for i in range(1, n+1):
        operacion = i * operacion
    return operacion

resultado = factorial(numerofactorial)
print(f"El factorial de {numerofactorial} es: {resultado}")
