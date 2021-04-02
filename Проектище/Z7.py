from Z2 import POS_Z_D # Определение положительности числа 2+ 1- 00
from Z1 import ABS_Z_N # Абсолютная величина числа
from N1_10 import COM_NN_D # Сравнение натуральных x,y 2-x>y 1-y<x 0-x=y
from N1_10 import ADD_NN_N # Сложение натуральных
from N1_10 import SUB_NN_N # Вичитание из первого большего натурального второго меньшего или равного
from Z3 import MUL_ZM_Z #Умножение целого на -1

def SUB_ZZ_Z(number1 , number2): # Вычитание целых чисел
     num1 = int(number1)
     num2 = int(number2)

     if(POS_Z_D(num1) == 2 and POS_Z_D(num2) == 2): #Если пришло 2 положительных числа
         return num1-num2



     if(POS_Z_D(num1) == 1 and POS_Z_D(num2) == 2): #Если первое отрицательное а второе положительное
         num1 = ABS_Z_N(num1)
         return(MUL_ZM_Z(ADD_NN_N(num1, num2)))


     if(POS_Z_D(num1) == 2 and POS_Z_D(num2) == 1): #Если первое положительное а второе отрицательное
         return  ADD_NN_N(num1, ABS_Z_N(num2))

     if(POS_Z_D(num1) != 0 and POS_Z_D(num2) == 0): # Если первое не ноль а второе ноль
         return num1

     if(POS_Z_D(num1) == 0 and POS_Z_D(num2) != 0): # Если первое ноль а второе не ноль
         return MUL_ZM_Z(num2)

     if(POS_Z_D(num1) == 0 and POS_Z_D(num2) == 0): # Если оба ноль
         return 0

