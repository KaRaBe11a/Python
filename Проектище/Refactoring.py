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
    if number.count("0") == len(number): # Если колиство 0 равно длинне
        return "1"
    if len(number) != 1: # Если длинна не нулевая
        return "0"

    return "1" if number == "0" else "0" # если в числе есть только 0


def ADD_1N_N(number: str):  # Добавление 1 к натуральному
    number = str(number)

    number = number[::-1]  # Переворачиваем число
    number = list(number)   # Преобразуем из строки в массив

    number[0], ost = ADD_N_N(number[0], "1")   # Добавляем к 1 числу единицу
    if ost == "0":   # Если остаток 0 то переворачиваем и возвращаем
        number = "".join(number[::-1])
        return number

    for i in range(1, len(number)):   # Если остаток не 0 идём по всему числу
        number[i], ost = ADD_N_N(number[i], ost)   # прибавляем к текущей цифре 1
        if ost == "0":   # Если остаток 0 то переворачиваем и возвращаем
            number = "".join(number[::-1])
            return number
        if i == len(number)-1:   # Если дошли до конца(значит было просто какое-то кол-во 9ок то возвращаем 1 + длинна числа нулей)
            return "1"+len(number)*"0"


def ADD_NN_N(number1: str, number2: str):  # Сложение натуральных
    number1 = str(number1)
    number2 = str(number2)
    number1 = number1.replace("+", "")  # Убираем начальные знаки (Нужно для работы в полиномах)
    number2 = number2.replace("+", "")
    if len(number2) > len(number1):   # если длинна второго больше первого то меняем местами для удобства
        number1, number2 = number2, number1

    if len(number2) != len(number1):  # Если длинны не равны то докидываем во второе нули
        for i in range(len(number1)-len(number2)):
            number2 = "0"+number2

    number1 = number1[::-1]  # Переворачиваем числа для удобства
    number2 = number2[::-1]

    number1 = list(number1)  # преобразуем строки в массивы
    number2 = list(number2)
    number1.append("0")  # добавляем в первое число 0 на случай если количество цифр увеличиться
    ost = "0"

    for i in range(len(number1)-1):  # Идём по длинне числа
        number1[i], ost = ADD_N_N_N(number1[i], number2[i], ost)  # Складываем цифру с первого числа и цифру со второго числа и остаток запоминая остаток
    number1[-1], ost = ADD_N_N(number1[-1], ost)  # Добавляем к последней цифре остаток
    if number1[-1] == "0":  # Если остаток получился нулевым
        number1[-1] = ""  # то убираем запасной символ
    number1 = "".join(number1[::-1])  # переворачиваем получившееся число и возвращаем его
    return number1


def SUB_NN_N(number1: str, number2: str):   # вычитание натуральных чисел

    number1 = str(number1)
    number2 = str(number2)

    if COM_NN_D(number1, number2) == "1":  # Если первое меньше второго
        return "ERROR first number < second number"  # Возвращаем ошибку
    if COM_NN_D(number1, number2) == "0":  # Если числа равны то возвращаем 0
        return "0"

    if len(number1) != len(number2):  # если длинны чисел неравны то добавляем ко второму числу нули до длинны первого
        for i in range(len(number1) - len(number2)):
            number2 = "0" + number2

    number1 = number1[::-1]   # Переворачиваем числа для удобства
    number2 = number2[::-1]

    number1 += "0"  # Добавляем на всякий случай 0 в конец что бы не выйти за пределы массива
    number2 += "0"

    number1 = list(number1)  # Преобразуем строку в массив
    number2 = list(number2)

    for i in range(len(number1)):  # Идём по длинне массива
        if number1[i][0] != "-":  # Если в начале не стоит -
            value = COM_NN_D(number1[i], number2[i])  # Сравниваем два числа
        else:
            value = "1"

        if value == "0":  # Если числа одинаковые то записываем 0
            number1[i] = "0"

        elif value == "2":  # Если первое больше второго вычитаем второе из первого
            number1[i] = SUB_N_N(number1[i], number2[i])

        elif value == "1":  # Если второе больше первого
            number1[i] = ADD_N_N_bez_ost(number1[i], "10")  # Добавляем к первому 10
            number1[i] = SUB_N_N(number1[i], number2[i])  # вычитаем из первого второе
            number1[i+1] = SUB_N_N(number1[i+1], "1")  # вычитаем из следующего 1

    j = len(number1)-1  # номер последнего символа
    if len(number1) > 1:  # Если длинна получившегося числа > 1
        while True:
            if number1[j] == "0":  # Идём с последнего числа удаляем ненужные нули
                number1[j] = ""
                j -= 1
            else:
                break

    number1 = "".join(number1[::-1])  # Переворачиваем рузультат и возвращаем его

    return number1


def MUL_ND_N(number1: str, number2: str):  # Умножение натурального на цифру
    number1 = str(number1)
    number2 = str(number2)
    if number2 == "0":  # Если цифра = 0 то возвращаем 0
        return "0"
    number1 = number1.replace("+", "")  # Удаляем начальные знаки(Нужно для работы с многочленами)
    number2 = number2.replace("+", "")
    number1 = str(number1)
    result = number1
    for i in range(0, int(number2)-1):  # циклом складывем 1 число столько раз на сколько надо умножить
        result = ADD_NN_N(result, number1)
    return result


def MUL_Nk_N(number1: str, k: str):  # Умножение натурального на 10^k
    number1 = str(number1)
    number1 += (int(k)*"0")  # припысаем к числу справа k нулей
    return number1


def MUL_NN_N(number1: str, number2: str):  # Умножение натурального числа на натуральное
    number1 = str(number1)
    number2 = str(number2)

    number2 = number2[::-1]  # Переворачиваем второе число

    tmp = list()

    for i in range(0, len(number2)):  # идём по длинне второго числа
        tmp.append(MUL_ND_N(number1, number2[i]))  # умножаем первое число на каждую цифру второго числа
        tmp[i] = MUL_Nk_N(tmp[i], i)  # умножаем полученное на 10^номера цифры на которую умножали

    result = "0"

    for i in tmp:  # складываем получившиеся числа
        result = ADD_NN_N(result, i)

    return result


def SUB_NDN_N(number1: str, number2: str, number3: str):  # Вычитание из натурального другого натурального домноженного на цифру
    number1 = str(number1)
    number2 = str(number2)
    number3 = str(number3)

    number2 = MUL_ND_N(number2, number3)  # Умножаем второе на третье
    number1 = SUB_NN_N(number1, number2)  # Вычитаем из первого то что получилось

    return number1


def DIV_NN_Dk(number1: str, number2: str):  # Вычисление первой цифры деления большего натурального на ментшее
    number1 = str(number1)
    number2 = str(number2)
    result = ""
    ost = ""
    i = 0

    if COM_NN_D(number1, number2) == "1":  # Если первое меньше второго выдаем ошибку
        return "ERROR"

    if COM_NN_D(number1, number2) == "0":  # Если числа одинаковые то возвращаем 1
        return "1"

    while i < len(number1):  # идём по длинне первого числа
        tmp = ost + number1[i]  # к остатку полученному на прошлом ходу прибавлем следующее число(конкатенация)
        i += 1
        while COM_NN_D(tmp, number2) == "1" and i < len(number1):  # Если получившееся число меньше делителя
            tmp += number1[i]  # прибавляем следующую цифру из делимого (конкатенация)
            i += 1
        count = "0"
        while COM_NN_D(tmp, number2) != "1":  # пока полученное число >= делителю
            tmp = SUB_NN_N(tmp, number2)  # вычитаем из полученного делитель
            count = ADD_1N_N(count)  # счётчик которы считает сколько раз вычли
        result += str(count)  # это хранит сколько раз вычли

    number = MUL_Nk_N(result[0], len(result)-1)  # Домножаем
    return number


def DIV_NN_N(number1: str, number2: str):  # Частное от деления натурального на натуральное
    number1 = str(number1)
    number2 = str(number2)
    result = ""
    ost = ""
    i = 0

    if COM_NN_D(number1, number2) == "1":  # Если первое число меньше второго то возвращаем ошибку
        return "ERROR"

    if COM_NN_D(number1, number2) == "0":  # Если числа равны то возвращаем единицу
        return "1"

    count = 0
    while COM_NN_D(number1, number2) != "1":  # пока первое число больше второго
        number1 = SUB_NN_N(number1, number2)  # вычитаем из первого второе
        count += 1  # Считаем сколько раз мы это сделали
    return str(count)
"""
Это были попытки сделать красиво но что-то пошло не по плану и я уже не понимаю что тут происходит
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



def MOD_NN_N(number1: str, number2: str):  # Остаток от делени натурального на натуральное
    number1 = str(number1)
    number2 = str(number2)
    if number2 == "1":  # если второе число = 1 то возвращаем 0
        return "0"

    chastnoe = DIV_NN_N(number1, number2)  # берём частное от деления первого натурального на второе
    if chastnoe == "ERROR":  # Если произошла ошибка возвращаем её
        return chastnoe
    print(number1, chastnoe, number2)
    print(number1, MUL_NN_N(chastnoe, number2))
    return SUB_NN_N(number1, MUL_NN_N(chastnoe, number2))  # Если всё ок то вычитаем из первого числа произведение частного на второе число


def GCF_NN_N(number1: str, number2: str):  # НОД двух натуральных чисел
    number1 = str(number1)
    number2 = str(number2)
    number1 = number1.replace("-", "")  # Убираем минусы(Нужно для работы рациональных)
    number2 = number2.replace("-", "")
    if number1 == number2:  # Если числа равны то возвращаем 1
        return "1"
    elif number1 == "0":  # Если какое-то из чисел = 0 то возврващаем 1
        return "1"
    elif number2 == "0":
        return "1"
    while COM_NN_D(number1, number2) != "0":  # Пока числа не равны
        if COM_NN_D(number1, number2) == "2":  # Если первое больше второго то первое = первое - второе
            number1 = SUB_NN_N(number1, number2)
        else:  # Если второе больше первого то второе = второе - первое
            number2 = SUB_NN_N(number2, number1)
    return number1  # возвращаем что получилось


def LCM_NN_N(number1: str, number2: str):  # НОК Натуральных чисел
    number1 = str(number1)
    number2 = str(number2)
    number1 = number1.replace("-", "")  # Убираем начальные знаки(Нужно для работы рациональных)
    number2 = number2.replace("-", "")
    # Возвращаем частное от произведения чисел деленное на НОД этих чисел n1*n2/nod(n1, n2)
    return DIV_NN_N(MUL_NN_N(number1, number2),GCF_NN_N(number1, number2))
