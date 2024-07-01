

print("Seleccione una opcion:\n 1.Sumar\n 2. Restar\n 3.Multiplicar\n 4.Dividir\n 6.Modulo")

sel =  int(input("Seleccione una opcion: "))
num1 = int(input("Seleccione el primer numero: "))
num2 = int(input("Seleccione el segundo numero: "))


if sel == 1:
    print("Suma")
    suma = num1 + num2
    print(f"El total de la suma: ", suma)
elif sel == 2:
    print("Restar")
    resta = num1 - num2
    print("El total de la resta: ", resta)
elif sel == 3:
    print("Multiplicar")
    multi = num1 * num2
    print("El total de la multiplicacion: ", multi)
elif sel == 4:
    print("Dividir")
    div = num1 / num2
    print("El total de la divicion: ", div)
elif sel == 5:
    print("Modulo")
    mod = num1 % num2
    print("El total de el modulo : ", mod)
else: 
    print("Seleccione una opcion valida")