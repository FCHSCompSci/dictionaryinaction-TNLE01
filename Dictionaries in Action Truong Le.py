#Project 2
#Dictionaries in Action
import random

#username pick
username = input('What is your username? ')
#weapons
musket = {
    'speed': 60,
    'power': 90,
    }
throwing_kinfe = {
    'speed': 90,
    'power': 50,
    }
shotgun = {
    'speed': 70,
    'power': 60,
    }
flamegun = {
    'speed': 80,
    'power': 70,
}
#weapon pick
print('musket, throwing_knife, shotgun, flamegun')
weapon = eval(input('What is your choice of weapon? '))
#player stats
game_stats = {
    'user': username,
    'health': 100,
    'xp': 0,
    'weapons': weapon,
    }
#monsters
monster1 = {
    'speed': 50,
    'power': random.choices(range(10, 16)),
    'health': 50,
}
monster2 = {
    'speed': 60,
    'power': random.choices(range(15, 21)),
    'health': 80,
}
monster3 = {
    'speed': 70,
    'power': random.choices(range(30, 41)),
    'health': 100,
}
#bosses
boss1 = {
    'speed': 50,
    'power': random.choices(range(10, 21)),
    'health': 70,
}
boss2 = {
    'speed': 70,
    'power': random.choices(range(20, 31)),
    'health': 80,
}
boss3 = {
    'speed': 90,
    'power': random.choices(range(10, 80)),
    'health': 150,
}
#missrate
missrate = ['hit', 'miss']
misses = random.choices[missrate]









    
