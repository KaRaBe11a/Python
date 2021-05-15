from tkinter import *
from tkinter import messagebox
import Refactoring as f1
import RefactoringP as f2
import RefactoringQ as f3
import RefactoringZ as f4



def razbil_ch(drob:str):
	i = 0
	chisletel = ''
	znamenatel = ''
	j = len(drob)
	
	while (drob[i] != ' '):
		chisletel +=  drob[i]
		i += 1
	i += 1 
	znamenatel = drob[i:]
	return chisletel, znamenatel




def btn_1():

	def clc(ch:int):
		qwe = [f1.COM_NN_D, f1.NZER_N_B, f1.ADD_1N_N, f1.SUB_NN_N, f1.ADD_NN_N, f1.MUL_ND_N,
		f1.MUL_Nk_N, f1.MUL_NN_N, f1.SUB_NDN_N, f1.DIV_NN_Dk, f1.DIV_NN_N, 
		f1.MOD_NN_N, f1.GCF_NN_N, f1.LCM_NN_N]
		
		a = Input.get()
		if (ch == 1 or ch == 2):
			try:
				info['text'] = f'{str(qwe[ch](int(a)))}'
			except:
				info['text'] = 'Error'
		elif (ch == 8):
			try:
				zxc.split()
				map(int,zxc.split())
				a, b, c = map(int,zxc.split())
				info['text'] = f'{str(qwe[ch](int(a), int(b), int(c)))}'
			except:
				info['text'] = 'Error'
		else:
			try:
				zxc = razbil_ch(a)
				info['text'] = f'{str(qwe[ch](int(zxc[0]), int(zxc[1])))}'
			except:
				info['text'] = 'Error'

	flag = None

	win.withdraw()
	children = Toplevel(win)
	children.overrideredirect(flag==None)
	children['bg'] = '#F7C52B'
	children.title("Натуральные числа с 0")
	#children.geometry("1200x800+300+100")
	w = win.winfo_screenwidth()
	h = win.winfo_screenheight()
	w = w//2 # середина экрана
	h = h//2 
	w = w - 575 # смещение от середины
	h = h - 400
	children.geometry('1150x800+{}+{}'.format(w, h))
	children.resizable(width=False, height=False)

	back = Button(children, text='Назад', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda: (children.destroy(), win.deiconify()), background = "#FF9914").grid(row=0, column=0)
	b1 = Button(children, background = "#FF9914", text='Сравнение натуральных чисел', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(0)).grid(row=1, column=0, stick='wens', padx=15, pady=15)
	b2 = Button(children, background = "#FF9914", text='Проверка на ноль', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(1)).grid(row=1, column=1, stick='wens', padx=15, pady=15)
	b3 = Button(children, background = "#FF9914", text='Добавление 1 к натуральному числу', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(2)).grid(row=1, column=2, stick='wens', padx=15, pady=15)
	b4 = Button(children, background = "#FF9914", text='Вычитание из большего меньшее', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(3)).grid(row=2, column=0, stick='wens', padx=15, pady=15)
	b5 = Button(children, background = "#FF9914", text='Сложение натуральных чисел', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(4)).grid(row=2, column=1, stick='wens', padx=15, pady=15)
	b6 = Button(children, background = "#FF9914", text='Умножение натурального числа на цифру', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(5)).grid(row=2, column=2, stick='wens', padx=15, pady=15)
	b7 = Button(children, background = "#FF9914", text='Умножение натурального числа на 10^k', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(6)).grid(row=3, column=0, stick='wens', padx=15, pady=15)
	b8 = Button(children, background = "#FF9914", text='Умножение натуральных чисел', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(7)).grid(row=3, column=1, stick='wens', padx=15, pady=15)
	b9 = Button(children, background = "#FF9914", text='Вычитание из натурального другого натурального, \nумноженного на цифру для случая с \nнеотрицательным результатом', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(8)).grid(row=3, column=2, stick='wens', padx=15, pady=15)
	b10 = Button(children, background = "#FF9914", text='Вычисление первой цифры деления большего \nнатурального на меньшее, домноженное на 10^k', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(9)).grid(row=4, column=0, stick='wens', padx=15, pady=15)
	b11 = Button(children, background = "#FF9914", text='Частное от деления большего натурального числа \n на меньшее', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(10)).grid(row=4, column=1, stick='wens', padx=15, pady=15)
	b12 = Button(children, background = "#FF9914", text='Остаток от деления большего натурального числа \nна меньшее', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(11)).grid(row=4, column=2, stick='wens', padx=15, pady=15)
	b13 = Button(children, background = "#FF9914", text='НОД натуральных чисел', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(12)).grid(row=5, column=0, stick='wens', padx=15, pady=15)
	b14 = Button(children, background = "#FF9914", text='НОК натуральных чисел', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(13)).grid(row=5, column=1, stick='wens', padx=15, pady=15)
	
	close = Button(children, background = "#FF9914", text='Выход)', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = '#6823E1', command=win.destroy).grid(row=5, column=2, padx=15, pady=15)

	info = Label(children, text='Вывод', bg='#F7C52B', font=40)
	info.grid(row=0, column=2, sticky=W)

	mainFrame = Frame(children)
	mainFrame.grid()
	
	
	Input=Entry(children, bg='white', font='Times 15')
	Input.grid(row=0, column=1, stick='wens', padx=15, pady=40, sticky='we')

	
def btn_2():
	def clc(ch:int):
		qwe = [f4.ABS_Z_N, f4.POS_Z_D, f4.MUL_ZM_Z, f4.TRANS_N_Z, f4.TRANS_Z_N, 
		f4.ADD_ZZ_Z, f4.SUB_ZZ_Z, f4.MUL_ZZ_Z, f4.DIV_ZZ_Z, f4.MOD_ZZ_Z]
		
		a = Input.get()
		if (ch < 5):
			try:
				info['text'] = f'{str(qwe[ch](int(a)))}'
			except:
				info['text'] = 'Error'
		else:
			try:
				zxc = razbil_ch(a)
				info['text'] = f'{str(qwe[ch](int(zxc[0]), int(zxc[1])))}'
			except:
				info['text'] = 'Error'

	flag = None

	win.withdraw()
	children = Toplevel(win)
	children.overrideredirect(flag==None)
	children['bg'] = '#F7C52B'
	children.title("Целые числа")
	#children.geometry("1200x800+300+100")
	w = win.winfo_screenwidth()
	h = win.winfo_screenheight()
	w = w//2 # середина экрана
	h = h//2 
	w = w - 575 # смещение от середины
	h = h - 400
	children.geometry('1150x800+{}+{}'.format(w, h))
	children.resizable(width=False, height=False)

	back = Button(children, text='Назад', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda: (children.destroy(), win.deiconify()), background = "#FF9914").grid(row=0, column=0)
	b1 = Button(children, background = "#FF9914", text='Абсолютная величина числа', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(0)).grid(row=1, column=0, stick='wens', padx=15, pady=15)
	b2 = Button(children, background = "#FF9914", text='Определение положительности числа', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(1)).grid(row=1, column=1, stick='wens', padx=15, pady=15)
	b3 = Button(children, background = "#FF9914", text='Умножение целого на (-1)', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(2)).grid(row=1, column=2, stick='wens', padx=15, pady=15)
	b4 = Button(children, background = "#FF9914", text='Преобразование натурального в целое', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(3)).grid(row=2, column=0, stick='wens', padx=15, pady=15)
	b5 = Button(children, background = "#FF9914", text='Преобразование целого неотрицательного \nв натуральное', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(4)).grid(row=2, column=1, stick='wens', padx=15, pady=15)
	b6 = Button(children, background = "#FF9914", text='Сложение целых чисел', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(5)).grid(row=2, column=2, stick='wens', padx=15, pady=15)
	b7 = Button(children, background = "#FF9914", text='Вычитание целых чисел', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(6)).grid(row=3, column=0, stick='wens', padx=15, pady=15)
	b8 = Button(children, background = "#FF9914", text='Умножение целых чисел', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(7)).grid(row=3, column=1, stick='wens', padx=15, pady=15)
	b9 = Button(children, background = "#FF9914", text='Частное от деления целого на целое \n(делитель отличен от нуля)', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(8)).grid(row=3, column=2, stick='wens', padx=15, pady=15)
	b10 = Button(children, background = "#FF9914", text='Остаток от деления целого на целое\n(делитель отличен от нуля)', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(9)).grid(row=4, column=0, stick='wens', padx=15, pady=15)
	
	
	close = Button(children, background = "#FF9914", text='Выход)', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = '#6823E1', command=win.destroy).grid(row=4, column=2, padx=15, pady=15)

	info = Label(children, text='Вывод', bg='#F7C52B', font=40)
	info.grid(row=0, column=2, sticky=W)

	mainFrame = Frame(children)
	mainFrame.grid()
	
	
	Input=Entry(children, bg='white', font='Times 15')
	Input.grid(row=0, column=1, stick='wens', padx=15, pady=40, sticky='we')
	

	


def btn_3():
	def clc(ch:int):
		qwe = [f3.RED_Q_Q, f3.INT_Q_B, f3.TRANS_Z_Q, f3.TRANZ_Q_Z, 
		f3.ADD_QQ_Q, f3.SUB_QQ_Q, f3.MUL_QQ_Q, f3.DIV_QQ_Q]
		
		a = Input.get()
		if (ch < 4):
			try:
				info['text'] = f'{str(qwe[ch](str(a)))}'
			except:
				info['text'] = 'Error'
		else:
			try:
				zxc = razbil_ch(a)
				info['text'] = f'{str(qwe[ch](str(zxc[0]), str(zxc[1])))}'
			except:
				info['text'] = 'Error'

	flag = None

	win.withdraw()
	children = Toplevel(win)
	children.overrideredirect(flag==None)
	children['bg'] = '#F7C52B'
	children.title("Рациональные числа (дроби)")
	#children.geometry("1200x800+300+100")
	w = win.winfo_screenwidth()
	h = win.winfo_screenheight()
	w = w//2 # середина экрана
	h = h//2 
	w = w - 575 # смещение от середины
	h = h - 400
	children.geometry('1150x800+{}+{}'.format(w, h))
	children.resizable(width=False, height=False)

	back = Button(children, text='Назад', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda: (children.destroy(), win.deiconify()), background = "#FF9914").grid(row=0, column=0)
	b1 = Button(children, background = "#FF9914", text='Сокращение дроби', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(0)).grid(row=1, column=0, stick='wens', padx=15, pady=15)
	b2 = Button(children, background = "#FF9914", text='Проверка на целое, \nесли рациональное число является целым', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(1)).grid(row=1, column=1, stick='wens', padx=15, pady=15)
	b3 = Button(children, background = "#FF9914", text='Преобразование целого в дробное', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(2)).grid(row=1, column=2, stick='wens', padx=15, pady=15)
	b4 = Button(children, background = "#FF9914", text='Преобразование дробного в целое \n(если знаменатель равен 1)', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(3)).grid(row=2, column=0, stick='wens', padx=15, pady=15)
	b5 = Button(children, background = "#FF9914", text='Сложение дробей', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(4)).grid(row=2, column=1, stick='wens', padx=15, pady=15)
	b6 = Button(children, background = "#FF9914", text='Вычитание дробей', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(5)).grid(row=2, column=2, stick='wens', padx=15, pady=15)
	b7 = Button(children, background = "#FF9914", text='Умножение дробей', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(6)).grid(row=3, column=0, stick='wens', padx=15, pady=15)
	b8 = Button(children, background = "#FF9914", text='Деление дробей\n(делитель отличен от нуля)', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(7)).grid(row=3, column=1, stick='wens', padx=15, pady=15)

	close = Button(children, background = "#FF9914", text='Выход)', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = '#6823E1', command=win.destroy).grid(row=3, column=2, padx=15, pady=15)

	info = Label(children, text='Вывод', bg='#F7C52B', font=40)
	info.grid(row=0, column=2, sticky=W)

	mainFrame = Frame(children)
	mainFrame.grid()
	
	
	Input=Entry(children, bg='white', font='Times 15')
	Input.grid(row=0, column=1, stick='wens', padx=15, pady=40, sticky='we')
	
def btn_4():
	win.withdraw()
	children = Toplevel(win)
	children.overrideredirect(flag==None)
	children['bg'] = '#F7C52B'
	children.title("Рациональные числа (дроби)")
	#children.geometry("1200x800+300+100")


	def clc(ch:int):
		qwe = [f2.ADD_PP_P, f2.SUB_PP_P, f2.MUL_PQ_P, f2.MUL_Pxk_P, f2.LED_P_Q, f2.DEG_P_N,
		f2.FAC_P_Q, f2.MUL_PP_P, f2.DER_P_P, f2.DIV_MOD_PP_P,  f2.GCF_PP_P, f2.NMR_P_P]
		
		a = Input.get()
		if (4 <= ch <= 5) or (ch == 8) or (ch == 11):
			try:
				info['text'] = f'{str(qwe[ch](str(a)))}'
			except:
				info['text'] = 'Error'
		elif (ch == 9):
			try:
				zxc = razbil_ch(a)
				t = qwe[ch](str(zxc[0]), str(zxc[1]))
				info['text'] ='частное = ' + t[0] + ' остаток = ' + t[1]
			except:
				info['text'] = 'Error'
		elif (ch == 6):
			try:
				t = str(qwe[ch](str(a)))
				info['text'] = "НОД = " + t[1] + " НОК = " + t[4]
			except:
				info['text'] = 'Error'
		else:
			try:
				zxc = razbil_ch(a)
				info['text'] = f'{str(qwe[ch](str(zxc[0]), str(zxc[1])))}'
			except:
				info['text'] = 'Error'

	w = win.winfo_screenwidth()
	h = win.winfo_screenheight()
	w = w//2 # середина экрана
	h = h//2 
	w = w - 575 # смещение от середины
	h = h - 400
	children.geometry('1150x800+{}+{}'.format(w, h))
	children.resizable(width=False, height=False)

	back = Button(children, text='Назад', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda: (children.destroy(), win.deiconify()), background = "#FF9914").grid(row=0, column=0)
	b1 = Button(children, background = "#FF9914", text='Сложение многочленов', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(0)).grid(row=1, column=0, stick='wens', padx=15, pady=15)
	b2 = Button(children, background = "#FF9914", text='Вычитание многочленов', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(1)).grid(row=1, column=1, stick='wens', padx=15, pady=15)
	b3 = Button(children, background = "#FF9914", text='Умножение многочлена на \nрациональное число', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(2)).grid(row=1, column=2, stick='wens', padx=15, pady=15)
	b4 = Button(children, background = "#FF9914", text='Умножение многочлена на x^k', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(3)).grid(row=2, column=0, stick='wens', padx=15, pady=15)
	b5 = Button(children, background = "#FF9914", text='Старший коэффициент многочлена', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(4)).grid(row=2, column=1, stick='wens', padx=15, pady=15)
	b6 = Button(children, background = "#FF9914", text='Степень многочлена', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(5)).grid(row=2, column=2, stick='wens', padx=15, pady=15)
	b7 = Button(children, background = "#FF9914", text='Вынесение из многочлена НОК знаменателей \nкоэффициентов и НОД числителей', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(6)).grid(row=3, column=0, stick='wens', padx=15, pady=15)
	b8 = Button(children, background = "#FF9914", text='Умножение многочленов', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(7)).grid(row=3, column=1, stick='wens', padx=15, pady=15)
	b10 = Button(children, background = "#FF9914", text='Остаток и частное от деления многочлена на \nмногочлен при делении с остатком', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(9)).grid(row=4, column=0, stick='wens', padx=15, pady=15)
	b11 = Button(children, background = "#FF9914", text='НОД многочленов', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(10)).grid(row=4, column=1, stick='wens', padx=15, pady=15)
	b12 = Button(children, background = "#FF9914", text='Производная многочлена', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(8)).grid(row=3, column=2, stick='wens', padx=15, pady=15)
	b13 = Button(children, background = "#FF9914", text='Преобразование многочлена — \nкратные корни в простые', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = lambda : clc(11)).grid(row=4, column=2, stick='wens', padx=15, pady=15)

	close = Button(children, background = "#FF9914", text='Выход)', bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = '#6823E1', command=win.destroy).grid(row=5, column=2, padx=15, pady=15)

	info = Label(children, text='Вывод', bg='#F7C52B', font=40)
	info.grid(row=0, column=2, sticky=W)

	mainFrame = Frame(children)
	mainFrame.grid()
	
	
	Input=Entry(children, bg='white', font='Times 15')
	Input.grid(row=0, column=1, stick='wens', padx=15, pady=40, sticky='we')

win = Tk()

w = win.winfo_screenwidth()
h = win.winfo_screenheight()
w = w//2 # середина экрана
h = h//2 
w = w - 575 # смещение от середины
h = h - 400
win.geometry('1150x800+{}+{}'.format(w, h))





#win.geometry("1200x800+300+100")
win.resizable(width=False, height=False)
win['bg'] = '#F7C52B'
win.title("kal'kulyator")
flag = None
win.overrideredirect(flag==None)
calc = Entry(win)

title = Label(text='Выберите нужный модуль', bg='#F7C52B', font='Times 30').grid(column = 1)

b1 = Button(text='Натуральные числа с 0', background = "#FF9914", bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = btn_1).grid(row=1, column=0, stick='wens', padx=15, pady=15)
b2 = Button(text='Целые числа', background = "#FF9914", bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = btn_2).grid(row=1, column=1, stick='wens', padx=15, pady=15)
b3 = Button(text='Рациональные числа(дроби)', background = "#FF9914", bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = btn_3).grid(row=1, column=2, stick='wens', padx=15, pady=15)
b4 = Button(text='Многочлен с рациональными коэффициентами', background = "#FF9914", bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command = btn_4).grid(row=2, column=1, stick='wens', padx=15, pady=15)
a = Label(text=' ', bg='#F7C52B', width = 40, height = 23).grid(row = 3, column = 1)

close = Button(text='Выход)', background = "#FF9914", bd=15, width=40, height = 3, activebackground = '#FF7D00', 
	activeforeground = 'black', command=win.destroy).grid(row=4, column=2, padx=15, pady=15)



win.mainloop()