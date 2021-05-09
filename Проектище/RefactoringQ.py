from Refactoring import *
from RefactoringZ import *


def razbil_drob(drob: str):
    drob = str(drob)
    if drob.count("/") == 0:
        return drob, "1"
    id = drob.find("/")
    chisl = drob[:id]
    znam = drob[id+1:]

    return chisl, znam


def RED_Q_Q(drob1: str):
    chislitel, znamenatel = razbil_drob(drob1)
    chisle_neg = 0
    znamen_neg = 0

    if POS_Z_D(chislitel) == "1":
        chislitel = ABS_Z_N(chislitel)
        chisle_neg = 1

    if POS_Z_D(znamenatel) == "1":
        znamenatel = ABS_Z_N(znamenatel)
        znamen_neg = 1

    if znamen_neg == 1 and chisle_neg == 1:
        znamen_neg = 0
        chisle_neg = 0
    nod = GCF_NN_N(chislitel, znamenatel)

    chislitel = DIV_ZZ_Z(chislitel, nod)
    znamenatel = DIV_ZZ_Z(znamenatel, nod)

    if chisle_neg == 1 and znamenatel == 1:
        pass
    elif chisle_neg == 1:
        chislitel = "-"+chislitel

    elif znamen_neg == 1:
        znamenatel = "-"+znamenatel

    result = chislitel+"/"+znamenatel
    if znamenatel == "1":
        return chislitel

    if znamenatel == "-1":
        return MUL_ZM_Z(chislitel)

    return result


def INT_Q_B(number: str):
    number = str(number)

    if number.count("/") == 0:
        return "1"

    number = RED_Q_Q(number)
    if number.count("/") == 0:
        return "1"

    return "0"


def TRANZ_Q_Z(number: str):
    if number.count("/") == 0:
        return number

    numerator = ""
    denominator = ""



def TRANS_Z_Q(number: str):

    zero = 0
    if number[0] == "-":
        number = number[1:]
        zero = 1
    if number.count(".") == 0:
        return number+"/1"


    id_dot = number.find(".")

    integer_part = number[:id_dot]
    float_part = number[id_dot+1:]

    if float_part.count("0") == len(float_part):
        return integer_part

    count_zero = 0
    for k in range(0, len(float_part)):
        if float_part[k] != "0":
            break
        else:
            count_zero += 1

    float_denominator = "1"+"0"*len(float_part)

    integer_part = MUL_ZZ_Z(integer_part, float_denominator)
    try:
        integer_part = ADD_QQ_Q(integer_part, float_part)
    except:
        integer_part = "0"

    result = integer_part + "/" + float_denominator
    if zero == 1:
        result = "-"+result
    return result


def ADD_QQ_Q(drob1: str, drob2: str):
    drob1 = str(drob1)
    drob2 = str(drob2)

    if drob1.count(".") == 1:
        drob1 = TRANS_Z_Q(drob1)

    if drob2.count(".") == 1:
        drob2 = TRANS_Z_Q(drob2)

    chisle1, znam1 = razbil_drob(drob1)
    chisle2, znam2 = razbil_drob(drob2)

    nok = LCM_NN_N(znam1, znam2)

    koef1 = DIV_ZZ_Z(nok, znam1)
    koef2 = DIV_ZZ_Z(nok, znam2)

    chisle1 = MUL_ZZ_Z(chisle1, koef1)
    chisle2 = MUL_ZZ_Z(chisle2, koef2)

    res_chisle = ADD_ZZ_Z(chisle1, chisle2)
    res = RED_Q_Q(res_chisle+"/"+nok)
    return res


def SUB_QQ_Q(drob1: str, drob2: str):
    drob1 = str(drob1)
    drob2 = str(drob2)
    if drob1.count(".") == 1:
        drob1 = TRANS_Z_Q(drob1)

    if drob2.count(".") == 1:
        drob2 = TRANS_Z_Q(drob2)
    chisle1, znam1 = razbil_drob(drob1)
    chisle2, znam2 = razbil_drob(drob2)
    nok = LCM_NN_N(znam1, znam2)

    koef1 = DIV_ZZ_Z(nok, znam1)
    koef2 = DIV_ZZ_Z(nok, znam2)
    chisle1 = MUL_ZZ_Z(chisle1, koef1)
    chisle2 = MUL_ZZ_Z(chisle2, koef2)
    res_chisle = SUB_ZZ_Z(chisle1, chisle2)
    res = RED_Q_Q(res_chisle + "/" + nok)
    return res


def MUL_QQ_Q(drob1: str, drob2: str):
    drob1 = str(drob1)
    drob2 = str(drob2)

    if drob1.count(".") == 1:
        drob1 = TRANS_Z_Q(drob1)

    if drob2.count(".") == 1:
        drob2 = TRANS_Z_Q(drob2)

    chisle1, znam1 = razbil_drob(drob1)
    chisle2, znam2 = razbil_drob(drob2)

    res_chisle = MUL_ZZ_Z(chisle1, chisle2)
    res_znam = MUL_ZZ_Z(znam1, znam2)

    res = RED_Q_Q(res_chisle + "/" + res_znam)
    return res


def DIV_QQ_Q(drob1: str, drob2: str):
    drob1 = str(drob1)
    drob2 = str(drob2)

    chisle1, znam1 = razbil_drob(drob1)
    chisle2, znam2 = razbil_drob(drob2)

    res_chisle = MUL_ZZ_Z(chisle1, znam2)
    res_znam = MUL_ZZ_Z(znam1, chisle2)

    res = RED_Q_Q(res_chisle + "/" + res_znam)
    return res


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
    count_negatives = 0
    neg1 = 0
    neg2 = 0
    if chisle1[0] == "-":
        chisle1 = chisle1[1:]
        count_negatives += 1
        neg1 = 1
    if chisle2[0] == "-":
        chisle2 = chisle2[1:]
        count_negatives += 1
        neg2 = 1

    result = COM_NN_D(chisle1, chisle2)
    if count_negatives == 1:
        if neg1 == 1:
            return "1"
        if neg2 == 1:
            return "2"
    if count_negatives == 2:
        if result == 1:
            result = 2
        if result == 2:
            result = 1

    return result # 2-первое больше 1-второе больше первого 0-равны