def COM_NN_D (x, y):    # Определение: какое число больше из двух, или они равны
    if (x > y):
        return 2
    if (x == y):
        return 0
    return 1


def NZER_N_B (x):      # Определение: равно лли число 0 или нет
    if (x != 0):
        return 1
    return 0

def ADD_1N_N (x):    # Добвление к числу 1
    x = x + 1
    return x

def ADD_NN_N (x, y):   # Сумма двух чисел
    return (x + y)


def SUB_NN_N (x, y):            # Вычитание из большего числа меньшее
    if (COM_NN_D(x, y) == 2):
        return (x - y)
    if (COM_NN_D(x, y) == 0):
        return 0
    if (COM_NN_D(x, y) == 1):
        return (y - x)


def MUL_ND_N (x, y):  # Умножение двух чисел
    return (x*y)

def MUL_Nk_N (x, k):   # Умножение числ на 10^k
    return (x*10**k)

def MUL_NN_N (x, y):    # Умножение натуральных чисел
    return x*y

def SUB_NDN_N (x, y, z):
    z = MUL_ND_N(z, y)    # Произведение z на y
    if (z > 0):      # Если z получилось положительным, то возврат вычитания из большего числа меньшее
        return SUB_NN_N (x, y)
    return None   # Если z отрицательное, то возврат None



def DIV_NN_Dk (x, y):
    k = 0
    if (COM_NN_D (x, y) == 2):  #  Если x больше y, тогда z присваивается деление x напроизведение y на 10^k
        z = x / MUL_Nk_N (y, k)
    if (COM_NN_D (x, y) == 1):    #  Если y больше x, тогда z присваивается деление y напроизведение x на 10^k
        z = y / MUL_Nk_N(x, k)
    if (COM_NN_D(x, y) == 0):   # Если x равен y, тогда возврат 1
        return 1
    return int(str(z)[0])  # Возврат первой цифры числа - результата верхних вычислений

def DIV_NN_N (x, y):
    if(COM_NN_D(x, y) == 2):    #  Если x больше y, тогда z присваивается чатсное от деления x на y
        z = x // y
    if(COM_NN_D(x ,y) == 1):    #  Если y больше x, тогда z присваивается частное от деления y на x
        z = y // x
    if (COM_NN_D(x, y) == 0):   # Если x равен y, тогда возврат 1
        return 1
    return z    # Возврат частного от деления


def MOD_NN_N (x, y):
    if(COM_NN_D(x, y) == 2):    #  Если x больше y, тогда z присваивается остаток от деления x на y
        z = x % y
    if(COM_NN_D(x ,y) == 1):    #  Если y больше x, тогда z присваивается остаток от деления y на x
        z = y % x
    if (COM_NN_D(x, y) == 0):   # Если x равен y, тогда возврат 0
        return 0
    return z    # Возврат остатка от деления

