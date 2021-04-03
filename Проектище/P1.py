from SRAVN_Q import SRAVN_Q
from raspil import rasp
from Q5 import ADD_QQ_Q
from Q6 import SUB_QQ_Q


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

                if (koef == ""):# если коэф пустой логично что там что? правильно 1
                    koef = "1"
                elif (koef == "+"):# ну думаю тут логично
                    koef = "+1"
                elif (koef == "-"):
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

        koefs[i], koefs[idMin] = koefs[idMin], koefs[i] # ОООООО эти прекрасные кортежи кайф неописуемый
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

                if SRAVN_Q(steps[i], "1") == 0: # если степень 1 ну я надеюсь вы уже поняли
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
    return resultStr # РЕТУРН !!!!!!!!!!!!!!!!!!!!!!!!


