from raspil import rasp
from Q7 import MUL_QQ_Q
from Q5 import ADD_QQ_Q

def MUL_Pxk_P(mnog, step):
    razrez = list(rasp(mnog))

    for i in range(0, len(razrez)):  # идём по списку
        j = len(razrez[i]) - 1  # Всякие прикольные переменные
        bufInt = list()
        bufRazr = list()
        bufStr = str()
        bufStr2 = str()
        znach = int()
        if (razrez[i].count("x") == 1):  # Если в этом куске многочлена есть x

            if (razrez[i].count("^") == 0):  # если x в первой степент
                razrez[i].append("^")  # Закидываем туда знак степени
                razrez[i].append(str(ADD_QQ_Q(str(step), "1")))  # Закидываем степень +1 т.к. у нас уже 1ая
            else:  # Если x не в первой степени (Шо я написал я в ахуе)
                while (razrez[i][j] != "^"):  # Короче идём справо налево и записываем какая у нас степень
                    bufInt.append(razrez[i][j])
                    j = j - 1

                bufInt.reverse()  # Поскольку писали справа налево переварачиваем значени
                bufStr = "".join(bufInt)  # Перекидываем из list в str
                bufStr = ADD_QQ_Q(bufStr, str(step))

                for k in range(0, j):  # закидываем в буферный list всё что было до "^"
                    bufRazr.append(razrez[i][k])
                bufRazr.append("^")  # добавляем знак "^" (Да я знаю что можно было это сделать красивее)
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
    return resStr  # Поздравляю вы великолепны

