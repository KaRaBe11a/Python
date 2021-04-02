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
