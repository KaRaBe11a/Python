from Refactoring import *
from random import *

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
print("10 - ")
print("11 - Частное от деления натурального на натуральное")
print("12 - Остаток от деления натурального на натуральное")
print("13 - НОД натуральных чисел")
print("14 - НОК натуральных чисел")
choice = int(input())
print("Сколько тестим?")
ra = int(input())
for i in range(ra):
    number1 = randint(1, 10000)
    number2 = randint(1, 10)
    number3 = randint(1, 1000)
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
    elif choice == 10:
        print(f"{number1} / {number2} = {DIV_NN_Dk(number1, number2)}")
    elif choice == 11:
        print(f"{number1} / {number2} = {DIV_NN_N(number1, number2)} " if number1 % number2 == 0 else "")
    elif choice == 12:
        print(f"ittaration {i}: {number1} % {number2} = {MOD_NN_N(number1, number2)} А надо {number1 % number2}")
    elif choice == 13:
        print(f"{number1} {number2} НОД = {GCF_NN_N(number1, number2)}")
    elif choice == 14:
        print(f"{number1} {number2} НОК = {LCM_NN_N(number1, number2)}")