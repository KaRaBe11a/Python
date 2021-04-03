from Z2 import POS_Z_D # Определение положительности числа 2+ 1- 0-0
from Z1 import ABS_Z_N # Абсолютная величина числа
from N1_12 import MUL_NN_N # Умножение натуральных чисел
from Z3 import MUL_ZM_Z # умножение целого на -1


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

