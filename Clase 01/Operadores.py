

num1 = int(input("Agregue el primer numero"))

num2 = int(input("Agregue el segundo numero"))

sum = num1 + num2
rest = num1 - num2
mult = num1 * num2
div = num2 / num1
mod = num2 % num1

print(f"\n el resultado de la suma es: {sum} \n el resultado de la resta es: {rest} \n el resultado de la suma es: {mult} \n el resultado de la suma es: {div} \n el resultado de la suma es: {mod} \n" )

# Operadores de comparacion

greatest_than = num1 > num2
less_than = num2 < num1
great_equal = num1 >= num2
less_equal = num2 <= num1
equal = num1 == num2
not_equal = num2 != num1

print(greatest_than, less_than, great_equal, less_equal, equal, not_equal)

# Operadores Lógicos and, or , not



is_true = False and True

print(is_true)

is_false = False or True

print = (is_false)

# Operadores de Asignacion = , += , -= , *= , /=

num1 = num1 + num2

num2 += num1

#Jerarquia de operadores

"""

    1. ()
    2. ^ , rad
    3. * , / , %
    4. + , -
    5. > , < , >= , <= , == , !=
    6. = , += , -= , *= , /=

"""