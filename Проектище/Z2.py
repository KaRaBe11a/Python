def POS_Z_D(number):  # Z-2 Определение положительности числа (2 - положительное, 0 — равное нулю, 1 - отрицательное)
    if number > 0:
        return 2
    if number == 0:
        return 0
    if number < 0:
        return 1
