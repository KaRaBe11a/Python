import P4
import P5
import P6

print("1 - Умножение на x^k")
print("2 - Старший коэфициент многочлена")
print("3 - Степень многочлена")
choice = int(input)
if(choice == 1):
    print("Введите многочлен аля x^2+x+1 ")
    mnog = str(input())
    print("Введите стпень на которую умножать x^ ")
    step = int(input())
    result = P4.MUL_Pxk_P(mnog, step)
    print("Результат", result)
if(choice == 2):
    print("Введите многочлен")
    mnog = str(input())
    result = P5.LED_P_Q(mnog)
    print("Результат", result)
if(choice == 3):
    print("Введите многочлен")
    mnog = str(input())
    result = P6.DEG_P_N(mnog)
    print("Результат", result)