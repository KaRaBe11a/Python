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

	if int(delimoe) % int(delitel) == 0 :
		return 1
	return 0

