from Refactoring import *
from random import *
from Dop_Functions_N import ADD_N_N_N
from Dop_Functions_N import ROFLAN
from time import time
ROFLAN()
print("Шо тестим?")
print("1 - Сравнение натуральных чисел")
print("2 - Являеться ли число 0")
print("3 - Добавление к натуральномк числу 1")
print("4 - Сложение двух натуральных")
print("5 - Вычитание из одного натурального другого")
print("6 - Умножение натурального на число")
print("7 - Умножение натурального на 10^k")
print("8 - Умножение натурального на натуральное")
print("9 - Вычитание из натурального другого натурального умноженного на цифру для случая с неотрицательным результатам")
choice = int(input())
print("Сколько тестим?")
ra = int(input())
for i in range(ra):
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    number3 = randint(1, 10)
    if choice == 1:
        print(f"Первое число {number1} Второе число {number2} результат сравнения {COM_NN_D(number1, number2)}")
    elif choice == 2:
        print(f"Являеться ли {number1} нулём {NZER_N_B(number1)}")
    elif choice == 3:
        print(f"{number1} + 1 = {ADD_1N_N(number1)}")
    elif choice == 4:
        print(f"{number1} + {number2} = {ADD_NN_N(number1, number2)}")
    elif choice == 5:
        print(f"{number1} - {number2} = {SUB_NN_N(number1, number2)}   А надо {number1-number2}")
    elif choice == 6:
        print(f"{number1} * {number2} = {MUL_ND_N(number1, number2)} А надо {number1 * number2}")
    elif choice == 7:
        print(f"{number1} * 10^{number2} = {MUL_Nk_N(number1, number2)} А надо {number1 * 10**number2}")
    elif choice == 8:
        print(f"{number1} * {number2} = {MUL_NN_N(number1, number2)} А надо {number1 * number2}")
    elif choice == 9:
        print(f"{number1} - {number2}*{number3} = {SUB_NDN_N(number1, number2, number3)} А надо {number1 - number2*number3}")