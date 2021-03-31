def INT_Q_B(a:float):
    string = str(a)
    j = len(string)-1
    while(j>0 and string[j] != "."):
        if(string[j] != "0"):
            return 0
        j = j-1
    return 1
