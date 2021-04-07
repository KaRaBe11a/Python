from raspil import rasp
from Q7 import MUL_QQ_Q
from Q5 import ADD_QQ_Q
from SRAVN_Q import SRAVN_Q

def MULL_PP_P(mnog1: str, mnog2 : str):
    razrez1 = rasp(mnog1)
    razrez2 = rasp(mnog2)

    koefs1 = list() #Коэфициенты первого многочлена
    steps1 = list() #Степени первого многочлена

    koefs2 = list() # Коэфициенты второго многочлена
    steps2 = list() # Степени второго многочлена
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
                bufStr = "".join(razrez1[i]) # перенесли член в строку
                idSt = bufStr.find("^") # нашли номер элемента в котором лежит знак степенеи
                step = "".join(razrez1[i][idSt + 1:]) # записали всё справо от него в степень
                koef = "".join(razrez1[i][:idSt - 1]) # Записаи всё слева от него -1(уходим на ещё 1 влево что бы не взять x) в коэфициент

                if koef == "": # обрабатываем возможные исключитьельные варианты коэфициентов
                    koef = "1"
                elif koef == "+":
                    koef = "+1"
                elif koef == "-":
                    koef = "-1"

                koefs1.append(koef) # добавляем степень и коэфициент в их массивы
                steps1.append(step)

            else: # Если x  в 1 степени
                steps1.append("1") # закидываем в массив степение 1
                bufStr = "".join(razrez1[i]) # берём член
                idX = bufStr.find("x") # находим номер элемента x
                koef = "".join(razrez1[i][:idX]) # записываем всё слева от него в коэфициент

                if koef == "": # обрабатываем исключительные случаи значения коэфициента
                    koef = "1"
                elif koef == "+":
                    koef = "+1"
                elif koef == "-":
                    koef = "-1"
                koefs1.append(koef) # добаялем коэфициент в массив
        else: # если x нету
            steps1.append("0") # закидываем в степень 0
            koefs1.append("".join(razrez1[i])) # в коэфициент закидываем всё что есть

    for i in range(len(razrez2)):
        bufStr = ""
        step = ""
        koef = ""
        if razrez2[i].count("x") == 1:  # Если в члене есть x

            if razrez2[i].count("^") == 1:  # Если он не в 1 степени
                bufStr = "".join(razrez2[i]) # перенесли член в строку
                idSt = bufStr.find("^")  # нашли номер элемента в котором лежит знак степенеи
                step = "".join(razrez2[i][idSt + 1:]) # записали всё справо от него в степень
                koef = "".join(razrez2[i][:idSt - 1]) # Записаи всё слева от него -1(уходим на ещё 1 влево что бы не взять x) в коэфициент

                if koef == "": # обрабатываем возможные исключитьельные варианты коэфициентов
                    koef = "1"
                elif koef == "+":
                    koef = "+1"
                elif koef == "-":
                    koef = "-1"

                koefs2.append(koef) # добавляем степень и коэфициент в их массивы
                steps2.append(step)

            else: # Если x  в 1 степени
                steps2.append("1") # закидываем в массив степение 1
                bufStr = "".join(razrez2[i]) # берём член
                idX = bufStr.find("x") # находим номер элемента x
                koef = "".join(razrez2[i][:idX]) # записываем всё слева от него в коэфициент

                if koef == "": # обрабатываем исключительные случаи значения коэфициента
                    koef = "1"
                elif koef == "+":
                    koef = "+1"
                elif koef == "-":
                    koef = "-1"
                koefs2.append(koef) # добаялем коэфициент в массив
        else: # если x нету
            steps2.append("0") # закидываем в степень 0
            koefs2.append("".join(razrez2[i])) # в коэфициент закидываем всё что есть


    """
    Перемножаем каждый элемент первого многочлена
    с каждым элементом второго многоччлена
    при этом их степени складываются а коэфициенты перемножаются
    результат записываем в 2 массива 1 массив получившиеся коэфициенты
    2 массив получившиеся степени
    """
    resKoefs = list() # коэфициенты после умножения
    resSteps = list() # степени после сложения
    for i in range(len(razrez1)): # Идём по длинне первого многочлена

        for j in range(len(razrez2)): # идём по длинне второго многочлена

            bufKoef = ""
            bufSt = ""

            bufKoef = MUL_QQ_Q(koefs1[i], koefs2[j]) # перемножаем коэфициенты
            bufSt = ADD_QQ_Q(steps1[i], steps2[j]) # Складываем степени

            resKoefs.append(bufKoef) # закидываем в результат в новые массивы
            resSteps.append(bufSt)

    """
    Сократим получившиеся многочлен сложив члены с одиноковыми степенями
    """

    for i in range(len(resSteps)): # идём от 0 до длинны многочлена

        for j in range(i+1, len(resKoefs)): # идём от i+1 до длинны многочлена
            if resSteps[i] != "" and resSteps[j] != "": # проверяем не удалён ли уже этот элемент
                if SRAVN_Q(resSteps[i], resSteps[j]) == 0: # если степени элементов равны
                    resKoefs[i] = ADD_QQ_Q(resKoefs[i], resKoefs[j]) # складываем коэфициенты
                    resKoefs[j] = "" # удаляем элемент который прибавили
                    resSteps[j] = ""


    """
    Соберём из полученных массивов массив элементов многочлена
    """
    result = list()
    for i in range(len(resSteps)): # собираем массивы коэфициентов и степеней в массив частей многочлена
        if resSteps[i] != "": # проверяем не удалён ли этот элемент
            if resSteps[i] == "0": # если степень = 0
                result.append(resKoefs[i]) # то добавляем в массив только коэфициент
            elif resSteps[i] == "1": # если степень = 1 то добавляем в массив коэф умноженный на x
                result.append(resKoefs[i] + "x")
            else: # если степень не ноль и не 1
                result.append(resKoefs[i] + "x^" + resSteps[i]) # добавляем в массив коэф умноженный на x в степени


    """
    Соберём из массива элементов многочлена многочлен
    """

    resultStr = "" # Это строка будет хранить рузельтирующий многочлен
    if result[0][0] == "+": # тут смотрим надо ли из начала убрать + или нет
        resultStr = "".join(result[0][1:]) # если в самом начале стоит + то его убираем
    else: # иначе записываем как есть
        resultStr = "".join(result[0])

    for i in range(1, len(result)): # записываем всё в результат
       if result[i][0] != "+" or result[i][0] != "-": # если перед коэфициентом не стоит не + и не -
           resultStr += "+" + "".join(result[i]) # значит надо добавить + потому что - бы программа сохранила а вот + она теряет при вычислениях
       else: # если знак не потерян
           resultStr += "".join(result[i]) # записыаем как есть
    return resultStr # конец

