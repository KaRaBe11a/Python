def rasp(mnog): # функция распила многочлена на отдельные члены возвращает list(list(str))
    buf = list()
    razrez = list()
    count = 0
    bufStr = str()
    i = 0
    while (i<len(mnog)-1): # идём по строке многочлена                                       
        if(mnog[i] == "+")or(mnog[i] == "-")or(i == 0): # если сивол = + или - или это первый символ            
            buf.append(mnog[i]) #закидываем этот символ в буферный лист
            i = i+1                                                
            while(mnog[i]!="+")and(mnog[i]!="-")and(i<len(mnog)-1): # идём до + или до - иди до конца строки
                buf.append(mnog[i]) # записываем эту часть в буферный лист
                i = i+1                                            
            bufStr = "".join(buf) # буферный лист преобразуем в строку
            razrez.append(list(bufStr)) # закидываем эту строку в основной лист
            count = count+1 # считаем количество отдельных членов многочлена
            buf.clear() # чистим буферный лист
    razrez[count-1].append(mnog[len(mnog)-1]) # КОСТЫЛЬ записываем в конец последний символ из строки 
    return razrez # вернёт list(list(str)) аля [['x', '^', '2'], ['+', 'x'], ['+', '1']] 
