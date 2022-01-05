from module1 import *
users=["Denis"]
passwords=["pass"]

while True:
	print("Регистрация - 1")
	print("Авторизация - 2")
	a=int(input())
	if a==1:
		print("Для регистрации, введите свой логин и пароль.")
		while 1:
			login=input("Введите имя/логин пользователя: ")
			if login not in users:
				print("Данное имя/логин не занято. Теперь оно ваше!")
				break
			else:
				print("Данное имя/логин уже кем то используется.")
		a=input("Вы желаете сами придумать пароль или пусть рандомно создаться? (Рандом -r, Самому -s)")
		if a.upper()=="r":
			ps=passautomat()
		elif a.upper()=="s":
			while 1:
				ps=input("Введите свой пароль")
				result=passkontroll(passwords)
				if result==True:
					users.append(login)
					passwords.append(ps)
					break
		else:
			print("Неверный пароль")
	elif a==2:
		print("Для авторизации введите свой логин и пароль.")
		login=input("Введите имя/логин пользователя: ")
		if passwords.index(,[passwords],[users]):
			print("Добро пожаловать")