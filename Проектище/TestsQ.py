from RefactoringQ import *
from random import *

print("1 - сокращение дробей")
print("2 - проверка на целое")
print("3 - Преобразование целого в дробное")
print("4 - Преобразование дробного в целое")
print("5 - Сложение дробей")
print("6 - Вычитание дробей")
print("7 - Умножение дробей")
print("8 - деление дробей")

choice = int(input())
ra = int(input("Сколько?"))

for i in range(0, ra):
    chisle1 = randint(-100, 100)
    chisle2 = randint(-100, 100)
    znam1 = randint(-10, 10)
    while znam1 == 0:
        znam1 = randint(-10, 10)
    znam2 = randint(-10, 10)
    while znam2 == 0:
        znam2 = randint(-10, 10)
    drob1 = str(chisle1)+"/"+str(znam1)
    drob2 = str(chisle2)+"/"+str(znam2)
    drob3 = str(chisle1)+"."+str(znam1)
    if choice == 1:
        print(f"{drob1} = {RED_Q_Q(drob1)}")
    if choice == 2:
        print(f"{drob1} = {INT_Q_B(drob1)}")
    if choice == 3:
        print(f"{drob3} = {TRANS_Z_Q(drob3)}")
    if choice == 4:
        pass
    if choice == 5:
        print(f"{drob1} + {drob2} = {ADD_QQ_Q(drob1,drob2)}")
    if choice == 6:
        print(f"{drob1} - {drob2} = {SUB_QQ_Q(drob1, drob2)}")
    if choice == 7:
        print(f"{drob1} * {drob2} = {MUL_QQ_Q(drob1, drob2)}")
    if choice == 8:
        print(f"{drob1} / {drob2} = {DIV_QQ_Q(drob1, drob2)}")
