from Z8 import MUL_ZZ_Z
from drob import razbil_drob
def DIV_QQ_Q(drob_1:str, drob_2:str):
	a = razbil_drob(drob_1)
	b = razbil_drob(drob_2)
	umn_chisl = MUL_ZZ_Z(int(a[0]), int(b[1]))
	umn_znam = MUL_ZZ_Z(a[1], b[0])
	zxc = str(umn_chisl) + '/' + str(umn_znam)
	return zxc


