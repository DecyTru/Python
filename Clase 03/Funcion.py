


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