from random import choice, randrange
from datetime import datetime

operators = ["+", "-","*","/"]

times = 5

init_time = datetime.now()

correct = 0
incorrect = 0

print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
for i in range(0, times):
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    result = int(input("resultado: "))
    if operator == "+":
        number_3 = number_1 + number_2
    elif operator == "-":
        number_3 = number_1 - number_2
    elif operator == "*":
        number_3 = number_1 * number_2
    else:
        number_3 = number_1 / number_2
    if result == number_3:
        correct += 1
        print("Correcto!")
    else:
        incorrect += 1
        print("Incorrecto!")    
            
end_time = datetime.now()

total_time = end_time - init_time

print(f"\n Tardaste {total_time.seconds} segundos.")
print(f"Tuviste un total de {correct} aciertos y un total de {incorrect} desaciertos")