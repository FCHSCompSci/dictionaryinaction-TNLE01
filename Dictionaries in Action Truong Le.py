#Project 2
#Dictionaries in Action
import random

username = input('What is your username? ')

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
print('musket, throwing_knife, shotgun, flamegun')
weapon = eval(input('What is your choice of weapon? '))

game_stats = {
    'user': username,
    'health': 100,
    'xp': 0,
    'weapons': weapon,
    }
