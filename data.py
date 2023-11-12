name=input('Введи свое имя  ')
next_enemy=0

top= {
    'name' : '',
        'armor' : 30,
        'HP' : 100,
        'attack' : 20,
        'luck' : 10,
        'energy': 150,
        'arsenal' : []  
    }

enemies= [
    {
        'name' : 'глеб хромой',
    'armor' : 1,
    'HP' : 100,
    'attack' : 20,
    'arsenal' : ['ГАДЮКА']
    },
    {
        'name' : 'Миха шустрый',
    'armor' : 10,
    'HP' : 150,
    'attack' : 15,
    'arsenal' : ['обрез']

    },
    {
        'name' : 'Воробей',
    'armor' : 12,
    'HP' : 450,
    'attack' : 20,
    'arsenal': []    
    },
    ]

shop = {
    '<1> хлеб' : 5 ,
    '<2> консерва' : 15,
    '<3> колбаса' : 20,
    '<4> водка казаки' : 50,
    '<5> патроны для ПМ' : 70,
    '<6> артефакт МЕДУЗА' : 100
    }



top_HP=top['HP']
enemy=enemies[next_enemy]
enemy_HP=enemies[next_enemy]['HP']
arsenal=top['arsenal']
enemy_arsenal=enemy['arsenal']
enemy=enemies[next_enemy]
enemy_HP=enemies[next_enemy]['HP']
top['name']=name