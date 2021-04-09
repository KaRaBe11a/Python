from raspil import rasp
from math import gcd
from math import lcm
from functools import  reduce
from Q3 import TRANS_Z_Q


def razb_koef(koef: str):
    chislitel = str()
    znam = str()
    if koef.find(".") != -1:
        koef = TRANS_Z_Q(koef)
    if koef.find("/") != -1:
        idDel = koef.find("/")
        for i in range(0, idDel):
            chislitel += koef[i]
        for i in range(idDel+1, len(koef)):
            znam += koef[i]
    else:
        chislitel = koef
        znam = "1"
    return chislitel, znam



def FAC_P_Q(mnog: str):
    razrez = rasp(mnog)

    chislitels = list()
    znams = list()
    koefs = list()

    """
    Запишем в массив все коэфициенты многочлена
    """
    bufStr = str()
    bufKoef = str()
    bufChisl = str()
    bufZnam = str()
    for i in range(len(razrez)):

        if razrez[i].count("x") == 1: #Если в многочлене есть x
            bufStr = "".join(razrez[i])
            idX = bufStr.find("x")
            bufKoef = "".join(razrez[i][:idX])
            bufChisl, bufZnam = razb_koef(bufKoef)
            chislitels.append(int(bufChisl))
            znams.append(int(bufZnam))
        else:
            bufKoef = "".join(razrez[i])
            bufChisl, bufZnam = razb_koef(bufKoef)
            chislitels.append(int(bufChisl))
            znams.append(int(bufZnam))
    print("НОД числителей")
    print(chislitels)
    print(reduce(lambda x,y:gcd(x,y), chislitels))
    print("НОК знаменателей")
    print(znams)
    print(reduce(lambda x,y: lcm(x,y), znams))