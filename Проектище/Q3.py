
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

print(TRANS_Z_Q("10.0"))


