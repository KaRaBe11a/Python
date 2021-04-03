from raspil import rasp
from SRAVN_Q import  SRAVN_Q

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

