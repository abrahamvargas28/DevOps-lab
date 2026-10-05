print("CALCULADORA SIMPLE")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("3. Dividir")

opcion = input("Seleccione una opción (1 o 2 o 3): ")

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer numero número: "))
numero4 = float(input("Ingrese el tercer numero número: "))

if opcion == "1":
    resultado = numero1 + numero2
    print("El resultado es:", resultado)

elif opcion == "2":
    resultado = numero1 - numero2
    print("El resultado es:", resultado)

elif opcion == "3":
    resultado = numero1 * numero2
    print("El resultado es:", resultado)

elif opcion == "4":
    resultado = numero1 / numero2
    print("El resultado es:", resultado)


else:
    print("Opción incorrecta")