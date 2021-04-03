from Z1 import ABS_Z_N
from N13 import GCF_NN_N
from Z9 import DIV_ZZ_Z
from drob import razbil_drob

def RED_Q_Q(drob:str):
	a = razbil_drob(drob)
	k = GCF_NN_N(int(a[0]), int(a[1]))
	zxc = (str(DIV_ZZ_Z(int(a[0]), k))) + '/' + str(DIV_ZZ_Z(int(a[1]), k))
	return zxc
print(RED_Q_Q("9/18"))