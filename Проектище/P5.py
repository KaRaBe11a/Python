from raspil import rasp
from SRAVN_Q import  SRAVN_Q


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








