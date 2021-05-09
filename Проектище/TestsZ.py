from RefactoringZ import *
from math import *
from random import randint
print("1 - Абсолютная величина числа")
print("2 - определение положительности числа")
print("3 - умножение целого на -1")
print("4 - преобразование натурального в целое")
print("5 - Преобразование целого неотрицательного в натуральное")
print("6 - Сложение целых чисел")
print("7 - вычитание целых чисел")
print("8 - умножение целых чисел")
print("9 - частное от деления целого на целое")
print("10 - остаток от деления целого на целое")

choice = int(input())
print("Сколько тестим?")
ra = int(input())
for i in range(0, ra):
    n1 = randint(-100, 100)
    n2 = randint(-10, 10)
    if choice == 1:
        print(f"{n1} abs = {ABS_Z_N(n1)}, А надо {abs(n1)}")
    if choice == 2:
        print(f"{n1}:  {POS_Z_D(n1)}")
    if choice == 3:
        print(f"{n1} * -1 = {MUL_ZM_Z(n1)}, А надо {n1*-1}")
    if choice == 6:
        print(f"{n1}+{n2} = {ADD_ZZ_Z(n1, n2)}, А надо {n1+n2}")
    if choice == 7:
        print(f"{n1}-{n2} = {SUB_ZZ_Z(n1, n2)}, А надо {n1-n2}")
    if choice == 8:
        print(f"{n1}*{n2} = {MUL_ZZ_Z(n1, n2)}, А надо {n1*n2}")
    if choice == 9:
        print(f"{n1}//{n2} = {DIV_ZZ_Z(n1, n2)}" if n1%n2 == 0 else "")
    if choice == 10:
        print(f"{n1}%{n2} = {MOD_ZZ_Z(n1, n2)}")