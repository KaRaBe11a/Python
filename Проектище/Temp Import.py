from P4 import MUL_Pxk_P
from P5 import LED_P_Q
from P6 import DEG_P_N
import P6

print("1 - Умножение на x^k")
print("2 - Старший коэфициент многочлена")
print("3 - Степень многочлена")
choice = int(input())
if(choice == 1):
    print("Введите многочлен аля x^2+x+1 ")
    mnog = str(input())
    print("Введите стпень на которую умножать x^ ")
    step = int(input())
    result = MUL_Pxk_P(mnog, step)
    print("Результат", result)
if(choice == 2):
    print("Введите многочлен")
    mnog = str(input())
    result = LED_P_Q(mnog)
    print("Результат", result)
if(choice == 3):
    print("Введите многочлен")
    mnog = str(input())
    result = DEG_P_N(mnog)
    print("Результат", result)