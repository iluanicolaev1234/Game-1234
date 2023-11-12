import random
import time
from data import*
import sale
import inform 


def update_armor():
    if top["armor"] < 0:
        top["armor"] = 0
    return    top["armor"]

def update_HP_top():
    global top_HP
    if top_HP < 0:
        top_HP = 0
    return    top_HP

def update_HP_enemies():
    global enemy_HP
    if enemy_HP < 0:
        enemy_HP = 0
    return    enemy_HP

def war() :
    global top_HP
    global enemy
    global enemy_HP
    global enemy_arsenal
    global next_enemy
    top_HP=top['HP']
    enemy=enemies[next_enemy]
    enemy_HP=enemies[next_enemy]['HP']
    arsenal=top['arsenal']
    enemy_arsenal=enemy['arsenal']
    print('БОЙ')
    input('Нажмите Enter чтобы продолжить')
    print()
    while top_HP > 0  and enemy_HP > 0 :
        step=random.randint(0 , 1)
        if step == 0 :
            time.sleep(1)
            print(f'{top["name"]} наносит удар')
            enemy_HP=enemy_HP - top['attack']
            inform.update_HP_enemies()
            print(f'    {enemy["name"]}  жив на {enemy_HP} %')
        if step == 1 :
            time.sleep(1)
            print(f'{enemy["name"]} наносит удар')
            top_HP=top_HP-enemy['attack']+top['armor']
            top['armor']=top['armor']-enemy['attack']
            inform.update_armor()
            inform.update_HP_top()
            print(f'   {top["name"]}  жив на {top_HP} %, броня {top["armor"]}') 
    if top_HP <= 0 :
        print('Ты поражён')
        print('ишь чё надумал!')
    if enemy_HP <= 0 :
        print('ПОБЕДА!!! отдавай всё что есть пока я не передумал!')
        print('теперь нужно отнести оружие бармену')
        arsenal=arsenal+enemy_arsenal
        print(f'Это теперь мое {enemy_arsenal}')
        print_t('кто идёт?')
        print()
        print('вот ты и попался!')
        print_t('!!!ПРОДОЛЖЕНИЕ СЛЕДУЕТ!!!')
    return top, enemies, top_HP, enemy_HP, enemy_arsenal, arsenal, next_enemy

def tume_1():
    print('бам!')
    time.sleep(1)
    print('бух!')
    time.sleep(1)
    print('бам!')
    time.sleep(1)
    print('бубух!')
    time.sleep(1.5)
    print('барабам!')


def tume_2():
    print('где же оно')
    time.sleep(1)
    print('может в шкафу')
    time.sleep(1)
    print('бам!')
    time.sleep(1)
    print('бубух!')
    time.sleep(1.5)
    print('чёрт!')
    time.sleep(1)
    print('ну и помойка!')
    time.sleep(1.5)
    print('нашёл!')


def print_t(str) :
    for i in str :
        print(i, end='', flush= True)
        time.sleep(0.03)






