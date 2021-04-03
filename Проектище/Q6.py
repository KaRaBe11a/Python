from Z8 import MUL_ZZ_Z # Умножение целых
from drob import razbil_drob #разбитие дроби
from Q3 import TRANS_Z_Q # перевод из x.xx в x/y
from Z7 import SUB_ZZ_Z #Вычитание целых

def SUB_QQ_Q(drob_1: str, drob_2: str):
    if (drob_1.count(".") == 1):
        drob_1 = TRANS_Z_Q(drob_1)

    if (drob_2.count(".") == 1):
        drob_2 = TRANS_Z_Q(drob_2)

    a = razbil_drob(drob_1)
    b = razbil_drob(drob_2)

    chisle_1 = MUL_ZZ_Z(a[0], b[1])
    chisle_2 = MUL_ZZ_Z(a[1], b[0])

    sub_chisle = SUB_ZZ_Z(chisle_1, chisle_2)
    sub_znam = MUL_ZZ_Z(a[1], b[1])


    if (int(sub_chisle) % int(sub_znam) == 0):
        return str(int(sub_chisle) / int(sub_znam))

    zxc = str(sub_chisle) + '/' + str(sub_znam)
    return zxc