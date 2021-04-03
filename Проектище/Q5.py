from N14 import LCM_NN_N #НОК натуральных чисел
from Z8 import MUL_ZZ_Z # Умножение целых чисел
from Z6 import ADD_ZZ_Z # Сложение целых чисел
from drob import razbil_drob #Разбиение дроби на составляющие
from Q3 import TRANS_Z_Q # преобразование десятичной в обычную


def ADD_QQ_Q(drob_1: str , drob_2: str):
    if(drob_1.count(".") == 1):
        drob_1 = TRANS_Z_Q(drob_1)
    if(drob_2.count(".") == 1):
        drob_2 = TRANS_Z_Q(drob_2)

    a = razbil_drob(drob_1)
    b = razbil_drob(drob_2)

    chisle1 = str(MUL_ZZ_Z(a[0], b[1]))
    chisle2 = str(MUL_ZZ_Z(a[1], b[0]))

    addChisl = ADD_ZZ_Z(chisle1, chisle2)
    addZnam = MUL_ZZ_Z(a[1], b[1])
    if(int(addChisl)%int(addZnam) == 0):
        return str(int(int(addChisl)/int(addZnam)))

    zxc = str(addChisl)+"/"+str(addZnam)
    return zxc

