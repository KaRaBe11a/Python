from N13 import GCF_NN_N  # НОД натуральных чисел
from N1_12 import MUL_NN_N  # Умножение натуральных чисел

def LCM_NN_N (number_1, number_2):  # НОК натуральных чисел
    return int(MUL_NN_N(number_1, number_2) / GCF_NN_N(number_1, number_2))