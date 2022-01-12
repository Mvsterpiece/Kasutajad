from module1 import *

users=["Denis","Pablo"]
passwords=["12345","boba"]

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
            print()
            print("Хотите узнать кто вы по знаку зодиака? Да-1, Нет-0.")
            a=int(input())
            if a==1:
                a=int(input("Введите день рождения:"))
                b=int(input("Введите месяц рождения:"))
                c=int(input("Введите год рождения:"))

                if (a>=21 and a<=31 and b==3) or( b==4 and a>=1 and a<=19):
                        print("Знак зодиака:Овен")
                        break
                elif (a>=20 and a<=30 and b==4) or( b==5 and a>=1 and a<=20):
                        print("Знак зодиака:Телец")
                        break
                elif (a>=21 and a<=31 and b==5) or( b==6 and a>=1 and a<=21):
                        print("Знак зодиака:Близнецы")
                        break
                elif (a>=22 and a<=30 and b==6) or( b==7 and a>=1 and a<=22):
                        print("Знак зодиака:Рак")
                        break
                elif (a>=23 and a<=31 and b==7) or( b==8 and a>=1 and a<=22):
                        print("Знак зодиака:Лев")
                        break
                elif (a>=23 and a<=31 and b==8) or( b==9 and a>=1 and a<=22):
                        print("Знак зодиака:Дева")
                        break
                elif (a>=23 and a<=30 and b==9) or( b==10 and a>=1 and a<=23):
                        print("Знак зодиака:Весы")
                        break
                elif (a>=24 and a<=31 and b==10) or( b==11 and a>=1 and a<=22):
                        print("Знак зодиака:Скорпион")
                        break
                elif (a>=23 and a<=30 and b==11) or( b==12 and a>=1 and a<=21):
                        print("Знак зодиака:Стрелец")
                        break
                elif (a>=22 and a<=31 and b==12) or( b==1 and a>=1 and a<=20):
                        print("Знак зодиака:Козерог")
                        break
                elif (a>=21 and a<=31 and b==1) or( b==2 and a>=1 and a<=18):
                        print("Знак зодиака:Водолей")
                        break
                elif (a>=19 and a<=29 and b==2) or( b==3 and a>=1 and a<=20):
                        print("Знак зодиака:Рыбы")                   
            elif a==0:
                print("Хорошо, прощай")
                break

    elif ch==3:
        print("Выход из программы")
        break
        