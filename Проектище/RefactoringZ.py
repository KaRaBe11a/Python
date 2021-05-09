from Refactoring import *


def ABS_Z_N(number: str):
    number = str(number)
    number = number.replace("-", "")
    return number


def POS_Z_D(number: str):
    number = str(number)
    if number.count("-") == 1:
        return "1"
    if number == "0":
        return "0"
    return "2"


def MUL_ZM_Z(number: str):
    number = str(number)
    number = "-"+number
    number = number.replace("--", "")
    return number


def TRANS_N_Z(number: str):
    number = str(number)
    return number


def TRANS_Z_N(number: str):
    number = str(number)
    return number


def ADD_ZZ_Z(number1: str, number2: str):
    number1 = str(number1)
    number2 = str(number2)

    if POS_Z_D(number1) == "1" and POS_Z_D(number2) == "1":
        number1 = ABS_Z_N(number1)
        number2 = ABS_Z_N(number2)
        result = ADD_NN_N(number1, number2)
        result = MUL_ZM_Z(result)
        return result

    if POS_Z_D(number1) == "1" and POS_Z_D(number2) == "2":
        number1 = ABS_Z_N(number1)

        if COM_NN_D(number2, number1) == "2":
            result = SUB_NN_N(number2, number1)

        elif COM_NN_D(number2, number1) == "0":
            return "0"

        elif COM_NN_D(number2, number1) == "1":
            result = SUB_NN_N(number1, number2)
            result = MUL_ZM_Z(result)

        return result

    if POS_Z_D(number1) == "2" and POS_Z_D(number2) == "1":
        number2 = ABS_Z_N(number2)

        if COM_NN_D(number2, number1) == "2":
            result = SUB_NN_N(number2, number1)
            result = MUL_ZM_Z(result)

        elif COM_NN_D(number2, number1) == "0":
            return "0"

        elif COM_NN_D(number2, number1) == "1":
            result = SUB_NN_N(number1, number2)

        return result

    if POS_Z_D(number1) == "0":
        return number2

    if POS_Z_D(number2) == "0":
        return number1
    if POS_Z_D(number1) == "2" and POS_Z_D(number2) == "2":
        return ADD_NN_N(number1, number2)

def SUB_ZZ_Z(number1, number2):
    number1 = str(number1)
    number2 = str(number2)

    number2 = MUL_ZM_Z(number2)
    return ADD_ZZ_Z(number1, number2)


def MUL_ZZ_Z(number1: str, number2: str):
    number1 = str(number1)
    number2 = str(number2)
    count_negatives = 0

    if number1 == "0" or number2 == "0":
        return "0"

    if POS_Z_D(number1) == "1":
        number1 = ABS_Z_N(number1)
        count_negatives += 1

    if POS_Z_D(number2) == "1":
        number2 = ABS_Z_N(number2)
        count_negatives += 1

    result = MUL_NN_N(number1, number2)

    if count_negatives == 1:
        result = MUL_ZM_Z(result)

    return result


def DIV_ZZ_Z(number1: str, number2: str):
    number1 = str(number1)
    number2 = str(number2)
    if number2 == "0":
        return "ERROR"
    if number1 == "0":
        return "0"
    count_negatives = 0

    if POS_Z_D(number1) == "1":
        number1 = ABS_Z_N(number1)
        count_negatives += 1

    if POS_Z_D(number2) == "1":
        number2 = ABS_Z_N(number2)
        count_negatives += 1

    result = DIV_NN_N(number1, number2)
    if result == "ERROR":
        result = "0"
        return result
    if count_negatives == 1:
        result = MUL_ZM_Z(result)

    return str(result)


def MOD_ZZ_Z(number1: str, number2: str):
    number1 = str(number1)
    number2 = str(number2)
    if number1 == "0":
        return "0"
    if number2 == "0" or number2 == 0:
        return "ERROR"

    chastnoe = DIV_ZZ_Z(number1, number2)
    return SUB_ZZ_Z(number1, MUL_ZZ_Z(chastnoe, number2))
