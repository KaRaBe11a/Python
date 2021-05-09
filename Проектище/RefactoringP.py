from RefactoringQ import *
from functools import reduce


def rasp(polynomial):  # функция распила многочлена на отдельные члены возвращает list(list(str))
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

    cut[count - 1].append(polynomial[len(polynomial) - 1])  # КОСТЫЛЬ записываем в конец последний символ из строки
    return cut  # вернёт list(list(str)) аля [['x', '^', '2'], ['+', 'x'], ['+', '1']]


def coefficients_and_steps(polynomial):
    cut = rasp(polynomial)

    coefficients = list()
    steps = list()
    for i in range(len(cut)):

        if cut[i].count("x") == 1:

            if cut[i].count("^") == 1:
                tmp_str = "".join(cut[i])
                id_step = tmp_str.find("^")
                step = tmp_str[id_step+1:]
                coefficient = tmp_str[:id_step-1]

                if coefficient == "":  # обрабатываем возможные исключитьельные варианты коэфициентов
                    coefficient = "1"
                elif coefficient == "+":
                    coefficient = "+1"
                elif coefficient == "-":
                    coefficient = "-1"

                coefficients.append(coefficient)
                steps.append(step)

            else:
                steps.append("1")
                tmp_str = "".join(cut[i])
                id_step = tmp_str.find("x")
                coefficient = tmp_str[:id_step]

                if coefficient == "":  # обрабатываем возможные исключитьельные варианты коэфициентов
                    coefficient = "1"
                elif coefficient == "+":
                    coefficient = "+1"
                elif coefficient == "-":
                    coefficient = "-1"

                coefficients.append(coefficient)
        else:
            steps.append("0")
            coefficients.append("".join(cut[i]))

    return coefficients, steps


def polynomial_sort(polynomial: str):
    coefficients, steps = coefficients_and_steps(polynomial)

    for i in range(len(steps)):
        min_step = SUB_QQ_Q(steps[i], "1")  # берём минимум = 1 степень -1
        id_min = 0

        for j in range(i, len(steps)):
            if SRAVN_Q(steps[j], min_step) == "2":
                min_step = str(steps[j])
                id_min = j

        coefficients[i], coefficients[id_min] = coefficients[id_min], coefficients[i]
        steps[i], steps[id_min] = steps[id_min], steps[i]

    return coefficients, steps


def list_to_sting(coefficients: list, steps: list):
    res_str = ""
    if coefficients[0] != "0":
        if steps[0] == "0":
            res_str = coefficients[0]
        elif steps[0] == "1":
            res_str = coefficients[0] + "x"
        else:
            res_str = coefficients[0] + "x^" + steps[0]
    for i in range(1, len(steps)):
        if coefficients[i] != "0":
            if steps[i] == "0":
                if coefficients[i][0] != "-" and coefficients[i][0] != "+":
                    res_str += "+"
                res_str += coefficients[i]
            elif steps[i] == "1":
                if coefficients[i][0] != "-" and coefficients[i][0] != "+":
                    res_str += "+"
                res_str += coefficients[i] + "x"
            else:
                if coefficients[i][0] != "-" and coefficients[i][0] != "+":
                    res_str += "+"
                res_str += coefficients[i] + "x^" + steps[i]
    if res_str == "":
        res_str = "0"
    if res_str[0] == "+":
        res_str = res_str[1:]
    return res_str


def ADD_PP_P(polynomial1: str, polynomial2: str):
    coefficients1, steps1 = coefficients_and_steps(polynomial1)
    coefficients2, steps2 = coefficients_and_steps(polynomial2)

    coefficients = coefficients1
    coefficients.extend(coefficients2)
    steps = steps1
    steps.extend(steps2)

    new_polynomial = list_to_sting(coefficients, steps)

    coefficients, steps = polynomial_sort(new_polynomial)

    res_coefficients = list()
    res_steps = list()

    for i in range(len(steps)):
        for j in range(i+1, len(steps)):
            if steps[i] == steps[j] and steps[i] != "":

                res_steps.append(steps[i])
                res_coefficients.append(ADD_QQ_Q(coefficients[i], coefficients[j]))
                steps[i] = ""
                steps[j] = ""
    for i in range(len(steps)):
        if steps[i] != "":
            res_steps.append(steps[i])
            res_coefficients.append(coefficients[i])

    result = list_to_sting(res_coefficients, res_steps)
    result = polynomial_sort(result)
    result = list_to_sting(result[0], result[1])
    return result


def MUL_PQ_P(polynomial: str, fraction: str):
    coefficients, steps = polynomial_sort(polynomial)

    for i in range(len(steps)):
        coefficients[i] = MUL_QQ_Q(coefficients[i], fraction)

    result = list_to_sting(coefficients, steps)
    return result


def SUB_PP_P(polynomial1: str, polynomial2: str):
    polynomial2 = MUL_PQ_P(polynomial2, "-1")
    return ADD_PP_P(polynomial1, polynomial2)


def MUL_Pxk_P(polynomial1: str, k: str):
    coefficients, steps = polynomial_sort(polynomial1)

    for i in range(len(steps)):
        steps[i] = ADD_QQ_Q(steps[i], k)

    result = list_to_sting(coefficients, steps)
    return result


def LED_P_Q(polynomial: str):
    coefficients, steps = polynomial_sort(polynomial)
    return coefficients[0]


def DEG_P_N(polynomial: str):
    coefficients, steps = coefficients_and_steps(polynomial)
    return steps[0]


def MUL_PP_P(polynomial1: str, polynomial2: str):

    coefficients1, steps1 = coefficients_and_steps(polynomial1)
    coefficients2, steps2 = coefficients_and_steps(polynomial2)
    print(coefficients1, steps1)
    print(coefficients2, steps2)

    new_coefficients = list()
    new_steps = list()

    for i in range(len(steps1)):
        for j in range(len(steps2)):

            new_coefficients.append(MUL_QQ_Q(coefficients1[i], coefficients2[j]))
            new_steps.append(ADD_QQ_Q(steps1[i], steps2[j]))

    summed_coefficients = list()
    summed_steps = list()

    for i in range(len(new_steps)):
        for j in range(i+1, len(new_steps)):
            if new_steps[i] == new_steps[j] and new_steps[i] != "":

                summed_coefficients.append(ADD_QQ_Q(new_coefficients[i], new_coefficients[j]))
                summed_steps.append(new_steps[i])

    for i in range(len(new_steps)):
        if new_steps[i] != "":
            summed_coefficients.append(new_coefficients[i])
            summed_steps.append(new_steps[i])

    result = list_to_sting(summed_coefficients, summed_steps)
    coefficients, steps = polynomial_sort(result)
    result = list_to_sting(coefficients, steps)
    return result


def FAC_P_Q(polynomial1: str):
    coefficients, steps = polynomial_sort(polynomial1)

    numerators = list()
    denominators = list()

    for i in range(len(coefficients)):
        numerator, denominator = razbil_drob(coefficients[i])
        numerators.append(numerator)
        denominators.append(denominator)

    result1 = reduce(lambda x, y: LCM_NN_N(x, y), numerators)
    result2 = reduce(lambda x, y: GCF_NN_N(x, y), denominators)

    return result1, result2


def DIV_PP_P(polynomial1: str, polynomial2: str):
    division_result = ""
    coefficients1, steps1 = coefficients_and_steps(polynomial1)

    coefficients2, steps2 = coefficients_and_steps(polynomial2)

    step_polynomial1 = DEG_P_N(polynomial1)
    step_polynomial2 = DEG_P_N(polynomial2)

    while SRAVN_Q(step_polynomial1, step_polynomial2) == "2" or SRAVN_Q(step_polynomial1, step_polynomial2) == "0":

        need_multiplier_step = SUB_QQ_Q(step_polynomial1, step_polynomial2)
        need_coefficient = MUL_QQ_Q(coefficients1[0], coefficients2[0])
        this_division = need_coefficient + "x^" + need_multiplier_step
        if this_division[0] != "-" and this_division[0] != "+":
            this_division = "+" + this_division
        division_result += this_division
        if this_division[0] == "+":
            this_division = this_division[1:]
        this_division = MUL_PP_P(polynomial2, this_division)
        this_division = polynomial_sort(this_division)
        this_division = list_to_sting(this_division[0], this_division[1])
        polynomial1 = SUB_PP_P(polynomial1, this_division)
        polynomial1 = polynomial_sort(polynomial1)
        polynomial1 = list_to_sting(polynomial1[0], polynomial1[1])
        coefficients1, steps1 = coefficients_and_steps(polynomial1)
        step_polynomial1 = DEG_P_N(polynomial1)
    if division_result[0] == "+":
        division_result = division_result[1:]
    division_result = polynomial_sort(division_result)
    division_result = list_to_sting(division_result[0], division_result[1])

    return division_result

def MOD_PP_P(polynomial1: str, polynomial2: str):

    chastnoe = DIV_PP_P(polynomial1, polynomial2)
    print(chastnoe)
    mul = MUL_PP_P(chastnoe, polynomial2)
    print(mul)

