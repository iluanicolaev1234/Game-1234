from calendar import c
import random
import time
from data import *
import sale
import inform 
from inform import print_t


while True :
    print_t('''1.тренировка или 2.к Петровичу или  3.в БАР 100 ренген
''')
    a=input()
    if a == '1':
        print_t('ТРЕНИРОВКА')
        print_t ('это груша , её нужно бить ')
        print_t('готовиться к бою ?-<ENTER>')
        b=input()
        if b == '':
            inform.tume_1()
            top['attack'] = top['attack'] + 10
            print(f'вы молодец, ваша сила равна {top["attack"]}!')
    if a == '2':
        print_t('здоров Петрович!')
        print_t ('слыш дай шмот мне да не плохой,на тысячу')
        print (f' Здорова   {top["name"]}  иди в кладовке погляди')
        print_t('идти в кладовку-<ENTER>')
        b=input()
        if b == '':
            inform.tume_2() 
        top['armor'] = top['armor'] + 10
        print(f'''так теперь есть бронижилет и комбинезон военных теперь прочность брони <<{top["armor"]}!>>
                ну что, как там тебя ...{top["name"]}  хочеш проверить себя в деле!?!
                ''')
    if a == '3':
        print_t('''     100 - Р_Е_Н_Г_Е_Н
                ''')
        print_t('привет Бармен , какой товар можешь предложить ?')
        print_t('в это вреня только хороший товар из тёмной долины!')
        print_t('Выбери свою покупку')
        print_t(f'''
<1> хлеб за 5 рублей
<2> консерва за 15 рублей
<3> колбаса за 20 рублей
<4> водка казаки за 50 рублей
<5> патроны за 70 рублей
<6> артефакт МЕДУЗА
                ''')
        sale.sal()
        for k, v in top.items() :
            print(k, v)
        print(f'    {top["name"]}, хочешь пойти на спец - задание  ')
        c=input('если <да> введите Enter, если <нет> введите <0>') 
    if c == '':
        print()
        print_t(f'''смотри на болото на свалке собралась банда бандитов из 3 человек , 
одного из них зовут Глеб хромой у него есть хороший автомат-ГАДЮКА на зажигательных патронах
            ''')
        print_t('достанешь товар в долгу не останусь')
        print_t('''
            берёшься за дело?,   если <да> введите Enter
            ''')
        inform.war()
    