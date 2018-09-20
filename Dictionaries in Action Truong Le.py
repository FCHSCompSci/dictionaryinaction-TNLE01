#Project 2
#Dictionaries in Action

import random
import time

#welcome


print('Welcome to monster hunt!')
username = input('What is your username? ')
print('Hello ' + username + '!')
print('Your current weapon are your hands, you can get a weapon in the storage room')

#weapons

default = 'fists'
fists = {

    'speed': 40,

    'power': 30,

}
musket = {

    'speed': 60,

    'power': 90,

}
throwing_knife = {

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
weapons_list = {

    'musket': musket,

    'throwing_knife': throwing_knife,

    'shotgun': shotgun,

    'flamegun': flamegun,

}

#player stats

game_stats = {
    'user': username,
    'health': 100,
    'xp': 0,
    'weapon': default,
    'weapon_stats': eval(default),
    }

#monsters

monster1 = {
    'speed': 50,
    'power': random.choices(range(10, 16)),
    'health': 50,
    'xp': 50,
}
monster2 = {
    'speed': 60,
    'power': random.choices(range(15, 21)),
    'health': 80,
    'xp': 75,
}
monster3 = {
    'speed': 70,
    'power': random.choices(range(30, 41)),
    'health': 100,
    'xp': 100,
}

#bosses

boss1 = {
    'speed': 50,
    'power': random.choices(range(10, 21)),
    'health': 70,
    'xp': 150,
}
boss2 = {
    'speed': 70,
    'power': random.choices(range(20, 31)),
    'health': 80,
    'xp': 200,
}
boss3 = {
    'speed': 90,
    'power': random.choices(range(10, 80)),
    'health': 150,
    'xp': 225,
}

#missrate

missrate = ['hit', 'miss']

#menu

print('Type "play()" to start the game.')
print('Type "stats()" to see your player stats.')
print('Type "weapons()" to see the list of weapons.')
print('Type "storage()" to see your storage.')
print('Type "quit()" to exit and end the game *note that all your stats will be lost.')
print('Type "menu()" to see the menu')

def stats():
    for key, value in game_stats.items():
        print('%s: %s' % (key, value))
def weapons():
    for key, value in weapons_list.items():
        print('%s: %s' % (key, value))
def storage():
    print('Here you can switch out your weapons')
    print('Type "switch_fists()" to put away your weapons and use your bare hands')
    print('Type "switch_musket()" to get the powerful musket')
    print('Type "switch_throwing_knife()" to get some knifes')
    print('Type "switch_shotgun()" to get a fun weapon')
    print('Type "switch_flamegun()" to get the burning flamethrower')
def switch_fists():
    print('You switched out your ' + game_stats['weapon'] + ' to your fists')
    game_stats['weapon'] = 'fists'
    game_stats['weapon_stats'] = fists
def switch_musket():
    print('You switch out your ' + game_stats['weapon'] + ' to the powerful musket')
    game_stats['weapon'] = 'musket'
    game_stats['weapon_stats'] = musket
def switch_throwing_knife():
    print('You switch out your ' + game_stats['weapon'] + ' to the throwing knifes')
    game_stats['weapon'] = 'throwing_knife'
    game_stats['weapon_stats'] = throwing_knife
def switch_shotgun():
    print('You switch out your ' + game_stats['weapon'] + ' to the super shotgun')
    game_stats['weapon'] = 'shotgun'
    game_stats['weapon_stats'] = shotgun
def switch_flamegun():
    print('You switch out your ' + game_stats['weapon'] + ' to the burning flamegun')
    game_stats['weapon'] = 'flamegun'
    game_stats['weapon_stats'] = flamegun
def menu():
    print('Type "play()" to start the game.')
    print('Type "stats()" to see your player stats.')
    print('Type "weapons()" to see the list of weapons.')
    print('Type "storage()" to see the market.')
    print('Type "quit()" to exit and end the game *note that all your stats will be lost.')

#gameplay

def heal():
    game_stats['health'] = 100
def respawn():
    monster1['health'] = 50
    monster2['health'] = 80
    monster3['health'] = 100
    boss1['health'] = 70
    boss2['health'] = 80
    boss3['health'] = 150
def play():
    print('How hard do you want to play?')
    print('easy()')
    print('normal()')
    print('hard()')
def easy():
    print('easy mode selected')
    time.sleep(random.choice(range(1, 6)))
    print('Loading...')
    time.sleep(random.choice(range(1, 6)))
    print('Game Start!')
    easycombat()
def normal():
    print('normal mode selected')
    time.sleep(random.choice(range(1, 6)))
    print('Loading...')
    time.sleep(random.choice(range(1, 6)))
    print('Game Start!')
    normalcombat()
def hard():
    print('hard mode selected')
    time.sleep(random.choice(range(1, 6)))
    print('Loading...')
    time.sleep(random.choice(range(1, 6)))
    print('Game Start!')
    hardcombat()
def easycombat():
    while True:
        if game_stats['weapon_stats']['speed'] > monster1['speed']:
            print('You attacked the monster first')
            attack = random.choice(missrate)
            if attack == 'hit':
                print('You hit the monster')
                print('You did ' + str(game_stats['weapon_stats']['power']) + ' damage to the monster')
                monster1['health'] = monster1['health'] - game_stats['weapon_stats']['power']
                if monster1['health'] <= 0:
                    print('monster down')
                    break
                else:
                    print('The monster now attacks you')
                    monster1['power'] = random.choices(range(10, 16))
                    attack = random.choice(missrate)
                    if attack == 'hit':
                        print('The monster hit you')
                        print('The monster did ' + str(monster1['power']) + ' damage to you')
                        game_stats['health'] = game_stats['health'] - sum(monster1['power'])
                        if game_stats['health'] <= 0:
                            print('Oh no..Game over')
                            break
                        else:
                            continue
                    else:
                        print('The monster miss you')
                        continue
            else:
                print('You miss the monster')
                print('The monster now attacks you')
                monster1['power'] = random.choices(range(10, 16))
                attack = random.choice(missrate)
                if attack == 'hit':
                    print('The monster hit you')
                    print('The monster did ' + str(monster1['power']) + ' damage to you')
                    game_stats['health'] = game_stats['health'] - sum(monster1['power'])
                    if game_stats['health'] <= 0:
                        print('Oh no..Game over')
                        break
                    else:
                         continue
                else:
                    print('The monster miss you')
                    continue
        else:
            print('The monster attacked you first')
            monster1['power'] = random.choices(range(10, 16))
            attack = random.choice(missrate)
            if attack == 'hit':
                print('The monster hit you')
                print('The monster did ' + str(monster1['power']) + ' damage to you')
                game_stats['health'] = game_stats['health'] - sum(monster1['power'])
                if game_stats['health'] <= 0:
                    print('Oh no..Game over')
                    break
                else:
                    print('You now attack the monster')
                    attack = random.choice(missrate)
                    if attack == 'hit':
                        print('You hit the monster')
                        print('You did ' + str(game_stats['weapon_stats']['power']) + ' damage to the monster')
                        monster1['health'] = monster1['health'] - game_stats['weapon_stats']['power']
                        if monster1['health'] <= 0:
                            print('monster down')
                            break
                        else:
                            continue
def normalcombat():
    while True:
        if game_stats['weapon_stats']['speed'] > monster2['speed']:
            print('You attacked the monster first')
            print('You did ' + str(game_stats['weapon_stats']['power']) + ' damage to the monster')
            monster2['health'] = monster2['health'] - game_stats['weapon_stats']['power']
            if monster2['health'] <= 0:
                print('monster down')
                break
            else:
                print('The monster now attacks you')
                monster2['power'] = random.choices(range(15, 21))
                print('The monster did ' + str(monster2['power']) + ' damage to you')
                game_stats['health'] = game_stats['health'] - sum(monster2['power'])
                if game_stats['health'] <= 0:
                    print('Oh no..Game over')
                    break
                else:
                    continue
        else:
            print('The monster attacked you first')
            monster2['power'] = random.choices(range(15, 21))
            print('The monster did ' + str(monster2['power']) + ' damage to you')
            game_stats['health'] = game_stats['health'] - sum(monster2['power'])
            if game_stats['health'] <= 0:
                print('Oh no..Game over')
                break
            else:
                print('You now attack the monster')
                print('You did ' + str(game_stats['weapon_stats']['power']) + ' damage to the monster')
                monster2['health'] = monster2['health'] - game_stats['weapon_stats']['power']
                if monster2['health'] <= 0:
                    print('monster down')
                    break
                else:
                    continue
def hardcombat():
    while True:
        if game_stats['weapon_stats']['speed'] > monster3['speed']:
            print('You attacked the monster first')
            print('You did ' + str(game_stats['weapon_stats']['power']) + ' damage to the monster')
            monster3['health'] = monster3['health'] - game_stats['weapon_stats']['power']
            if monster3['health'] <= 0:
                print('monster down')
                break
            else:
                print('The monster now attacks you')
                monster3['power'] = random.choices(range(30, 41))
                print('The monster did ' + str(monster3['power']) + ' damage to you')
                game_stats['health'] = game_stats['health'] - sum(monster3['power'])
                if game_stats['health'] <= 0:
                    print('Oh no..Game over')
                    break
                else:
                    continue
        else:
            print('The monster attacked you first')
            monster3['power'] = random.choices(range(30, 41))
            print('The monster did ' + str(monster3['power']) + ' damage to you')
            game_stats['health'] = game_stats['health'] - sum(monster3['power'])
            if game_stats['health'] <= 0:
                print('Oh no..Game over')
                break
            else:
                print('You now attack the monster')
                print('You did ' + str(game_stats['weapon_stats']['power']) + ' damage to the monster')
                monster3['health'] = monster3['health'] - game_stats['weapon_stats']['power']
                if monster3['health'] <= 0:
                    print('monster down')
                    break
                else:
                    continue











    
