from N import GCF_NN_N
from N import COM_NN_D # сравнение натуральных чисел
from Z import DIV_ZZ_Z
from Z import MUL_ZZ_Z # Умножение целых чисел
from Z import ADD_ZZ_Z # Сложение целых чисел
from Z import SUB_ZZ_Z #Вычитание целых

def RED_Q_Q(drob:str):
	a = razbil_drob(drob)
	k = GCF_NN_N(int(a[0]), int(a[1]))
	zxc = (str(DIV_ZZ_Z(int(a[0]), k))) + '/' + str(DIV_ZZ_Z(int(a[1]), k))
	return zxc


def INT_Q_B(drob: str):
	j = len(drob)-1
	i = 0
	delimoe = str()
	delitel = str()
	while i < j and drob[i] != "/":
		delimoe += drob[i]
		i = i+1
	i = i+1
	while i < j:
		delitel += drob[i]
		i = i+1
	if(delitel == ""):
		delitel += "1"
	if int(delimoe) % int(delitel) == 0 :
		return 1
	return 0

def TRANS_Z_Q(number: str):
    if(number.count(".") == 0): #Если число целое
        return number+"/1"

    integerPart = str()
    floatPart = str()
    j = 0

    while(number[j] != "."):  # Берём целую часть
        integerPart += number[j]
        j += 1

    i = len(number)-1
    j += 1
    razr = 0
    while(j<=i): # берём дробную часть
        floatPart += number[j]
        razr += 1
        j+=1

    if(floatPart.count("0") == len(floatPart)): #Если дробная часть = 0
        return int(integerPart)

    countZero = 0
    F = False
    for k in range(0, razr): # Убираем из дробной части начальные нули
        if(floatPart[k] != "0"):
            F = True
            break;
        if (F == False):
            countZero += 1

    newFloatPart = str()
    for k in range(countZero, razr):
        newFloatPart += floatPart[k]


    floatDelitel = str()
    floatDelitel += "1"
    for k in range(0, razr): # собираем делитель дробной части
        floatDelitel += "0"

    result = str()
    integerPart = int(int(integerPart)*int(floatDelitel))
    integerPart = integerPart + int(floatPart)
    result += str(integerPart)+"/"+floatDelitel
    return result

def TRANS_Q_Z(number: str):
    if(number.count("/") == 0):
        return  int(number)

    delimoe = str()
    delitel = str()

    j = 0
    while(number[j] != "/"):
        delimoe += number[j]
        j += 1
    j += 1
    while(j<len(number)):
        delitel += number[j]
        j += 1
    if(delitel == "1"):
        return int(delimoe)
    print("знаменатель не равен 1")
    return -1

def ADD_QQ_Q(drob_1: str , drob_2: str):
    if(drob_1.count(".") == 1):
        drob_1 = TRANS_Z_Q(drob_1)
    if(drob_2.count(".") == 1):
        drob_2 = TRANS_Z_Q(drob_2)

    a = razbil_drob(drob_1)
    b = razbil_drob(drob_2)

    chisle1 = str(MUL_ZZ_Z(a[0], b[1]))
    chisle2 = str(MUL_ZZ_Z(a[1], b[0]))

    addChisl = ADD_ZZ_Z(chisle1, chisle2)
    addZnam = MUL_ZZ_Z(a[1], b[1])
    if(int(addChisl)%int(addZnam) == 0):
        return str(int(int(addChisl)/int(addZnam)))

    zxc = str(addChisl)+"/"+str(addZnam)
    return zxc

def SUB_QQ_Q(drob_1: str, drob_2: str):
    if (drob_1.count(".") == 1):
        drob_1 = TRANS_Z_Q(drob_1)

    if (drob_2.count(".") == 1):
        drob_2 = TRANS_Z_Q(drob_2)

    a = razbil_drob(drob_1)
    b = razbil_drob(drob_2)

    chisle_1 = MUL_ZZ_Z(a[0], b[1])
    chisle_2 = MUL_ZZ_Z(a[1], b[0])

    sub_chisle = SUB_ZZ_Z(chisle_1, chisle_2)
    sub_znam = MUL_ZZ_Z(a[1], b[1])


    if (int(sub_chisle) % int(sub_znam) == 0):
        return str(int(sub_chisle) / int(sub_znam))

    zxc = str(sub_chisle) + '/' + str(sub_znam)
    return zxc

def MUL_QQ_Q(drob_1:str, drob_2:str):
	if(drob_1.count(".") == 1):
		drob_1 = TRANS_Z_Q(drob_1)

	if(drob_2.count(".") == 1):
		drob_2 = TRANS_Z_Q(drob_2)

	a = razbil_drob(drob_1)
	b = razbil_drob(drob_2)

	umn_chisl = MUL_ZZ_Z(int(a[0]), int(b[0]))
	umn_znam = MUL_ZZ_Z(a[1], b[1])

	if(int(umn_chisl)%int(umn_znam) == 0):
		return str(int(umn_chisl)/int(umn_znam))

	zxc = str(umn_chisl) + '/' + str(umn_znam)
	return zxc

def DIV_QQ_Q(drob_1:str, drob_2:str):
	a = razbil_drob(drob_1)
	b = razbil_drob(drob_2)
	umn_chisl = MUL_ZZ_Z(int(a[0]), int(b[1]))
	umn_znam = MUL_ZZ_Z(a[1], b[0])
	zxc = str(umn_chisl) + '/' + str(umn_znam)
	return zxc


def razbil_drob(drob: str):
    i = 0
    chisletel = ''
    znamenatel = ''
    drob = str(drob)
    j = len(drob)

    while (i < j and drob[i] != '/'):
        chisletel += drob[i]
        i += 1
    i += 1
    while (i < j):
        znamenatel += drob[i]
        i += 1
    if (znamenatel == ""):
        znamenatel += "1"
    return chisletel, znamenatel

def SRAVN_Q(drob_1:str, drob_2:str):
    # Приводим рациональное число к общему виду x/y
    if(drob_1.count(".") == 1):
        drob_1 = TRANS_Z_Q(drob_1)
    if(drob_2.count(".") == 1):
        drob_2 = TRANS_Z_Q(drob_2)

    a = razbil_drob(drob_1)
    b = razbil_drob(drob_2)
    chisle1 = MUL_ZZ_Z(a[0], b[1])
    chisle2 = MUL_ZZ_Z(a[1], b[0])
    countNegativ = 0

    result = COM_NN_D(int(chisle1), int(chisle2))
    return result # 2-первое больше 1-второе больше первого 0-равны