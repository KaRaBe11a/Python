from Z8 import MUL_ZZ_Z # Умножение целых чисел
from Z6 import ADD_ZZ_Z # Сложение целых чисел
from drob import razbil_drob #Разбиение дроби на составляющие
from Q3 import TRANS_Z_Q # преобразование десятичной в обычную
from N1_12 import COM_NN_D # сравнение натуральных чисел

def SRAVN_Q(drob_1:str, drob_2:str):
    # Приводим рациональное число к общему виду x/y
    if(drob_1.count(".") == 1):
        drob_1 = TRANS_Z_Q(drob_1)
    if(drob_2.count(".") == 1):
        drob_2 = TRANS_Z_Q(drob_2)

    a = razbil_drob(drob_1)
    b = razbil_drob(drob_2)
    chisle1 = MUL_ZZ_Z(a[0], b[1])
    chisle2 = MUL_ZZ_Z(a[1], b[0])
    result = COM_NN_D(int(chisle1), int(chisle2))
    return result # 2-первое больше 1-второе больше первого 0-равны