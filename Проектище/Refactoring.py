from Dop_Functions_N import *


def COM_NN_D(number1: str, number2: str):  # Сравнение натуральных чисел
    number1 = str(number1)
    number2 = str(number2)

    if len(number1) != len(number2):  # Проверка на длинну что длиннее то и больше
        return "2" if len(number1) > len(number2) else "1"

    for i in range(len(number1)):  # Посимвольная проверка как только что-то разное проверяем и выдаём результат
        if number1[i] != number2[i]:
            return "2" if number1[i] > number2[i] else "1"

    return "0"


def NZER_N_B(number: str):
    number = str(number)
    if number.count("0") == len(number):
        return "1"
    if len(number) != 1:
        return "0"

    return "1" if number == "0" else "0"


def ADD_1N_N(number: str):
    number = str(number)

    number = number[::-1]
    number = list(number)

    number[0], ost = ADD_N_N(number[0], "1")
    if ost == "0":
        number = "".join(number[::-1])
        return number

    for i in range(1, len(number)):
        number[i], ost = ADD_N_N(number[i], ost)
        if ost == "0":
            number = "".join(number[::-1])
            return number
        if i == len(number)-1:
            return "1"+len(number)*"0"


def ADD_NN_N(number1: str, number2: str):
    number1 = str(number1)
    number2 = str(number2)
    number1 = number1.replace("+", "")
    number2 = number2.replace("+", "")
    if len(number2) > len(number1):
        number1, number2 = number2, number1

    if len(number2) != len(number1):
        for i in range(len(number1)-len(number2)):
            number2 = "0"+number2

    number1 = number1[::-1]
    number2 = number2[::-1]

    number1 = list(number1)
    number2 = list(number2)
    number1.append("0")
    ost = "0"

    for i in range(len(number1)-1):
        number1[i], ost = ADD_N_N_N(number1[i], number2[i], ost)
    number1[-1], ost = ADD_N_N(number1[-1], ost)
    if number1[-1] == "0":
        number1[-1] = ""
    number1 = "".join(number1[::-1])
    return number1


def SUB_NN_N(number1: str, number2: str):

    number1 = str(number1)
    number2 = str(number2)

    if COM_NN_D(number1, number2) == "1":
        return "ERROR first number < second number"
    if COM_NN_D(number1, number2) == "0":
        return "0"

    if len(number1) != len(number2):
        for i in range(len(number1) - len(number2)):
            number2 = "0" + number2

    number1 = number1[::-1]
    number2 = number2[::-1]

    number1 += "0"
    number2 += "0"

    number1 = list(number1)
    number2 = list(number2)

    for i in range(len(number1)):
        if number1[i][0] != "-":
            value = COM_NN_D(number1[i], number2[i])
        else:
            value = "1"

        if value == "0":
            number1[i] = "0"

        elif value == "2":
            number1[i] = SUB_N_N(number1[i], number2[i])

        elif value == "1":
            number1[i] = ADD_N_N_bez_ost(number1[i], "10")
            number1[i] = SUB_N_N(number1[i], number2[i])
            number1[i+1] = SUB_N_N(number1[i+1], "1")

    j = len(number1)-1
    if len(number1) > 1:
        while True:
            if number1[j] == "0":
                number1[j] = ""
                j -= 1
            else:
                break

    number1 = "".join(number1[::-1])

    return number1


def MUL_ND_N(number1: str, number2: str):

    if number2 == "0":
        return "0"
    number1 = number1.replace("+", "")
    number2 = number2.replace("+", "")
    number1 = str(number1)
    result = number1
    for i in range(0, int(number2)-1):
        result = ADD_NN_N(result, number1)
    return result


def MUL_Nk_N(number1: str, k: str):

    number1 = str(number1)
    number1 += (k*"0")
    return number1


def MUL_NN_N(number1: str, number2: str):
    number1 = str(number1)
    number2 = str(number2)

    number2 = number2[::-1]

    tmp = list()

    for i in range(0, len(number2)):
        tmp.append(MUL_ND_N(number1, number2[i]))
        tmp[i] = MUL_Nk_N(tmp[i], i)

    result = "0"

    for i in tmp:
        result = ADD_NN_N(result, i)

    return result


def SUB_NDN_N(number1: str, number2: str, number3: str):
    number1 = str(number1)
    number2 = str(number2)
    number3 = str(number3)

    number2 = MUL_ND_N(number2, number3)
    number1 = SUB_NN_N(number1, number2)

    return number1


def DIV_NN_Dk(number1: str, number2: str):
    number1 = str(number1)
    number2 = str(number2)
    result = ""
    ost = ""
    i = 0

    if COM_NN_D(number1, number2) == "1":
        return "ERROR"

    if COM_NN_D(number1, number2) == "0":
        return "1"

    while i < len(number1):
        tmp = ost + number1[i]
        i += 1
        while COM_NN_D(tmp, number2) == "1" and i < len(number1):
            tmp += number1[i]
            i += 1
        count = "0"
        while COM_NN_D(tmp, number2) != "1":
            tmp = SUB_NN_N(tmp, number2)
            count = ADD_1N_N(count)
        result += str(count)

    number = MUL_Nk_N(result[0], len(result)-1)
    return number


def DIV_NN_N(number1: str, number2: str):
    number1 = str(number1)
    number2 = str(number2)
    result = ""
    ost = ""
    i = 0

    if COM_NN_D(number1, number2) == "1":
        return "ERROR"

    if COM_NN_D(number1, number2) == "0":
        return "1"

    count = 0
    while COM_NN_D(number1, number2) == "2":
        number1 = SUB_NN_N(number1, number2)
        count += 1
    count += 1
    return str(count)
"""
    while i < len(number1):
        tmp = ""
        if ost != '0':
            tmp = ost

        tmp += number1[i]
        if number1[i] == "0" and number1[i] == tmp:
            result += "0"
            tmp = ""

        i += 1

        while COM_NN_D(tmp, number2) == "1" and i < len(number1):
            tmp += number1[i]
            if result != "":
                result += "0"

            i += 1

        count = ""
        if tmp != "0" and tmp != "":
            while True:
                if len(tmp) > 0:
                        if tmp[0] == "0" and len(tmp) > 0:
                            tmp = tmp[1:]
                        else:
                            break
                else:
                    break
        if i == len(number1) and COM_NN_D(tmp, number2) == "1":
            result += "0"
            return result

        while COM_NN_D(tmp, number2) != "1":
            tmp = SUB_NN_N(tmp, number2)
            count += "1"

        ost = tmp
        if len(count) != 0:
            result += str(len(count))

    return result
"""



def MOD_NN_N(number1: str, number2: str):
    number1 = str(number1)
    number2 = str(number2)
    if number2 == "1":
        return "0"

    chastnoe = DIV_NN_N(number1, number2)
    if chastnoe == "ERROR":
        return chastnoe
    return SUB_NN_N(number1, MUL_NN_N(chastnoe, number2))


def GCF_NN_N(number1: str, number2: str):
    number1 = number1.replace("-", "")
    number2 = number2.replace("-", "")
    if number1 == number2:
        return "1"
    elif number1 == "0":
        return "1"
    elif number2 == "0":
        return "1"
    while COM_NN_D(number1, number2) != "0":
        if COM_NN_D(number1, number2) == "2":
            number1 = SUB_NN_N(number1, number2)
        else:
            number2 = SUB_NN_N(number2, number1)
    return number1


def LCM_NN_N(number1: str, number2: str):
    number1 = number1.replace("-", "")
    number2 = number2.replace("-", "")
    return DIV_NN_N(MUL_NN_N(number1, number2),GCF_NN_N(number1, number2))
