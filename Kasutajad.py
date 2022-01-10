from module1 import *

users=["Denis"]
passwords=["12345"]

while True:
    print("Зарегистрироваться-1, Авторизоваться-2, Выход-3")
    ch=int(input())
    if ch==1:
        print("Вы выбрали регистрацию")
        while 1:
            log=input("Введите свое имя: ")
            if log not in users:
                print("Данное имя не было занято, теперь оно принадлежит вам.")
                break
            else:
                print("Данное имя уже кем то используется.")
        ch=input("Самим записать пароль(S) или робот придумает(R)? ")
        if ch.upper()=="R":
            pas=randompass()
            print(pas)
        elif ch.upper()=="S":
            while 1:
                pas=input("Введите свой пароль: ")
                result=control(pas)
                if result==True:
                    users.append(log)
                    passwords.append(pas)
                    break
    elif ch==2: 
        print("Вы выбрали авторизацию")
        user=input("Введите свое имя: ")
        pas=input("Введите свой пароль: ")
        if users.index(user)==passwords.index(pas):
            print("Добро пожаловать")
    elif ch==3:
        print("Выход из программы")
        break