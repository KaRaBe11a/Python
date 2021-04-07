from raspil import rasp
from Q7 import MUL_QQ_Q
from Q5 import ADD_QQ_Q
from SRAVN_Q import SRAVN_Q

def MULL_PP_P(mnog1: str, mnog2 : str):
    razrez1 = rasp(mnog1)
    razrez2 = rasp(mnog2)

    koefs1 = list()
    steps1 = list()

    koefs2 = list()
    steps2 = list()
    """
    Разбиваем оба многочлена на их степени
    и коэфициенты записывая эти данные в соответсвующие массивы
    """
    for i in range(len(razrez1)):
        bufStr = ""
        step = ""
        koef = ""
        if razrez1[i].count("x") == 1:  # Если в члене есть x

            if razrez1[i].count("^") == 1:  # Если он не в 1 степени
                bufStr = "".join(razrez1[i])
                idSt = bufStr.find("^")
                step = "".join(razrez1[i][idSt + 1:])
                koef = "".join(razrez1[i][:idSt - 1])

                if koef == "":
                    koef = "1"
                elif koef == "+":
                    koef = "+1"
                elif koef == "-":
                    koef = "-1"

                koefs1.append(koef)
                steps1.append(step)

            else:
                steps1.append("1")
                bufStr = "".join(razrez1[i])
                idX = bufStr.find("x")
                koef = "".join(razrez1[i][:idX])

                if koef == "":
                    koef = "1"
                elif koef == "+":
                    koef = "+1"
                elif koef == "-":
                    koef = "-1"
                koefs1.append(koef)
        else:
            steps1.append("0")
            koefs1.append("".join(razrez1[i]))

    for i in range(len(razrez2)):
        bufStr = ""
        step = ""
        koef = ""
        if razrez2[i].count("x") == 1:  # Если в члене есть x

            if razrez2[i].count("^") == 1:  # Если он не в 1 степени
                bufStr = "".join(razrez2[i])
                idSt = bufStr.find("^")
                step = "".join(razrez2[i][idSt + 1:])
                koef = "".join(razrez2[i][:idSt - 1])

                if koef == "":
                    koef = "1"
                elif koef == "+":
                    koef = "+1"
                elif koef == "-":
                    koef = "-1"

                koefs2.append(koef)
                steps2.append(step)

            else:
                steps2.append("1")
                bufStr = "".join(razrez2[i])
                idX = bufStr.find("x")
                koef = "".join(razrez2[i][:idX])

                if koef == "":
                    koef = "1"
                elif koef == "+":
                    koef = "+1"
                elif koef == "-":
                    koef = "-1"
                koefs2.append(koef)
        else:
            steps2.append("0")
            koefs2.append("".join(razrez2[i]))


    """
    Перемножаем каждый элемент первого многочлена
    с каждым элементом второго многоччлена
    при этом их степени складываются а коэфициенты перемножаются
    результат записываем в 2 массива 1 массив получившиеся коэфициенты
    2 массив получившиеся степени
    """
    resKoefs = list()
    resSteps = list()
    for i in range(len(razrez1)):

        for j in range(len(razrez2)):

            bufKoef = ""
            bufSt = ""

            bufKoef = MUL_QQ_Q(koefs1[i], koefs2[j])
            bufSt = ADD_QQ_Q(steps1[i], steps2[j])

            resKoefs.append(bufKoef)
            resSteps.append(bufSt)


    CountKoefs = len(resKoefs)
    CountSteps = len(resSteps)
    for i in range(len(resSteps)):

        for j in range(i+1, len(resKoefs)):
            if resSteps[i] != "" and resSteps[j] != "":
                if SRAVN_Q(resSteps[i], resSteps[j]) == 0:
                    resKoefs[i] = ADD_QQ_Q(resKoefs[i], resKoefs[j])
                    resKoefs[j] = ""
                    resSteps[j] = ""


    print(resSteps)
    print(resKoefs)

    result = list()
    for i in range(len(resSteps)):
        if resSteps[i] != "":
            if resSteps[i] == "0":
                result.append(resKoefs[i])
            elif resSteps[i] == "1":
                result.append(resKoefs[i] + "x")
            else:
                result.append(resKoefs[i] + "x^" + resSteps[i])

    resultStr = ""
    if result[0][0] == "+": # тут смотрим надо ли из начала убрать + или нет
        resultStr = "".join(result[0][1:])
    else:
        resultStr = "".join(result[0])

    for i in range(1, len(result)): # записываем всё в результат
       if result[i][0] != "+" or result[i][0] != "-":
           resultStr += "+" + "".join(result[i])
       else:
           resultStr += "".join(result[i])
    return resultStr # конец

