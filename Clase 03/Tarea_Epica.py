option1 = int(input("\nPROYECTO MARCOS \nSeleccione 1 para iniciar el programa\n"))
if option1 == 1:
    print("Registrate")
    user2 = str(input("Ingresa Un username: "))
    passwo = str(input("Ingresa un password: "))

    username = []

    for i in range(2):
        print("Inicia session")
        user = input("Ingrese el user: ")
        if user == user2:
            for i in range(2):
                passw = input("Ingrese su contraseña: ")
                if passw == passw:
                    print("\n Menu: ")
                    option = int(input("\n Datos [1]\n Calcular su salario neto[2]\n Imprima[3]\n"))
                    if(option == 1):
                        nombre = str(input("Ingrese nombre"))
                        apellido = str(input("Ingrese apellido"))
                        datos = [nombre,apellido]
                    elif(option == 2):
                        salary = float(input("Ingrese el salario"))

                        transpor_aid = 162000

                        rete_healt_discount = 0.04

                        rete_pension_discount = 0.04

                        mininum_legal_salary = 1300000



                        def calculate_healt_discount(salary, rete_healt_discount):
                            heal_discount = salary * rete_healt_discount
                            return heal_discount

                        discount_perheart = calculate_healt_discount(salary, rete_pension_discount)

                        def calculate_pension_discount(salary, discount_perheart):
                            pension_discount = salary * rete_pension_discount
                            return pension_discount


                        discount_perheart = calculate_healt_discount(salary, rete_healt_discount)
                        discount_per_pension = calculate_pension_discount(salary, rete_healt_discount)


                        def calculate_net_salary(salary, discount_perheart, discount_perpension):
                        


                            if salary <  (mininum_legal_salary* 2):
                                net_salary = salary - discount_perheart - discount_perpension + transpor_aid
                            else:
                                net_salary = salary - discount_perheart - discount_perpension 
                            
                            return net_salary 

                        emp_net_salary = calculate_net_salary(salary, discount_perheart, discount_per_pension)

                        print(f"Salario Neto{emp_net_salary}") 
                        break
                    else:
                        print(datos)
                else: 
                    print("Su Contraseña no es valida")

        else: 
            print("Usuario no existente")
else:
    print("Ingresa un valor valido")