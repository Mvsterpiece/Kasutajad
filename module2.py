def zodiac(a:int,b:int,c:int):
	"""

	"""
	if a==1:
		a=int(input("Введите день рождения:"))
		b=int(input("Введите месяц рождения:"))
		c=int(input("Введите год рождения:"))

		if (a>=21 and a<=31 and b==3) or( b==4 and a>=1 and a<=19):
			print("Знак зодиака:Овен")
		elif (a>=20 and a<=30 and b==4) or( b==5 and a>=1 and a<=20):
			print("Знак зодиака:Телец")
		elif (a>=21 and a<=31 and b==5) or( b==6 and a>=1 and a<=21):
			print("Знак зодиака:Близнецы")
		elif (a>=22 and a<=30 and b==6) or( b==7 and a>=1 and a<=22):
			print("Знак зодиака:Рак")
		elif (a>=23 and a<=31 and b==7) or( b==8 and a>=1 and a<=22):
			print("Знак зодиака:Лев")
		elif (a>=23 and a<=31 and b==8) or( b==9 and a>=1 and a<=22):
			print("Знак зодиака:Дева")
		elif (a>=23 and a<=30 and b==9) or( b==10 and a>=1 and a<=23):
			print("Знак зодиака:Весы")
		elif (a>=24 and a<=31 and b==10) or( b==11 and a>=1 and a<=22):
			print("Знак зодиака:Скорпион")
		elif (a>=23 and a<=30 and b==11) or( b==12 and a>=1 and a<=21):
			print("Знак зодиака:Стрелец")
		elif (a>=22 and a<=31 and b==12) or( b==1 and a>=1 and a<=20):
			print("Знак зодиака:Козерог")
		elif (a>=21 and a<=31 and b==1) or( b==2 and a>=1 and a<=18):
			print("Знак зодиака:Водолей")
		elif (a>=19 and a<=29 and b==2) or( b==3 and a>=1 and a<=20):
			print("Знак зодиака:Рыбы")    

	elif a==0:
		print("Хорошо, прощай!")
	return zodiac