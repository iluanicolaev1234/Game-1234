from data import *

def sal() :
    buy= input()
    if buy == '1' :
        keys ='<1> хлеб'
        top['HP']= top['HP'] + shop[keys]
        top['energy']= top['energy']-shop[keys]
        
    if buy == '2' :
        keys ='<2> консерва'
        top['HP']= top['HP'] + shop[keys]
        top['energy']= top['energy']-shop[keys]
        
    if buy == '3' :
        keys ='<3> колбаса'
        top['HP']= top['HP'] + shop[keys]
        top['energy']= top['energy']-shop[keys]
        
    if buy == '4' :
        keys ='<4> водка казаки'
        top['luck']= top['luck'] + shop[keys]
        top['energy']= top['energy']-shop[keys]
        
    if buy == '5' :
        keys ='<5> патроны для ПМ'
        top['HP']= top['HP'] + shop[keys]
        top['energy']= top['energy']-shop[keys]
        
    if buy == '6' :
        keys ='<6> артефакт МЕДУЗА'
        top['HP']= top['HP'] + shop[keys]
        top['armor']=top['armor'] + shop[keys]
        top['energy']= top['energy']-shop[keys]
        
    arsenal=top['arsenal']
    arsenal.append(keys)
    return arsenal



