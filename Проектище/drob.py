def razbil_drob(drob:str):
	i = 0
	chisletel = ''
	znamenatel = ''
	j = len(drob)
	
	while (i < j and drob[i] != '/'):
		chisletel +=  drob[i]
		i += 1
	i += 1
	while (i < j):
		znamenatel += drob[i]
		i += 1
	return chisletel, znamenatel


