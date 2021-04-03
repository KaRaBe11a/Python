from SRAVN_Q import SRAVN_Q
from raspil import rasp
from Q6 import SUB_QQ_Q
from Q7 import MUL_QQ_Q

def MUL_PQ_P(mnog: str, drob: str):

    razrez = rasp(mnog)

    steps = list() # Степени многочлена
    koefs = list() # коэфициенты многочлена
    # закидываем степени и коэфициенты многочлена в массивы
    for i in range(len(razrez)):

        bufStr = ""
        step = ""
        koef = ""

        if razrez[i].count("x") == 1:  #Если в члене есть x
            if razrez[i].count("^") == 1: #Если он не в 1 степени

                bufStr = "".join(razrez[i]) # Берём член
                idSt = bufStr.find("^") # Находим номер знака степени
                step = "".join(razrez[i][idSt+1:]) # пишем в степень всё после него
                koef = "".join(razrez[i][:idSt-1]) # пишем в коэф всё от начала о номера знака степени -1

                if koef == "": # если коэф = "" значит там 1
                    koef = "1"
                elif koef == "+": # аналогично работаем с + и -
                    koef = "+1"
                elif koef == "-":
                    koef = "-1"

                koefs.append(koef) # закидываем коэф в массив
                steps.append(step) # закидываем степень в массив
            else: # Если он в 1 степени
                steps.append("1") #Логично что степень = 1
                bufStr = "".join(razrez[i]) # берём весь член
                idX = bufStr.find("x") # находим номер икса
                koef = "".join(razrez[i][:idX]) # записываем в коэф всё до него

                if koef == "": # если коэф = "" значит там 1
                    koef = "1"
                elif koef == "+": # аналогично работаем с + и -
                    koef = "+1"
                elif koef == "-": # закидываем коэф в массив
                    koef = "-1"
                koefs.append(koef)
        else: # если x нет
            steps.append("0") #логично что степень 0
            koefs.append("".join(razrez[i])) # берём всё что есть закидываем это в коэф

    # Сортируем массивы по степеням
    for i in range(len(steps)):
        min = SUB_QQ_Q(steps[i], "1")  # так надо поверьте мне
        idMin = 0

        for j in range(i, len(steps)):
            if SRAVN_Q(steps[j], min) == 2:
                min = str(steps[j])
                idMin = j

        koefs[i], koefs[idMin] = koefs[idMin], koefs[i]  # ОООООО эти прекрасные кортежи кайф неописуемый
        steps[i], steps[idMin] = steps[idMin], steps[i]

    result = list()
    resultStr = ""
    for i in range(len(steps)): # умножаем коэфициенты на число и записываем в результат

        resultKoef = MUL_QQ_Q(koefs[i], drob) # Считаем новый коэфициент
        resultStr = ""

        if SRAVN_Q(steps[i], "1") == 0: # Если степень 1 то докидываем x
            resultStr += resultKoef + "x"

        elif SRAVN_Q(steps[i], "0") == 0: # если степень 0 не докидываем x
            resultStr += resultKoef

        else:
            resultStr += resultKoef +"x^"+steps[i] # Если степень не 0 и не 1 то докидываем x^ и степень

        if resultStr[0] != "+" and resultStr[0] != "-": # проверяем на потерю начального знака
            resultStr = "+" + resultStr

        result.append(resultStr) # записываем строку в результат

    resultStr = ""
    if result[0][0] == "+": # тут смотрим надо ли из начала убрать + или нет
        resultStr = "".join(result[0][1:])
    else:
        resultStr = "".join(result[0])
    for i in range(1, len(result)): # записываем всё в результат
        resultStr += "".join(result[i])
    return resultStr # конец





