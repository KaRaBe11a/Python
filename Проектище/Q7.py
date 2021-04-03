from Z8 import MUL_ZZ_Z
from drob import razbil_drob
from Q3 import TRANS_Z_Q
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
