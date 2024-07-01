


salary = int(input("Ingrese el salario"))


def calculateNetSalary(salary):

    healDiscount = salary * 0.04
    pensionDiscount = salary * 0.04

    netSalary = salary - healDiscount - pensionDiscount

    return netSalary