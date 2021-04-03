from N1_12 import MOD_NN_N  # Остаток от деления большего натурального числа на меньшее или равное натуральное с остатком(делитель отличен от нуля)
from N1_12 import COM_NN_D  # Сравнение натуральных чисел: 2 - если первое больше второго, 0, если равно, 1 иначе
from N1_12 import NZER_N_B  # Проверка на ноль: если число не равно нулю, то «да» иначе «нет»

def GCF_NN_N(number_1, number_2):  # НОД натуральных чисел
    while NZER_N_B(number_1) and NZER_N_B(number_2) == 1:
        if COM_NN_D(number_1, number_2) == 2:
            number_1 = MOD_NN_N(number_1, number_2)
        else:
            number_2 = MOD_NN_N(number_2, number_1)

    return(number_1 + number_2)