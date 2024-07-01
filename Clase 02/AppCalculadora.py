

init = int(input("Presione uno para iniciar la app "))

while init != 0:
    print("Seleccione una opcion:\n 1.Sumar\n 2.Restar\n 3.Multiplicar\n 4.Dividir\n 5.Modulo\n 6.Salir\n")

    sel =  int(input("Seleccione una opcion: "))
    
    num1 = int(input("Seleccione el primer numero: "))
    num2 = int(input("Seleccione el segundo numero: "))
 
    if sel == 1:
        print("Suma")
        suma = num1 + num2
        print("El total de la suma es: ", suma)
    elif sel == 2:
        print("Restar")
        resta = num1 - num2
        print("El total de la resta es: ", resta)
    elif sel == 3:
        print("Multiplicar")
        multi = num1 * num2
        print("El total de la multiplicacion es: ", multi)
    elif sel == 4:
        print("Dividir")
        div = num1 / num2
        print("El total de la divicion es: ", div)
    elif sel == 5:
        print("Modulo")
        mod = num1 % num2
        print("El total de el modulo es: ", mod)
    elif sel == 6:
        init = 0
    else: 
        print("Seleccione una opcion valida")