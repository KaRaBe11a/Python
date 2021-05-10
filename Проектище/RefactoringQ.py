from Refactoring import *
from RefactoringZ import *


def razbil_drob(drob: str):  # Функция разбитися дроби на числитель и знаменатель
    drob = str(drob)
    if drob.count("/") == 0:  # Если в дроби нет знака деления
        return drob, "1"  # возвращаем всё число как числитель и 1 как знаменатель(это поможет для приведения всех получаемых чисел к одному виду)
    id = drob.find("/")  # Находим номер знака деления в строке
    chisl = drob[:id]  # Берём числитель
    znam = drob[id+1:]  # Берём знаменатель

    return chisl, znam  # Возвращаем их


def RED_Q_Q(drob1: str):  # Сокращение дроби
    chislitel, znamenatel = razbil_drob(drob1)  # Разбиваем дробь на числитель и знаменатель
    chisle_neg = 0  # Отрицателен ли числитель
    znamen_neg = 0  # Отрицателен ли знаменатель


    if POS_Z_D(chislitel) == "1":  # Если числитель отрицательный
        chislitel = ABS_Z_N(chislitel)  # Берём модуль
        chisle_neg = 1  # Запоминаем что он отрицательный

    if POS_Z_D(znamenatel) == "1":  # Если знаменатель отрицательный
        znamenatel = ABS_Z_N(znamenatel)  # Берём модуль
        znamen_neg = 1  # Запоминаем что он отрицателтный

    if znamen_neg == 1 and chisle_neg == 1:  # Если и числитель и знаменатель отрицательные то минусы сократятся
        znamen_neg = 0
        chisle_neg = 0

    if znamen_neg == 1 or chisle_neg == 1:  # Если только одно отрицательное
        if znamenatel == chislitel:  # И они равны по модулю
            return "-1"  # Возвращаем -1
    if znamen_neg == 0 and chisle_neg == 0:   # Если оба положительны
        if znamenatel == chislitel:  # И они равны
            return "1"  # Возвращаем 1

    nod = GCF_NN_N(chislitel, znamenatel)  # Находим НОД числитля и знаменателся

    chislitel = DIV_ZZ_Z(chislitel, nod)  # Делим числитель на НОД
    znamenatel = DIV_ZZ_Z(znamenatel, nod)  # Делим знаменятель на НОД

    if chisle_neg == 1 and znamen_neg == 1:
        pass
    elif chisle_neg == 1:  # если числитель был отрицателным
        chislitel = "-"+chislitel  # Приписываем ему минус

    elif znamen_neg == 1:  # Если знаменатль был отрицательным приписываем ему -
        znamenatel = "-"+znamenatel

    result = chislitel+"/"+znamenatel  # Формируем результирующую строку
    if znamenatel == "1":  # Если знаменатель равен 1
        return chislitel  # возвращаем числитель

    if znamenatel == "-1":  # Если знаменатль равен -1
        return MUL_ZM_Z(chislitel)  # Возвращаем числитель домноженный на -1

    return result


def INT_Q_B(number: str):  # Проверка на целое
    number = str(number)

    if number.count("/") == 0:  # Если нет знака деления значит целое
        return "1"

    number = RED_Q_Q(number)  # Используем функцию сокращения дроби
    if number.count("/") == 0:  # Если она сократиталь до такого что знака деления больше нет значит число целое
        return "1"

    return "0"  # Если число не целое значит оно дробное


def TRANZ_Q_Z(number: str):  # Преобразование дробного в целое
    if number.count("/") == 0:  # Если нет знака деления значит целое
        return number
    chislitel, znamen = razbil_drob(number)  # Разбиваем дробь
    if znamen == "1":  # Если знаменатель = 1 то возвращаем числитель
        return number


def TRANS_Z_Q(number: str):  # Преобразование целого в дробное
    # Сделанно что оно преобразует десятичное в дробное
    zero = 0
    if number[0] == "-":  # Если в начале стоит - то убираем его и запоминаем это
        number = number[1:]
        zero = 1
    if number.count(".") == 0:  # Если в числе нет точки то возвращаем его делённое на 1
        return number+"/1"

    id_dot = number.find(".")  # Находим номер точки в строке

    integer_part = number[:id_dot]  # Записываем целую часть
    float_part = number[id_dot+1:]  # Записываем дробную часть

    if float_part.count("0") == len(float_part):  # Если вся дробная часть состоит из нулей то возвращаем целую часть
        return integer_part

    count_zero = 0  # Кол-во нулей
    for k in range(0, len(float_part)):  # Считаем кол-во нулей до пекрвой цифры
        if float_part[k] != "0":
            break
        else:
            count_zero += 1

    float_denominator = "1"+"0"*len(float_part)  # делаем число равное 1 и (длинна дробной части)нулей

    integer_part = MUL_ZZ_Z(integer_part, float_denominator)  # домножаем целую часть на полученное число
    try:
        integer_part = ADD_QQ_Q(integer_part, float_part)  # прибавляем к целой части дробную часть
    except:  # Защита на случай появления нулей
        integer_part = "0"

    result = integer_part + "/" + float_denominator  # формируем результирующую строку
    if zero == 1:  # Если был - то возвращаем его
        result = "-"+result
    return result


def ADD_QQ_Q(drob1: str, drob2: str):  # Сложение рациональных
    drob1 = str(drob1)
    drob2 = str(drob2)

    if drob1.count(".") == 1:  # Если в первом числе есть точка
        drob1 = TRANS_Z_Q(drob1)  # Приводим к общему виду

    if drob2.count(".") == 1:  # Если во втором числе есть точка
        drob2 = TRANS_Z_Q(drob2)  # Приводим к общему виду

    chisle1, znam1 = razbil_drob(drob1)  # Разбиваем оба числа на числители и знаменатели
    chisle2, znam2 = razbil_drob(drob2)

    nok = LCM_NN_N(znam1, znam2)  # Берём НОК знаменателей

    koef1 = DIV_ZZ_Z(nok, znam1)  # делим нок на каждый знаменатель
    koef2 = DIV_ZZ_Z(nok, znam2)

    chisle1 = MUL_ZZ_Z(chisle1, koef1)  # домножаем числители на полученные числа
    chisle2 = MUL_ZZ_Z(chisle2, koef2)

    res_chisle = ADD_ZZ_Z(chisle1, chisle2)  # Складываем числители
    res = RED_Q_Q(res_chisle+"/"+nok)  # Формируем результирующую строку
    return res


def SUB_QQ_Q(drob1: str, drob2: str):  # Вичитаение рациональных чисел
    drob1 = str(drob1)
    drob2 = str(drob2)
    if drob1.count(".") == 1:  # Если в числе есть точка
        drob1 = TRANS_Z_Q(drob1)  # Приводим к общему виду

    if drob2.count(".") == 1:  # Если в числе есть точка
        drob2 = TRANS_Z_Q(drob2)  # Приводим к общему виду
    chisle1, znam1 = razbil_drob(drob1)  # Разбиваем дроби на числители и знаменатли
    chisle2, znam2 = razbil_drob(drob2)
    nok = LCM_NN_N(znam1, znam2)  # Находим НОК знаменателей

    koef1 = DIV_ZZ_Z(nok, znam1)  # Делим НОК на знаменатели
    koef2 = DIV_ZZ_Z(nok, znam2)

    chisle1 = MUL_ZZ_Z(chisle1, koef1)  # Умножаем числители на полученные числа
    chisle2 = MUL_ZZ_Z(chisle2, koef2)

    res_chisle = SUB_ZZ_Z(chisle1, chisle2)  # Вычитаем числители

    res = RED_Q_Q(res_chisle + "/" + nok)  # Формируем рузультирующую строку
    return res


def MUL_QQ_Q(drob1: str, drob2: str):  # Произведение рациональных чисел
    drob1 = str(drob1)
    drob2 = str(drob2)

    if drob1.count(".") == 1:  # Если в числе есть точка
        drob1 = TRANS_Z_Q(drob1)  # приводим к общему виду

    if drob2.count(".") == 1:  # Если в числе есть тока
        drob2 = TRANS_Z_Q(drob2)  # приводим к общему виду

    chisle1, znam1 = razbil_drob(drob1)  # разбиваем дроби на числители и знаменатели
    chisle2, znam2 = razbil_drob(drob2)

    res_chisle = MUL_ZZ_Z(chisle1, chisle2)  # перемножаем числители и знаменатли
    res_znam = MUL_ZZ_Z(znam1, znam2)

    res = RED_Q_Q(res_chisle + "/" + res_znam)  # Формируем результирующую строку
    return res


def DIV_QQ_Q(drob1: str, drob2: str):  # Деление рациональных чисел
    drob1 = str(drob1)
    drob2 = str(drob2)

    if drob1.count(".") == 1:  # Если в числе есть точка
        drob1 = TRANS_Z_Q(drob1)  # Приводим к общему виду

    if drob2.count(".") == 1:  # Если в числе есть точка
        drob2 = TRANS_Z_Q(drob2)  # Приводим к обшему виду

    chisle1, znam1 = razbil_drob(drob1)  # Разбиваем дроби на числители и знаменатели
    chisle2, znam2 = razbil_drob(drob2)

    res_chisle = MUL_ZZ_Z(chisle1, znam2)  # Перемножаем числитель первого числа на знаменатель второго
    res_znam = MUL_ZZ_Z(znam1, chisle2)  # Перемножаем знаменатель первого на числитель второго

    res = RED_Q_Q(res_chisle + "/" + res_znam)  # Формируем результирующую строк
    return res


def SRAVN_Q(drob_1:str, drob_2:str):  # Сравнение рационалных чисел
    # Приводим рациональное число к общему виду x/y
    if drob_1.count(".") == 1:  # Если в числе есть точка
        drob_1 = TRANS_Z_Q(drob_1)  # Приводим к общему виду
    if drob_2.count(".") == 1:  # Если в числе есть точка
        drob_2 = TRANS_Z_Q(drob_2)  # Приводим к общему виду


    a = razbil_drob(drob_1)  # Разбиваем дроби на числитель и знаменатль
    b = razbil_drob(drob_2)
    chisle1 = MUL_ZZ_Z(a[0], b[1])  # Перемножаем числитель перого на знаменатель второго
    chisle2 = MUL_ZZ_Z(a[1], b[0])  # Перемножаем знаменатль первого на числитель второго
    count_negatives = 0  # Количество отрицаний
    neg1 = 0
    neg2 = 0
    if chisle1[0] == "-":  # Если числитель первого отрицательным
        chisle1 = chisle1[1:]  # убираем минус
        count_negatives += 1  # запоминаем что было отрицательное
        neg1 = 1  # запоминаем что это именно первый числитель
    if chisle2[0] == "-":  # Если числитель второго отрицательный
        chisle2 = chisle2[1:]  # Убираем минус
        count_negatives += 1  # Запоминаем что было отрицательное
        neg2 = 1  # Запоминаем что это именно второй числитель

    result = COM_NN_D(chisle1, chisle2)  # Сравниваем числители
    if count_negatives == 1:  # Если отрицательное одно
        if neg1 == 1:  # Если первое отрицательное
            return "1"  # Значит второе больше
        if neg2 == 1:  # Если второе отрицательное
            return "2"  # Значит первое больше
    if count_negatives == 2:  # Если оба были отрицательные
        if result == 1:  # Меняем результат на противоположный
            result = 2
        if result == 2:
            result = 1

    return result # 2-первое больше 1-второе больше первого 0-равны