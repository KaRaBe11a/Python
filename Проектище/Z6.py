from Z1 import ABS_Z_N  # Абсолютная величина числа, результат - натуральное
from Z2 import POS_Z_D  # Определение положительности числа (2 - положительное, 0 — равное нулю, 1 - отрицательное)
from N1_12 import COM_NN_D  # Сравнение натуральных чисел: 2 - если первое больше второго, 0, если равно, 1 иначе.
from N1_12 import ADD_NN_N  # Сложение натуральных чисел
from N1_12 import SUB_NN_N  # Вычитание из первого большего натурального числа второго меньшего или равного
from Z3 import MUL_ZM_Z  # Умножение целого на (-1)


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