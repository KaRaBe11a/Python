from raspil import rasp

def DER_P_P(mnog: str):
    razrez = list(rasp((mnog)))

    buffRazr = list()
    buffKoef = str()
    buffStep = str()
    buffZnak = str()
    for i in range(0, len(razrez)):
        buffRazr.clear()
        buffKoef = ""
        buffStep = ""
        if(razrez[i].count("x") == 1): #Если в этом члене есть x
            if(razrez[i].count("^") == 0): #Если x в первой степени

                j = 0
                while(razrez[i][j] != "x"): # Записываем коэфициент
                    buffKoef += razrez[i][j]
                    j += 1

                razrez[i].clear() # Чистим изначальный член
                if(buffKoef == ""): # в зависимости от того что лежит в коэфициенте добавляем то что нужно)))
                    razrez[i].append("1")
                if(buffKoef == "-"):
                    razrez[i].append("-1")
                if(buffKoef == "+"):
                    razrez[i].append("+1")
                if(buffKoef != "" and buffKoef != "-" and buffKoef != "+"):
                    for k in range(0, len(buffKoef)):
                        razrez[i].append(buffKoef[k])

            else: # Если x не в первой степени

                j = 0
                while(razrez[i][j] != "x"): # Взяли коэфициент
                    buffKoef+= razrez[i][j]
                    j+= 1

                if(buffKoef == "" or buffKoef == "+"): # Если коэфа нет значит он равен 1
                    buffKoef += "1"

                if(buffKoef == "-"):
                    buffKoef += "1"

                j += 2
                while(j<len(razrez[i])): # взяли степень
                    buffStep += razrez[i][j]
                    j += 1

                buffKoef = str( int( int(buffKoef) * int(buffStep) ) ) # Расчитали новый коэф
                buffStep = str( int( int(buffStep)-1 ) ) # расчитали новую степень

                buffZnak = razrez[i][0] #Запомнили что лежало в начале
                razrez[i].clear()
                if(buffZnak == "+"): #Если там был + то докидываем его так как преобразования в инт его теряет
                    razrez[i].append("+")

                for k in range(0, len(buffKoef)): #Закидываем всё остальное
                    razrez[i].append(buffKoef[k])

                if(int(buffStep) == 1): #Если степень стала 1
                    razrez[i].append("x")

                if(int(buffStep) > 1): # Если степень стала > 1
                    razrez[i].append("x")
                    razrez[i].append("^")
                    for k in range(0, len(buffStep)):
                        razrez[i].append(buffStep[k])

        else:
            razrez[i] = ""

    resStr = str()
    for i in range(0, len(razrez)):
        resStr += ("".join((razrez[i])))
    return resStr




