import random

def randompass()->str:
    """Пароль создаётся рандомно

    """
    str0=".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper() # 'QWERTYUIOPASDFGHJKLZXCVBNM'
    str4 = str0+str1+str2+str3
    ls = list(str4)
    random.shuffle(ls) #перемешиваются все символы
    psword = ''.join([random.choice(ls) for x in range(12)])
    return psword

def control(passwords:str)->str:
    """Проверка пароля, самое главное чтобы в личном пароле присутсвовал хотя 1 тип символов.
    """
    str0=".,:;!_*-+()/#¤%&"
    alpha=digit=upper=sprcial=0
    ls=list(str0)
    pas=list(passwords)
    for i in range(len(pas)):
        if pas[i].isupper():
            upper=1
        if pas[i].isalpha():
            alpha=1
        if pas[i].isdigit():
            digit=1
        if pas[i] in ls:
            special=1
    if alpha==1 and digit==1 and upper==1 and special==1:
        control=True
    else:
        control=False
    return control

def failist_lugemine(f:str,u:list):
    """Info failist f listisse u

    """
    fail=open(f,"r",)
    for rida in fail:
        u.append(rida.strip())
    fail.close()
    return u 

def failist_passw(a:str,p:list):
    """Info failist a listisse p

    """
    fail=open(a,"r")
    for rida in fail:
        p.append(rida.strip())
    fail.close()
    return p

#def failisse_salvestamine(f:str,u:list):
#    fail=open(f,"w")
#    for el in u:
#        fail.write(el+"\n")
#    fail.close()
def rida_salvestamine(f:str,rida:str):
    fail=open(f,"a")
    fail.write(rida+"\n")
    fail.close()
