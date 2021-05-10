from Refactoring import *


def ABS_Z_N(number: str):  # Абсолютная величина числа
    number = str(number)
    number = number.replace("+", "")
    number = number.replace("-", "")  # Убираем из строки -
    return number


def POS_Z_D(number: str):  # Определение положительности числа
    number = str(number)
    number = number.replace("+", "")
    if number.count("-") == 1:  # Если в строке есть - то оно отрицательное
        return "1"
    if number == "0":  # Если в числе содержиться только 0 то оно равно нулю
        return "0"
    return "2"  # Иначе оно положительное


def MUL_ZM_Z(number: str):  # Умножение целого на -1
    number = str(number)
    number = number.replace("+", "")
    number = "-"+number  # приписываем слева
    number = number.replace("--", "")  # Если минуса 2 то онизаменяются на пустоту
    return number


def TRANS_N_Z(number: str):  # Преобразование натурального в целое
    number = str(number)  # целые числа содержат в себе все натуральные так что любое натуральное принадлежит целым числам
    return number


def TRANS_Z_N(number: str):  # преобразование целого неотрицательного в натуральное
    number = str(number)  # целое неотрицательное = натуральное
    return number


def ADD_ZZ_Z(number1: str, number2: str):  # Сложение целых чисел
    number1 = str(number1)
    number2 = str(number2)
    number1 = number1.replace("+", "")
    number2 = number2.replace("+", "")

    if POS_Z_D(number1) == "1" and POS_Z_D(number2) == "1":  # Если оба числа <0
        number1 = ABS_Z_N(number1)  # Берём модуль от них
        number2 = ABS_Z_N(number2)
        result = ADD_NN_N(number1, number2)  # Складываем их как натуральные
        result = MUL_ZM_Z(result)  # Домножаем на -1
        return result

    if POS_Z_D(number1) == "1" and POS_Z_D(number2) == "2":  # Если первое отрицательное а второе положительное
        number1 = ABS_Z_N(number1)  # берём модуль от первого

        if COM_NN_D(number2, number1) == "2":  # если второе больше первого
            result = SUB_NN_N(number2, number1)  # то вычитаем из второго первое

        elif COM_NN_D(number2, number1) == "0":  # Если они равны то возвращаем 0
            return "0"

        elif COM_NN_D(number2, number1) == "1":  # Если первое больше второго
            result = SUB_NN_N(number1, number2)  # вычитаем из первого второе
            result = MUL_ZM_Z(result)  # домножаем на -1

        return result

    if POS_Z_D(number1) == "2" and POS_Z_D(number2) == "1":   # Если первое положительное а второе отрицательное
        number2 = ABS_Z_N(number2)  # берём модуль от второго

        if COM_NN_D(number2, number1) == "2":  # Если второе больше первого
            result = SUB_NN_N(number2, number1)  # вычитаем из второго первое
            result = MUL_ZM_Z(result)  # домножаем на -1

        elif COM_NN_D(number2, number1) == "0":  # Если они равны то возвращаем 0
            return "0"

        elif COM_NN_D(number2, number1) == "1":  # Если второе меньше первого
            result = SUB_NN_N(number1, number2)  # вычитаем из первого второе

        return result

    if POS_Z_D(number1) == "0":  # Если первое число = 0
        return number2  # Возвращаем второе

    if POS_Z_D(number2) == "0":  # Если второе = 0
        return number1  # возвращаем первое
    if POS_Z_D(number1) == "2" and POS_Z_D(number2) == "2":  # Если оба числа положительны
        return ADD_NN_N(number1, number2)  # Возвращаем их сумму


def SUB_ZZ_Z(number1, number2):  # Вычитание целых чисел
    number1 = str(number1)
    number2 = str(number2)
    number1 = number1.replace("+", "")
    number2 = number2.replace("+", "")

    number2 = MUL_ZM_Z(number2)  # домножаем второе на -1
    return ADD_ZZ_Z(number1, number2)  # Возвращаем их сумму


def MUL_ZZ_Z(number1: str, number2: str):  # Умножение целых чисел
    number1 = str(number1)
    number2 = str(number2)
    count_negatives = 0  # количество отрицательных чисел

    number1 = number1.replace("+", "")
    number2 = number2.replace("+", "")

    if number1 == "0" or number2 == "0":  # Если хоть одно = 0 то возвращаем 0
        return "0"

    if POS_Z_D(number1) == "1":  # Если первое отрицательно
        number1 = ABS_Z_N(number1)  # Берём модуль
        count_negatives += 1  # Записываем что встречено отрицательное

    if POS_Z_D(number2) == "1":  # Если второе отрицательное
        number2 = ABS_Z_N(number2)  # Берём модуль
        count_negatives += 1  # Записываем что встречено отрицательное

    result = MUL_NN_N(number1, number2)  # перемножаем числа

    if count_negatives == 1:  # если было встреченно только одно отрицательное
        result = MUL_ZM_Z(result)  # то домножаем результат на -1

    return result


def DIV_ZZ_Z(number1: str, number2: str):  # Частное от деления целых чисел
    number1 = str(number1)
    number2 = str(number2)
    number1 = number1.replace("+", "")
    number2 = number2.replace("+", "")
    if number2 == "0":  # если делитель 0 возвращаем ошибку
        return "ERROR"
    if number1 == "0":  # Если делимое ноль возвращаем 0
        return "0"
    count_negatives = 0  # Количество отрицательных чисел

    if POS_Z_D(number1) == "1":  # Если первое отрицательное
        number1 = ABS_Z_N(number1)  # Берём модуль
        count_negatives += 1  # Записываем что встреченно отрицательное

    if POS_Z_D(number2) == "1":  # Если второе отрицательное
        number2 = ABS_Z_N(number2)  # Берём модуль
        count_negatives += 1  # Записываем что встреченно отрицательное

    result = DIV_NN_N(number1, number2)  # Берём частное
    if result == "ERROR":  # Если полученная ошибка
        result = "0"  # Возвращаем 0 (Для того что бы в будущем прога не крашилась)
        return result
    if count_negatives == 1:  # если встреченно только одно отрицательное то домножаем результат на -1
        result = MUL_ZM_Z(result)

    return str(result)


def MOD_ZZ_Z(number1: str, number2: str):  # Остаток от деления целых
    number1 = str(number1)
    number2 = str(number2)
    number1 = number1.replace("+", "")
    number2 = number2.replace("+", "")
    if number1 == "0":  # Если делимое ноль возвращаем ноль
        return "0"
    if number2 == "0":  # Если делитель 0 то возвращаем ошибку
        return "ERROR"

    chastnoe = DIV_ZZ_Z(number1, number2)  # Берём частное от этих чисел
    # Возвращаем Разность первого числа и произведения частного на второе
    return SUB_ZZ_Z(number1, MUL_ZZ_Z(chastnoe, number2))
