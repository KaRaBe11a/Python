from raspil import rasp


def LED_P_Q(mnog):
    razrez = list(rasp(mnog))  # Распиливаем многочлен на отдельные члены
    stKoef = 0
    maxSt = 0
    step = 0
    bufStr = str()
    for i in range(0, len(razrez)):  # идём по всем членам

        if (razrez[i].count("x") == 1):  # Если в члене есть x
            j = len(razrez[i]) - 1

            if (razrez[i].count("^") == 1):  # если x не в 1 степени

                while (razrez[i][j] != "^"):  # считываем справо на лево его степень
                    bufStr = bufStr + razrez[i][j]
                    j = j - 1
                bufStr = bufStr[::-1]  # переворачиваем
                bufStr = bufStr + str(razrez[i][len(razrez[i]) - 1])  # КОСТЫЛЬ закидываем в конец последний символ
                step = int(bufStr)  # преобразуем степень в int

                bufStr = ""

                if (step > maxSt):  # если степень больше максимальной
                    maxSt = step  # запоминаем степень
                    j = 0
                    while (razrez[i][j] != "x"):  # идём слева до x
                        bufStr = bufStr + razrez[i][j]  # закидываем в строку
                        j = j + 1
                    if (bufStr == "") or (bufStr == "+") or (
                            bufStr == "-"):  # если строка пустая или строка = + или строка = - значит там голый x или же его коэфициент = 1
                        stKoef = 1  # записываем
                    else:
                        stKoef = int(bufStr)  # если там что то есть то кидаем в int и записываем в старший коэфициент
            else:  # если x в 1 степени
                if (maxSt < 1):  # проверяем максимальную степень с 1
                    maxSt = 1
                    j = 0
                    bufStr = ""
                    while (razrez[i][j] != "x"):  # считываем слва до x
                        bufStr = bufStr + razrez[i][j]  # закидываем в строку
                        j = j + 1
                    if (bufStr == "") or (bufStr == "+") or (
                            bufStr == "-"):  # если строка пустая или строка = + или строка = - значит там голый x или же его коэфициент = 1
                        stKoef = 1  # записываем
                    else:
                        stKoef = int(bufStr)  # если там что то есть то кидаем в int и записываем в старший коэфициент
    if (stKoef == 0):  # после прохода по всем элементам если старший коэфициент = 0 значит многочлен это просто число
        bufStr = "".join(razrez[0])  # преобразуем из листа в строку
        stKoef = int(bufStr)  # из строки в int
    return stKoef  # готово








