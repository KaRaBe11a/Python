from RefactoringQ import *
from functools import reduce


def rasp(polynomial):  # функция распила многочлена на отдельные члены возвращает list(list(str))
    if polynomial == "0":
        return "0"
    buf = list()
    cut = list()
    count = 0
    i = 0

    while i < len(polynomial) - 1:  # идём по строке многочлена

        if polynomial[i] == "+" or polynomial[i] == "-" or i == 0:  # если сивол = + или - или это первый символ
            buf.append(polynomial[i])  # закидываем этот символ в буферный лист
            i = i+1
            # идём до + или до - иди до конца строки
            while polynomial[i] != "+" and polynomial[i] != "-" and i < len(polynomial)-1:
                buf.append(polynomial[i])  # записываем эту часть в буферный лист
                i = i+1
            buf_str = "".join(buf)  # буферный лист преобразуем в строку
            cut.append(list(buf_str))  # закидываем эту строку в основной лист
            count = count+1  # считаем количество отдельных членов многочлена
            buf.clear()  # чистим буферный лист

    cut[count - 1].append(polynomial[-1])  # КОСТЫЛЬ записываем в конец последний символ из строки
    return cut  # вернёт list(list(str)) аля [['x', '^', '2'], ['+', 'x'], ['+', '1']]


def coefficients_and_steps(polynomial):  # Функциы переводящая многочлен из строки в массив коэфициентво и степеней
    cut = rasp(polynomial)  # разбиваем многочлен на отдельные члены

    coefficients = list()  # Создаём массив для коэфициентов
    steps = list()  # Создаём массив для степеней
    for i in range(len(cut)):  # идём по количеству членов

        if cut[i].count("x") == 1:  # Если в члене есть x

            if cut[i].count("^") == 1:  # Если он не в первой степени
                tmp_str = "".join(cut[i])  # преобразуем член из массива в строку
                id_step = tmp_str.find("^")  # Находим номер знака степени в строке
                step = tmp_str[id_step+1:]  # Записывакм степень
                coefficient = tmp_str[:id_step-1]  # Записываем коэфициент

                if coefficient == "":  # обрабатываем возможные исключитьельные варианты коэфициентов
                    coefficient = "1"
                elif coefficient == "+":
                    coefficient = "+1"
                elif coefficient == "-":
                    coefficient = "-1"

                coefficients.append(coefficient)  # Добавляем полученное в массивы степеней и коэфициентов
                steps.append(step)

            else:  # Если х в первой степени
                steps.append("1")  # Записываем в степень 1
                tmp_str = "".join(cut[i])  # преобразуем член из массива в строку
                id_step = tmp_str.find("x")  # Находим номер х в строку
                coefficient = tmp_str[:id_step]  # Записываем коэфициент

                if coefficient == "":  # обрабатываем возможные исключитьельные варианты коэфициентов
                    coefficient = "1"
                elif coefficient == "+":
                    coefficient = "+1"
                elif coefficient == "-":
                    coefficient = "-1"

                coefficients.append(coefficient)  # Добавляем коэфициент в массив
        else:  # Если х в члене отсутствует
            steps.append("0")  # Добавляем в массив степеней 0
            coefficients.append("".join(cut[i]))  # добавляем в массив коэфициентов весь член

    return coefficients, steps


def polynomial_sort(polynomial: str):  # Функция сортировки многочлена
    coefficients, steps = coefficients_and_steps(polynomial)  # разьиваем многочлен на массивы коэфициентов и степеней

    for i in range(len(steps)):  # Идём по количеству степеней
        min_step = SUB_QQ_Q(steps[i], "1")  # берём минимум = 1 степень -1
        id_min = 0

        for j in range(i, len(steps)):  # Находим минимальную степень и её номер
            if SRAVN_Q(steps[j], min_step) == "2":
                min_step = str(steps[j])
                id_min = j

        coefficients[i], coefficients[id_min] = coefficients[id_min], coefficients[i]  # постепенно меняем члены местами
        steps[i], steps[id_min] = steps[id_min], steps[i]

    return coefficients, steps  # возвращаем массив коэфициентов и степеней


def list_to_sting(coefficients: list, steps: list):  # Функция преобразования многочлена из массивов степеней и коэфициентов в строку
    res_str = ""
    # Обрабатываем первый член
    if coefficients[0] != "0":  # Если коэфициент не ноль
        if steps[0] == "0":  # Если степень 0
            res_str = coefficients[0]  # То записываем в рузельтат только коэфициент
        elif steps[0] == "1":  # Есди степень 1
            res_str = coefficients[0] + "x"  # То записываем в результат коэфициент + х
        else:  # Иначе
            res_str = coefficients[0] + "x^" + steps[0]  # записываем в рузельтат коэфициент + x^ + степень
    for i in range(1, len(steps)):  # Обрабатываем все следующие члены
        if coefficients[i] != "0":  # Если коэфициент не 0
            if steps[i] == "0":  # Если степень 0
                if coefficients[i][0] != "-" and coefficients[i][0] != "+":  # Если у коэфициента нет знака
                    res_str += "+"  # добавляем +
                res_str += coefficients[i]  # Записываем в результат коэфициент
            elif steps[i] == "1":  # Если степень = 1
                if coefficients[i][0] != "-" and coefficients[i][0] != "+":  # если у коэфициента нет знака
                    res_str += "+"  # добавляем +
                res_str += coefficients[i] + "x"  # Записываем клэфициент + х
            else:  # Иначе
                if coefficients[i][0] != "-" and coefficients[i][0] != "+":  # Если у коэфициента нет знака
                    res_str += "+"  # добавляем в результат +
                res_str += coefficients[i] + "x^" + steps[i]  # добавляем в результат коэфициент + x^ + степень
    if res_str == "":  # Если многочлена не получилось
        res_str = "0"  # Возвращаем 0
    if res_str[0] == "+":  # Если в начале чтоит +
        res_str = res_str[1:]  # Убираем его
    return res_str


def ADD_PP_P(polynomial1: str, polynomial2: str):  # Сложение многочленов
    coefficients1, steps1 = coefficients_and_steps(polynomial1)  # Разбиваем многочлены на массивы степеней и коэфициентов
    coefficients2, steps2 = coefficients_and_steps(polynomial2)

    coefficients = coefficients1  # Собираем из двух массивов 1
    coefficients.extend(coefficients2)
    steps = steps1
    steps.extend(steps2)

    new_polynomial = list_to_sting(coefficients, steps)   # сортируем полученный многочлен
    coefficients, steps = polynomial_sort(new_polynomial)

    res_coefficients = list()  # Итоговые коэфициенты
    res_steps = list()  # Итоговые степени

    for i in range(len(steps)):  # идём от 0 до длинны степеней
        for j in range(i+1, len(steps)):  # идём от i дл длинны степеней
            if steps[i] == steps[j] and steps[i] != "":  # Если степени равны и они не пустые

                res_steps.append(steps[i])  # Добавляем степень в результат
                res_coefficients.append(ADD_QQ_Q(coefficients[i], coefficients[j]))  # Добавляем в результат сумму коэфициентов
                steps[i] = ""  # убираем степени которые использовали
                steps[j] = ""
    # Добавим в результат всё что не сложилось
    for i in range(len(steps)):  # идём по длинне степеней
        if steps[i] != "":  # Если сьепень не пустая
            res_steps.append(steps[i])  # Добавляем её в результат
            res_coefficients.append(coefficients[i])  # добавим коэфициент в результат
    # отсортируем что получили
    result = list_to_sting(res_coefficients, res_steps)
    result = polynomial_sort(result)
    result = list_to_sting(result[0], result[1])  # и преобразуем в строку
    return result


def MUL_PQ_P(polynomial: str, fraction: str):  # Умножение многочлена на число
    coefficients, steps = polynomial_sort(polynomial)  # разбиваем многочлен на массив коэфициентов и степеней

    for i in range(len(steps)):  # умножаем каждый коэфициент на число
        coefficients[i] = MUL_QQ_Q(coefficients[i], fraction)

    result = list_to_sting(coefficients, steps)  # преобразуем всё обратно в строку
    return result


def SUB_PP_P(polynomial1: str, polynomial2: str):  # вычитание многочленов
    polynomial2 = MUL_PQ_P(polynomial2, "-1")  # Умножаем второй многочлен на -1
    polynomial2 = ADD_PP_P(polynomial1, polynomial2)  # Сложим первый со вторым
    polynomial2 = polynomial_sort(polynomial2)  # Отсортируем и уберём всё что обнулилось
    polynomial2 = list_to_sting(polynomial2[0], polynomial2[1])
    return polynomial2


def MUL_Pxk_P(polynomial1: str, k: str):  # Умножение многочлена на x^k
    coefficients, steps = polynomial_sort(polynomial1)   # Разбиваем многочлен на массив коэфициентов и степеней

    for i in range(len(steps)):  # прибавляем к каждой степени k
        steps[i] = ADD_QQ_Q(steps[i], k)

    result = list_to_sting(coefficients, steps)   # преобразуем обратно в строку
    return result


def LED_P_Q(polynomial: str):  # Старший коэфициент многочлена
    coefficients, steps = polynomial_sort(polynomial)  # Сортируем многочлен по степеням
    return coefficients[0]  # Возвращаем первый коэфициент


def DEG_P_N(polynomial: str):  # Степень многочлена
    coefficients, steps = coefficients_and_steps(polynomial)  # Сортируем многочлен по степеням
    return steps[0]  # Возвращаем первую степень


def MUL_PP_P(polynomial1: str, polynomial2: str):  # Произведение многочленов

    coefficients1, steps1 = coefficients_and_steps(polynomial1)  # Разбиваем многочлены на массивы степеней и коэфициентов
    coefficients2, steps2 = coefficients_and_steps(polynomial2)

    new_coefficients = list()  # новые коэфициенты
    new_steps = list()  # Новые степени

    for i in range(len(steps1)):  # Идём по длинне первого многочлена
        for j in range(len(steps2)):  # Идём по длинне второго многочлена

            new_coefficients.append(MUL_QQ_Q(coefficients1[i], coefficients2[j]))  # Умножаем каждый коэфициент первого многочлена на каждый коэф второго
            new_steps.append(ADD_QQ_Q(steps1[i], steps2[j]))  # Умножаем каждую степень первого многочлена на каждуй степень второго

    summed_coefficients = list()
    summed_steps = list()
    # Проссумируем все члены с одинаковыми степенями
    for i in range(len(new_steps)):  # идём по длинне многочлена
        for j in range(i+1, len(new_steps)):  # идём от i+1 до длинны второго
            if new_steps[i] == new_steps[j] and new_steps[i] != "":  # Если степени равны и не пустые

                summed_coefficients.append(ADD_QQ_Q(new_coefficients[i], new_coefficients[j]))  # Складываем коэфициенты
                summed_steps.append(new_steps[i])  # записываем степень
                new_steps[i] = ""
                new_steps[j] = ""

    for i in range(len(new_steps)):  # Идём по длинне степеней
        if new_steps[i] != "":  # Если степень не пустая
            summed_coefficients.append(new_coefficients[i])  # добавляем в итоговый массив коэф
            summed_steps.append(new_steps[i])  # Добавляем в итоговый массив коэфициент

    result = list_to_sting(summed_coefficients, summed_steps)  # Сортируем что получили
    coefficients, steps = polynomial_sort(result)
    result = list_to_sting(coefficients, steps)
    return result


def FAC_P_Q(polynomial1: str):  # НОК знаменателей коэфициентов НОД числителей коэфициентов
    coefficients, steps = polynomial_sort(polynomial1)   # Разбиваем многочлен на массив степеней и коэфициентов

    numerators = list()  # Массив числителей
    denominators = list()  # Массив знаменателей

    for i in range(len(coefficients)):  # разбиваем коэфициенты на числители и знаменатели
        numerator, denominator = razbil_drob(coefficients[i])
        numerators.append(numerator)
        denominators.append(denominator)

    result1 = reduce(lambda x, y: LCM_NN_N(x, y), numerators)  # Вычситываем НОК
    result2 = reduce(lambda x, y: GCF_NN_N(x, y), denominators)  # Высчитываем НОД

    return result1, result2


def DIV_MOD_PP_P(polynomial1: str, polynomial2: str):  # Частное и остаток от деления многочленов
    division_result = ""
    coefficients1, steps1 = coefficients_and_steps(polynomial1)  # разбиваем многочлены на массивы коэфициентов и степеней
    coefficients2, steps2 = coefficients_and_steps(polynomial2)

    step_polynomial1 = DEG_P_N(polynomial1)  # Берём степени многочленов
    step_polynomial2 = DEG_P_N(polynomial2)

    # пока степенбь первого больше второго или они равны
    while SRAVN_Q(step_polynomial1, step_polynomial2) == "2" or SRAVN_Q(step_polynomial1, step_polynomial2) == "0":
        need_multiplier_step = SUB_QQ_Q(step_polynomial1, step_polynomial2)  # вычитаем степень делителя из степени делимого
        need_coefficient = DIV_QQ_Q(coefficients1[0], coefficients2[0])  # Берём частно от старших коэфициентов
        this_division = need_coefficient + "x^" + need_multiplier_step  # находим очередной член многочлена частного
        if this_division[0] != "-" and this_division[0] != "+":  # Если у него нет знака то добавляем его
            this_division = "+" + this_division
        division_result += this_division  # Добавляем в итоговое частное
        if this_division[0] == "+":  # Убираем начльный знак если он +
            this_division = this_division[1:]
        this_division = MUL_PP_P(polynomial2, this_division)  # Умножаем очередной член многочлена частного на делитель
        this_division = polynomial_sort(this_division)  # сортируем
        this_division = list_to_sting(this_division[0], this_division[1])
        polynomial1 = SUB_PP_P(polynomial1, this_division)  # Вычитаем из делимого полученный многочлен
        polynomial1 = polynomial_sort(polynomial1)  # Сортируем
        polynomial1 = list_to_sting(polynomial1[0], polynomial1[1])
        coefficients1, steps1 = coefficients_and_steps(polynomial1)  # Разбиваем на массив коэфициентов и степеней
        step_polynomial1 = DEG_P_N(polynomial1)  # Берём степень получившегося делимого

    if division_result[0] == "+":  # Если в начале итога + то убираем его
        division_result = division_result[1:]

    division_result = polynomial_sort(division_result)  # Сортируем результат
    division_result = list_to_sting(division_result[0], division_result[1])

    return division_result, polynomial1


def GCF_PP_P(polynomial1: str, polynomial2: str):  # Нод многочленов

    div, mod = DIV_MOD_PP_P(polynomial1, polynomial2)  # находим частное и остаток от деления многочленова
    prev_mod = ""  # Запоминает предыдущий остаток
    while mod != "0":  # Пока остаток не ноль
        prev_mod = mod  # запоминаем предыдущий остаток
        polynomial1 = polynomial2  # делитель становиться делимым
        div, mod = DIV_MOD_PP_P(polynomial1, mod)  # Находим чатное и остаток
        polynomial2 = div
    return prev_mod  # Возвращаем последний ненулевой остаток


def DER_P_P(polynomial: str):  # Производная многочлена
    coefficients, steps = coefficients_and_steps(polynomial)  # Разбиваем многочлен на массив степеней и коэфициентов
    for i in range(len(steps)):  # идём по длинне степеней
        coefficients[i] = MUL_QQ_Q(coefficients[i], steps[i])  # домножаем каждый коэфициент на степень
        steps[i] = SUB_QQ_Q(steps[i], "1")  # вычитаем из степени 1
    result = list_to_sting(coefficients, steps)  # преобразуем в строку
    return result


def NMR_P_P(polynomial: str):
    proizv = DER_P_P(polynomial)
    nod = GCF_PP_P(polynomial, proizv)
    div, mod = DIV_MOD_PP_P(polynomial, nod)
    res = div
    return res