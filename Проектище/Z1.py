def ABS_Z_N(number):  # Z-1 Абсолютная величина числа, результат - натуральное
    if number > 0:
        return int(number)
    if number < 0:
        number = number * -1
        return int(number)
