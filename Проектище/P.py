from Q import SRAVN_Q
from Q import ADD_QQ_Q
from Q import SUB_QQ_Q
from Q import MUL_QQ_Q
from Q import TRANS_Z_Q
from math import gcd
from sympy import lcm
from functools import reduce


def rasp(mnog): # функция распила многочлена на отдельные члены возвращает list(list(str))
    buf = list()
    razrez = list()
    count = 0
    bufStr = str()
    i = 0
    while (i<len(mnog)-1): # идём по строке многочлена
        if(mnog[i] == "+") or (mnog[i] == "-") or (i == 0): # если сивол = + или - или это первый символ
            buf.append(mnog[i]) #закидываем этот символ в буферный лист
            i = i+1
            while(mnog[i]!="+") and (mnog[i]!="-") and (i<len(mnog)-1): # идём до + или до - иди до конца строки
                buf.append(mnog[i]) # записываем эту часть в буферный лист
                i = i+1
            bufStr = "".join(buf) # буферный лист преобразуем в строку
            razrez.append(list(bufStr)) # закидываем эту строку в основной лист
            count = count+1 # считаем количество отдельных членов многочлена
            buf.clear() # чистим буферный лист
    razrez[count-1].append(mnog[len(mnog)-1]) # КОСТЫЛЬ записываем в конец последний символ из строки
    return razrez # вернёт list(list(str)) аля [['x', '^', '2'], ['+', 'x'], ['+', '1']]


def ADD_PP_P(mnog1: str, mnog2: str):
    razrez1 = rasp(mnog1)
    razrez2 = rasp(mnog2)

    stepsR1 = list() # Степени 1го многочлена
    stepsR2 = list() # степени 2го многочлена

    koefsR1 = list() # коэфициента 1го многочлена
    koefsR2 = list() # коэфициенты 2го многочлена

    # запишем степени и коэфициенты 1го многочлена в массив
    for i in range(len(razrez1)):
        bufStr = ""
        step = ""
        koef = ""
        if(razrez1[i].count("x") == 1): #Если в члене есть x
            if(razrez1[i].count("^") == 1): #Если он не в 1 степени

                bufStr = "".join(razrez1[i]) # берём член
                idSt = bufStr.find("^") # находим в какой позиции знак степени
                step = "".join(razrez1[i][idSt+1:]) # пишем в степень всё после него
                koef = "".join(razrez1[i][:idSt-1]) # пишем в коэф всё от начала о номера знака степени -1

                if(koef == ""): # если коэф = "" значит там 1
                    koef = "1"
                elif(koef == "+"): # аналогично работаем с + и -
                    koef = "+1"
                elif(koef == "-"):
                    koef = "-1"

                koefsR1.append(koef) # закидываем коэф в массив
                stepsR1.append(step) # закидываем степень в массив

            else: # Если он в 1 степени

                stepsR1.append("1") #Логично что степень = 1
                bufStr = "".join(razrez1[i]) # берём весь член
                idX = bufStr.find("x") # находим номер икса
                koef = "".join(razrez1[i][:idX]) # записываем в коэф всё до него

                if(koef == ""): # если коэф = "" значит там 1
                    koef = "1"
                elif(koef == "+"):# аналогично работаем с + и -
                    koef = "+1"
                elif(koef == "-"):
                    koef = "-1"
                koefsR1.append(koef) # закидываем коэф в массив

        else: # если x нет
            stepsR1.append("0") #логично что степень 0
            koefsR1.append("".join(razrez1[i])) # берём всё что есть закидываем это в коэф



    # повторяем вышеперечисленное ко 2му многочлену0
    for i in range(len(razrez2)):
        idMin = 0
        step = ""
        if(razrez2[i].count("x") == 1): #если есть x
            if(razrez2[i].count("^") == 1): #если он не в 1 степени

                bufStr = "".join(razrez2[i]) # берём весь член
                idSt = bufStr.find("^") # находим номер знака степени
                step = "".join(razrez2[i][idSt + 1:]) # пишем в степень всё после него
                koef = "".join(razrez2[i][:idSt - 1]) # пишем в коэф всё до номера знака степени -1

                if (koef == ""): # если коэф пустой логично что там что? правильно 1
                    koef = "1"
                elif (koef == "+"): # ну думаю тут логично
                    koef = "+1"
                elif (koef == "-"):
                    koef = "-1"

                koefsR2.append(koef) # ну и кидаем коэф со степенью в массивы
                stepsR2.append(step)

            else: # если x  в 1 степени
                stepsR1.append("1") # Логично что в степень пишем 1
                bufStr = "".join(razrez2[i]) # бурём весь член
                idX = bufStr.find("x") # находим номер x
                koef = "".join(razrez2[i][:idX]) # записываем всё до него в коэф

                if (koef == ""):# если коэф пустой значит коэф = 1
                    koef = "1"
                elif (koef == "+"): # если коэф + значит коэф = +1
                    koef = "+1"
                elif (koef == "-"):# если коэф - значит коэф = -1
                    koef = "-1"
                koefsR2.append(koef)
        else: # если x нема
            stepsR2.append("0") # пишем в степень ноль
            koefsR2.append("".join(razrez2[i])) # закидываем всё в коэф

    # Соединяем массивы степеней и коэфов
    steps = stepsR1
    steps.extend(stepsR2)
    koefs = koefsR1
    koefs.extend(koefsR2)

    #Сортируем оба массива по степеням методом прямого выбора
    for i in range(len(steps)):
        min = SUB_QQ_Q(steps[i], "1") # так надо поверьте мне
        idMin = 0

        for j in range(i, len(steps)):
            if SRAVN_Q(steps[j], min) == 2 :
                min = str(steps[j])
                idMin = j

        koefs[i], koefs[idMin] = koefs[idMin], koefs[i]
        steps[i], steps[idMin] = steps[idMin], steps[i]

    # А теперь всё это считаем и кидаем в результирующий массив
    result = list()
    for i in range(len(steps)):
        F = True # True - за этот проход ничего не ссумировалось False значит что-то ссумировалось
        for j in range(i+1, len(steps)):

            #Если стпенеи сошлись и если тут ещё что-то осталось
            if steps[i] != "" and steps[j] != "":
                if SRAVN_Q(steps[i], steps[j]) == 0:

                    resKoef = ADD_QQ_Q(koefs[i], koefs[j]) # складываем коэфициенты
                    F = False # отмечаем что на этой итерации что-то сложилось

                    if SRAVN_Q(steps[i], "1") == 0: #Если степень 1 то и запишем коэф+x
                        resStr = resKoef+"x"

                    elif SRAVN_Q(steps[i], "0") == 0: #Если степень 0 то и запишем коэф
                        resStr = resKoef

                    else:
                        resStr = resKoef+"x^"+steps[i] # Ну а иначе коэф + x^ + степень

                    if resKoef[0] != "+" and resKoef[0] != "-": # если у коэфа 1 символ не + и не - то закинем +
                        resStr = "+"+resStr

                    result.append(resStr) # закидываем сформированную строку в массив
                    steps[j] = "" # вычищаем из массивов сложенные члены
                    koefs[j] = ""
                    steps[i] = ""
                    koefs[i] = ""
        # Если такой же степени небыло
        # то есть на этой итерации ничекго не сложилось
        if F:
            if steps[i] != "": # кидаем проверку есть ли тут какое то значение или уже пусто
                resKoef = koefs[i]

                if SRAVN_Q(steps[i], "1") == 0: # Если степень 1 то и запишем коэф+x
                    resStr = resKoef+"x"

                elif SRAVN_Q(steps[i], "0") == 0: # если степеень 0 ок
                    resStr = resKoef

                else:
                    resStr = resKoef+"x^"+steps[i] # если степень не 0 и не 1

                if resStr[0] != "+" and resStr[0] != "-": # тут проверяем нужно ли коэфу знак добавить
                    resStr = "+" + resStr
                result.append(resStr) # закидываем получившуюся строку в массив
                koefs[i] = "" # вычищаем что использовали
                steps[i] = ""
    resultStr = ""
    if(result[0][0] == "+"): # тут смотрим если в начале итоговой строки стоит + то его в принципе можно спокойно убрать
        resultStr += "".join(result[0][1:])
    else: # Если там был + то записываем с 1го символа если небыло то с 0го
        resultStr += "".join(result[0])

    for i in range(1, len(result)): # ну и закидываем всё из массива в строку
        resultStr += " " + "".join(result[i])
    return resultStr

def SUB_PP_P(mnog1: str, mnog2: str):
    mnog2 = MUL_PQ_P(mnog2, "-1") # домнажаем второй многочлен на -1
    return ADD_PP_P(mnog1, mnog2) # складываем многочлены

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
        min = SUB_QQ_Q(steps[i], "1")  # берём минимум = 1 степень -1
        idMin = 0

        for j in range(i, len(steps)):
            if SRAVN_Q(steps[j], min) == 2:
                min = str(steps[j])
                idMin = j

        koefs[i], koefs[idMin] = koefs[idMin], koefs[i]
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

def MUL_Pxk_P(mnog, step):
    razrez = list(rasp(mnog))

    for i in range(0, len(razrez)):  # идём по списку
        j = len(razrez[i]) - 1
        bufInt = list()
        bufRazr = list()
        bufStr = str()
        bufStr2 = str()
        znach = int()
        if (razrez[i].count("x") == 1):  # Если в этом куске многочлена есть x

            if (razrez[i].count("^") == 0):  # если x в первой степент
                razrez[i].append("^")  # Закидываем туда знак степени
                razrez[i].append(str(ADD_QQ_Q(str(step), "1")))  # Закидываем степень +1 т.к. у нас уже 1ая
            else:
                while (razrez[i][j] != "^"):  # идём справо налево и записываем какая у нас степень
                    bufInt.append(razrez[i][j])
                    j = j - 1

                bufInt.reverse()  # Поскольку писали справа налево переварачиваем значени
                bufStr = "".join(bufInt)  # Перекидываем из list в str
                bufStr = ADD_QQ_Q(bufStr, str(step)) #Складываем степени

                for k in range(0, j):  # закидываем в буферный list всё что было до "^"
                    bufRazr.append(razrez[i][k])
                bufRazr.append("^")  # добавляем знак "^"
                for k in range(0, len(bufStr)):  # в буферный list закидываем нашу степень
                    bufRazr.append(bufStr[k])
                razrez[i].clear()  # очищаем основной list
                razrez[i] = bufRazr  # записываем новое значение
        else:  # если в этом элементе многочлена нет x
            razrez[i].append("x")  # докидываем x
            razrez[i].append("^")  # докидываем "^"
            razrez[i].append(str(step))  # докидываем степень

    resStr = str()  # итоговая строка
    for i in range(0, len(razrez)):  # из массива листов делаем 1 строку
        resStr = resStr + ("".join(razrez[i]))
    return resStr

def LED_P_Q(mnog): #Старший коэф многочлена
    razrez = list(rasp(mnog))  # Распиливаем многочлен на отдельные члены
    stKoef = ""
    maxSt = "0"
    step = 0
    bufStr = str()
    for i in range(0, len(razrez)):  # идём по всем членам
        bufStr = ""
        if (razrez[i].count("x") == 1):  # Если в члене есть x
            j = len(razrez[i]) - 1

            if (razrez[i].count("^") == 1):  # если x не в 1 степени

                while (razrez[i][j] != "^"):  # считываем справо на лево его степень
                    bufStr = bufStr + razrez[i][j]
                    j = j - 1
                bufStr = bufStr[::-1]  # переворачиваем
                step = bufStr  # просто закинул в нормальную переменную

                bufStr = ""
                if (SRAVN_Q(step, str(maxSt)) == 2):
                    # если степень больше максимальной
                    maxSt = step  # запоминаем степень
                    j = 0
                    while (razrez[i][j] != "x"):  # идём слева до x
                        bufStr = bufStr + razrez[i][j]  # закидываем в строку
                        j = j + 1
                    if(bufStr == "" or bufStr == "+"):
                        stKoef = "1"
                    elif(bufStr == "-"):
                        stKoef = "-1"
                    else:
                        stKoef = bufStr  # если там что то есть то кидаем в int и записываем в старший коэфициент
            else:  # если x в 1 степени
                if (SRAVN_Q("1", str(maxSt)) == 2):  # проверяем максимальную степень с 1
                    maxSt = 1
                    j = 0
                    bufStr = ""
                    while (razrez[i][j] != "x"):  # считываем слва до x
                        bufStr = bufStr + razrez[i][j]  # закидываем в строку
                        j = j + 1
                    if (bufStr == "") or (bufStr == "+") or (
                            bufStr == "-"):  # если строка пустая или строка = + или строка = - значит там голый x или же его коэфициент = 1
                        stKoef = "1" # записываем
                    else:
                        stKoef = bufStr  # если там что то есть то кидаем в int и записываем в старший коэфициент
    if (stKoef == ""):  # после прохода по всем элементам если старший коэфициент = 0 значит многочлен это просто число
        bufStr = "".join(razrez[0])  # преобразуем из листа в строку
        stKoef = bufStr  # из строки в int
    return stKoef  # готово

def DEG_P_N(mnog):
    razrez = list(rasp(mnog))  # Распиливаем многочлен на отдельные члены
    maxStep = "0"
    bufStr = str()
    for i in range(0, len(razrez)):  # Идём по всем членам
        bufStr = ""
        if (razrez[i].count("x") == 1):  # Если в члене есть x
            j = len(razrez[i]) - 1

            if (razrez[i].count("^") == 1):  # Если x не в 1 степени
                while (razrez[i][j] != "^"):  # Выписываем справо на лево до знака степени
                    bufStr = bufStr + razrez[i][j]
                    j = j - 1
                bufStr = bufStr[::-1]  # Переворачиваем
                step = bufStr  # Кидаем в инт
                bufStr = ""

                if (SRAVN_Q(step, maxStep) == 2):  # Проверяем с максимальной степенью
                    maxStep = step
            else:  # Если x в 1 степени
                if (SRAVN_Q("1", maxStep) == 2):
                    maxStep = "1"
    return maxStep  # Если x ов нигде не было вернёт 0

def razb_koef(koef: str):
    chislitel = str()
    znam = str()
    if koef.find(".") != -1:
        koef = TRANS_Z_Q(koef)
    if koef.find("/") != -1:
        idDel = koef.find("/")
        for i in range(0, idDel):
            chislitel += koef[i]
        for i in range(idDel+1, len(koef)):
            znam += koef[i]
    else:
        chislitel = koef
        znam = "1"
    return chislitel, znam



def FAC_P_Q(mnog: str):
    razrez = rasp(mnog)

    chislitels = list()
    znams = list()
    koefs = list()

    """
    Запишем в массив все коэфициенты многочлена
    """
    bufStr = str()
    bufKoef = str()
    bufChisl = str()
    bufZnam = str()
    for i in range(len(razrez)):

        if razrez[i].count("x") == 1: #Если в многочлене есть x
            bufStr = "".join(razrez[i])
            idX = bufStr.find("x")
            bufKoef = "".join(razrez[i][:idX])
            bufChisl, bufZnam = razb_koef(bufKoef)
            chislitels.append(int(bufChisl))
            znams.append(int(bufZnam))
        else:
            bufKoef = "".join(razrez[i])
            bufChisl, bufZnam = razb_koef(bufKoef)
            chislitels.append(int(bufChisl))
            znams.append(int(bufZnam))
    print("НОД числителей")
    print(chislitels)
    print(reduce(lambda x,y:gcd(x,y), chislitels))
    print("НОК знаменателей")
    print(znams)
    print(reduce(lambda x,y: lcm(x,y), znams))

def MUL_PP_P(mnog1: str, mnog2 : str):
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

def DER_P_P(mnog: str):
    razrez = list(rasp((mnog)))

    buffRazr = list()
    buffKoef = str()
    buffStep = str()
    buffZnak = str()
    for i in range(0, len(razrez)):
        buffRazr.clear()
        buffKoef = ""
        buffStep = ""
        if(razrez[i].count("x") == 1): #Если в этом члене есть x
            if(razrez[i].count("^") == 0): #Если x в первой степени

                j = 0
                while(razrez[i][j] != "x"): # Записываем коэфициент
                    buffKoef += razrez[i][j]
                    j += 1

                razrez[i].clear() # Чистим изначальный член
                if(buffKoef == ""): # в зависимости от того что лежит в коэфициенте добавляем то что нужно)))
                    razrez[i].append("1")
                if(buffKoef == "-"):
                    razrez[i].append("-1")
                if(buffKoef == "+"):
                    razrez[i].append("+1")
                if(buffKoef != "" and buffKoef != "-" and buffKoef != "+"):
                    for k in range(0, len(buffKoef)):
                        razrez[i].append(buffKoef[k])

            else: # Если x не в первой степени

                j = 0
                while(razrez[i][j] != "x"): # Взяли коэфициент
                    buffKoef+= razrez[i][j]
                    j+= 1

                if(buffKoef == "" or buffKoef == "+"): # Если коэфа нет значит он равен 1
                    buffKoef += "1"

                if(buffKoef == "-"):
                    buffKoef += "-1"

                j += 2
                while(j<len(razrez[i])): # взяли степень
                    buffStep += razrez[i][j]
                    j += 1

                buffKoef = MUL_QQ_Q(buffKoef, buffStep)
                buffStep = SUB_QQ_Q(buffStep, "1") # расчитали новую степень

                buffZnak = razrez[i][0] #Запомнили что лежало в начале
                razrez[i].clear()
                if(buffZnak == "+"): #Если там был + то докидываем его так как преобразования в инт его теряет
                    razrez[i].append("+")

                for k in range(0, len(buffKoef)): #Закидываем всё остальное
                    razrez[i].append(buffKoef[k])

                print(SRAVN_Q(buffStep, "1"))
                if(SRAVN_Q(buffStep, "1") == 0): #Если степень стала 1
                    razrez[i].append("x")

                if(SRAVN_Q(buffStep, "1") != 0): # Если степень стала > 1
                    razrez[i].append("x")
                    razrez[i].append("^")
                    for k in range(0, len(buffStep)):
                        razrez[i].append(buffStep[k])

        else:
            razrez[i] = ""

    resStr = str()
    for i in range(0, len(razrez)):
        resStr += ("".join((razrez[i])))
    return resStr