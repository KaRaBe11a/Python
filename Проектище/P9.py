from P2 import SUB_PP_P
from P8 import MULL_PP_P
from P6 import DEG_P_N
from P3 import MUL_PQ_P
from raspil import rasp
from SRAVN_Q import SRAVN_Q
def DIV_PP_P(mnog1: str, mnog2: str):

    razrez1 = rasp(mnog1)
    razrez2 = rasp(mnog2)

    Delimoe = mnog1
    Delitel = mnog2
    Ostatok = ""
    while SRAVN_Q(DEG_P_N(Delimoe), DEG_P_N(Delitel)) == 2:
        pass
