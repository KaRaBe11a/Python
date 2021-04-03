from P1 import ADD_PP_P
from P3 import MUL_PQ_P

def SUB_PP_P(mnog1: str, mnog2: str):
    mnog2 = MUL_PQ_P(mnog2, "-1") # домнажаем второй многочлен на -1
    return ADD_PP_P(mnog1, mnog2) # складываем многочлены
