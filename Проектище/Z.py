from N import COM_NN_D  # Сравнение натуральных чисел: 2 - если первое больше второго, 0, если равно, 1 иначе.
from N import ADD_NN_N  # Сложение натуральных чисел
from N import SUB_NN_N  # Вычитание из первого большего натурального числа второго меньшего или равного
from N import MUL_NN_N # Умножение натуральных чисел
from N import DIV_NN_N  # Частное от деления большего натурального числа на меньшее или равное натуральное с остатком(делитель отличен от нуля)


def ABS_Z_N(number):  # Z-1 Абсолютная величина числа, результат - натуральное
    if number > 0:
        return int(number)
    if number < 0:
        number = number * -1
        return int(number)

def POS_Z_D(number):  # Z-2 Определение положительности числа (2 - положительное, 0 — равное нулю, 1 - отрицательное)
    if number > 0:
        return 2
    if number == 0:
        return 0
    if number < 0:
        return 1

def MUL_ZM_Z(number):  # Z-3 Умножение целого на (-1)
    number = int(number) * -1
    return number

def TRANS_N_Z(number):  # Z-4 Преобразование натурального в целое
    return int(number)

def TRANS_Z_N(number):  # Z-5 Преобразование целого неотрицательного в натуральное
    return int(number)

def ADD_ZZ_Z(number_1, number_2):

    number_1 = int(number_1)
    number_2 = int(number_2)

    if COM_NN_D(abs(number_1), abs(number_2)) == 2:  # Если модуль первого числа больше второго

        if POS_Z_D(number_1) == 2:  # И оно положительное
            if POS_Z_D(number_2) == 2:  # И второе положительное
                return ADD_NN_N(int(ABS_Z_N(number_1)), int(ABS_Z_N(number_2)))
            if POS_Z_D(number_2) == 1:  # И второе отрицательное
                return SUB_NN_N(int(ABS_Z_N(number_1)), int(ABS_Z_N(number_2)))

        if POS_Z_D(number_1) == 1:  # И оно отрицательное
            if POS_Z_D(number_2) == 2:  # И второе положительное
                return MUL_ZM_Z(SUB_NN_N(int(ABS_Z_N(number_1)), int(ABS_Z_N(number_2))))
            if POS_Z_D(number_2) == 1:  # И второе отрицательное
                return MUL_ZM_Z(ADD_NN_N(int(ABS_Z_N(number_1)), int(ABS_Z_N(number_2))))

    if COM_NN_D(abs(number_1), abs(number_2)) == 1:  # Если модуль второго числа больше первого

        if POS_Z_D(number_2) == 2:  # И оно положительное
            if POS_Z_D(number_1) == 2:  # И первое положительное
                return ADD_NN_N(int(ABS_Z_N(number_1)), int(ABS_Z_N(number_2)))
            if POS_Z_D(number_1) == 1:  # И первое отрицательное
                return SUB_NN_N(int(ABS_Z_N(number_2)), int(ABS_Z_N(number_1)))

        if POS_Z_D(number_2) == 1:  # И второе отрицательное
            if POS_Z_D(number_1) == 2:  # И первое положительное
                return MUL_ZM_Z(SUB_NN_N(int(ABS_Z_N(number_2)), int(ABS_Z_N(number_1))))
            if POS_Z_D(number_2) == 1:  # И первое отрицательное
                return MUL_ZM_Z(ADD_NN_N(int(ABS_Z_N(number_1)), int(ABS_Z_N(number_2))))

    if COM_NN_D(abs(number_1), abs(number_2)) == 0:  # Если модуль второго числа равен модулю первого первого числа
        if POS_Z_D(number_1) & POS_Z_D(number_2) == 2:  # Если оба положительные
            return ADD_NN_N(int(ABS_Z_N(number_1)), int(ABS_Z_N(number_2)))
        if POS_Z_D(number_1) & POS_Z_D(number_2) == 1:  # Если оба трицательные
            return MUL_ZM_Z(ADD_NN_N(int(ABS_Z_N(number_1)), int(ABS_Z_N(number_2))))
        if POS_Z_D(number_1) & POS_Z_D(number_2) == 0:  # Если оба равны нулю
            return 0

    if POS_Z_D(number_1) == 0:
        return number_2
    if POS_Z_D(number_2) == 0:
        return number_1


def SUB_ZZ_Z(number1, number2):  # Вычитание целых чисел
    num1 = int(number1)
    num2 = int(number2)

    if (POS_Z_D(num1) == 2 and POS_Z_D(num2) == 2):  # Если пришло 2 положительных числа
        return num1 - num2

    if (POS_Z_D(num1) == 1 and POS_Z_D(num2) == 2):  # Если первое отрицательное а второе положительное
        num1 = ABS_Z_N(num1)
        return (MUL_ZM_Z(ADD_NN_N(num1, num2)))

    if (POS_Z_D(num1) == 2 and POS_Z_D(num2) == 1):  # Если первое положительное а второе отрицательное
        return ADD_NN_N(num1, ABS_Z_N(num2))

    if (POS_Z_D(num1) != 0 and POS_Z_D(num2) == 0):  # Если первое не ноль а второе ноль
        return num1

    if (POS_Z_D(num1) == 0 and POS_Z_D(num2) != 0):  # Если первое ноль а второе не ноль
        return MUL_ZM_Z(num2)

    if (POS_Z_D(num1) == 0 and POS_Z_D(num2) == 0):  # Если оба ноль
        return 0

def MUL_ZZ_Z(number1, number2): # принимает выражения вида x.y

    countNegatives = 0

    num1 = int(number1)
    num2 = int(number2)

    if(POS_Z_D(num1) == 1): #Проверяем числа на отрицательность если да берём модуль и +1 к количству отрицательных
        num1 = ABS_Z_N(num1)
        countNegatives += 1
    if(POS_Z_D(num2) == 1):

        num2 = ABS_Z_N(num2)
        countNegatives += 1
    numResult = MUL_NN_N(num1, num2) #Перемножаем числа
    if(countNegatives == 1): # Если кол-во отрицательных = 1 то домнажаем число на -1
        numResult = MUL_ZM_Z(numResult)
    return numResult

def DIV_ZZ_Z(number_1, number_2):  # Частное от деления целого на целое (делитель отличен от нуля)
    int(number_1)
    int(number_2)

    if POS_Z_D(number_2) == 0:   # Если делитель ноль выдать ошибку
        return -1

    if POS_Z_D(number_1) == 0:   # Если делимое ноль выдать ноль
        return 0

    if (POS_Z_D(number_1) == 1) and (POS_Z_D(number_2) == 1):  # Если оба отрицательные
        return int(DIV_NN_N(ABS_Z_N(number_1), ABS_Z_N(number_2)))

    if (POS_Z_D(number_1) == 2) and (POS_Z_D(number_2) == 2):  # Если оба положительные
        return int(DIV_NN_N(ABS_Z_N(number_1), ABS_Z_N(number_2)))

    if (POS_Z_D(number_1) == 2) or (POS_Z_D(number_2) == 1):  # Если делитель отрицательный
        return int(-1 * DIV_NN_N(ABS_Z_N(number_1), ABS_Z_N(number_2)))

    if (POS_Z_D(number_1) == 1) or (POS_Z_D(number_2) == 2):  # Если делимое отрицательный
        return int(-1 * DIV_NN_N(ABS_Z_N(number_1), ABS_Z_N(number_2)))

def MOD_ZZ_Z(number_1, number_2):  # Остаток от деления целого на целое(делитель отличен от нуля)
    int(number_1)
    int(number_2)

    if number_2 == 0:  # Если делитель ноль то выдать ошибку
        return -1

    if number_1 == 0:  # Если делимое ноль то выдать делитель
        return number_2

    if number_2 < 0:  # Если делитель отрицательный то выдать делитель
        return number_2

    output = DIV_ZZ_Z(abs(number_1), number_2)
    output = MUL_ZZ_Z(output, number_2)
    output = SUB_ZZ_Z(abs(number_1), output)

    if number_1 > 0:
        return output
    if number_1 < 0:
        return MUL_ZM_Z(output)