from raspil import rasp


def DEG_P_N(mnog):
    razrez = list(rasp(mnog))  # Распиливаем многочлен на отдельные члены
    maxStep = 0
    bufStr = str()
    for i in range(0, len(razrez)):  # Идём по всем членам

        if (razrez[i].count(x) == 1):  # Если в члене есть x
            j = len(razrez[i]) - 1

            if (razrez[i].count("^") == 1):  # Если x не в 1 степени
                while (razrez[i][j] != "^"):  # Выписываем справо на лево до знака степени
                    bufStr = bufStr + razrez[i][j]
                    j = j - 1
                bufStr = bufStr[::-1]  # Переворачиваем
                bufStr = bufStr + str(razrez[i][len(razrez[i]) - 1])  # Костыль закидываем в конец последний элемент
                step = int(BufStr)  # Кидаем в инт
                bufStr = ""

                if (step > maxStep):  # Проверяем с максимальной степенью
                    maxStep = step
            else:  # Если x в 1 степени
                if (maxSt < 1):
                    maxSt = 1
    return maxSt  # Если x ов нигде не было вернёт 0

