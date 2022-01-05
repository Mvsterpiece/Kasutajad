import random
def passautomat()->str: #делаю функцию где пароль будет создаваться автоматом
	str0=".,:;!_*-+()/#¤%&"
	str1 = '0123456789'
	str2 = 'qwertyuiopasdfghjklzxcvbnm'
	str3 = str2.upper()
	print(str3) #'QWERTYUIOPASDFGHJKLZXCVBNM'
	str4 = str0+str1+str2+str3
	print(str4)
	ls = list(str4)
	print(ls)
	random.shuffle(ls) #random.shuffle меняет позиции относительно других данных в списке
	print(ls)
	psword = ''.join([random.choice(ls) for x in range(12)])
	print(psword)

def passkontroll(passwords:str)-> bool:
	ls=list(psword)
	for n in ls:
		if n.isdigit(): d=True #идёт проверка, является ли переменная числом
		if n.isalpha(): v=True #идёт проверка, состоит ли переменная из букв
		if n.isupper(): u=True #идёт проверка, состоит ли переменная из заглавных букв
		if n.islower(): i=True #идёт проверка, состоит ли переменная из маленьких букв
		if n in list(".,:;!_*-+()/#¤%&"): s=True ##идёт проверка, состоит ли переменная из данных символов
	if d==True and v==True and u==True and i==True and s==True:
		t=True
	else:
		t=False
	return t
