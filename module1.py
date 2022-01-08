users=["Denis"]
passwords=["12345"]
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
