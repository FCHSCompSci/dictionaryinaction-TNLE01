#Project 2
#Dictionaries in Action
import random
import time
#welcome
print('Welcome to monster hunt!')
username = input('What is your username? ')
print('Hello ' + username + '!')
#weapons
default = 'fists'
fists = {
    'speed': 40,
    'power': 30,
}
game_stats = {
    'user': username,
    'health': 100,
    'xp': 0,
    'weapon': default,
    'weapon_stats': eval(default),
}
def stats():
    for key, value in game_stats.items():
        print('%s: %s' % (key, value))
def switch_fists():
    print('You switched out your ' + game_stats['weapon'] + ' to your fists')
    game_stats['weapon'] = 'fists'
    game_stats['weapon_stats'] = fists
musket = {
    'speed': 60,
    'power': 90,
}
def switch_musket():
    print('You switch out your ' + game_stats['weapon'] + ' to the powerful musket')
    game_stats['weapon'] = 'musket'
    game_stats['weapon_stats'] = musket
throwing_knife = {
    'speed': 90,
    'power': 50,
}
def switch_throwing_knife():
    print('You switch out your ' + game_stats['weapon'] + ' to the throwing knifes')
    game_stats['weapon'] = 'throwing_knife'
    game_stats['weapon_stats'] = throwing_knife
shotgun = {
    'speed': 70,
    'power': 60,
}
def switch_shotgun():
    print('You switch out your ' + game_stats['weapon'] + ' to the super shotgun')
    game_stats['weapon'] = 'shotgun'
    game_stats['weapon_stats'] = shotgun
flamegun = {
    'speed': 80,
    'power': 70,
}
def switch_flamegun():
    print('You switch out your ' + game_stats['weapon'] + ' to the burning flamegun')
    game_stats['weapon'] = 'flamegun'
    game_stats['weapon_stats'] = flamegun
weapons_list = {
    'musket': musket,
    'throwing_knife': throwing_knife,
    'shotgun': shotgun,
    'flamegun': flamegun,
}
def weapons():
    for key, value in weapons_list.items():
        print('%s: %s' % (key, value))
#monsters
monster1 = {
    'speed': 50,
    'power': random.choice(range(10, 16)),
    'health': 50,
    'xp': 50,
}
monster2 = {
    'speed': 60,
    'power': random.choice(range(15, 21)),
    'health': 80,
    'xp': 75,
}
monster3 = {
    'speed': 70,
    'power': random.choice(range(30, 41)),
    'health': 100,
    'xp': 100,
}
#bosses
boss1 = {
    'speed': 50,
    'power': random.choice(range(10, 21)),
    'health': 70,
    'xp': 150,
}
boss2 = {
    'speed': 70,
    'power': random.choice(range(20, 31)),
    'health': 80,
    'xp': 200,
}
boss3 = {
    'speed': 90,
    'power': random.choice(range(10, 80)),
    'health': 150,
    'xp': 225,
}
#missrate
missrate = ['hit', 'miss']
#critrate
critrate = ['hit', 'miss', 'miss', 'miss', 'miss', 'miss', 'miss', 'miss', 'miss', 'miss',]
#menu
def storage():
    print('Here you can switch out your weapons')
    print('Type "sf" to put away your weapons and use your bare hands')
    print('Type "sm" to get the powerful musket')
    print('Type "stk" to get some knifes')
    print('Type "ss" to get a fun weapon')
    print('Type "sfg" to get the burning flamethrower')
    print('Type "b" to go back')
    while True:
        pickin = input('What would you like? ')
        if pickin == 'sf':
            switch_fists()
            break
        elif pickin == 'sm':
            switch_musket()
            break
        else:
            if pickin == 'stk':
                switch_throwing_knife()
                break
            elif pickin == 'ss':
                switch_shotgun()
                break
            else:
                if pickin == 'sfg':
                    switch_flamegun()
                    break
                elif pickin == 'b':
                    break
                else:
                    print(random.choice(what))
    time.sleep(2)
    print('Exiting storage..')
    time.sleep(2)
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
def market():
    print('close at the moment..sorry')
def play():
    print('"e" for easy')
    print('"n" for normal')
    print('"h" for hard')
    print('"m" for market')
    print('"b" for back')
    while True:
        gamestarts = input('How hard do you want to play? ')
        if gamestarts == 'e':
            easy()
            break
        elif gamestarts == 'n':
            normal()
            break
        else:
            if gamestarts == 'h':
                hard()
                break
            elif gamestarts =='m':
                market()
                break
            else:
                if gamestarts == 'b':
                    break
                else:
                    print(random.choice(what))
def easy():
    print('easy mode selected')
    time.sleep(random.choice(range(1, 6)))
    print('Loading...')
    time.sleep(random.choice(range(1, 6)))
    print('Game Start!')
    combat(monster1)
    time.sleep(2)
    respawn()
    if game_stats['health'] <= 0:
        print('Returning to menu..')
        heal()
        pass
    else:
        print('Next monster coming..')
        combat(monster1)
def normal():
    print('normal mode selected')
    time.sleep(random.choice(range(1, 6)))
    print('Loading...')
    time.sleep(random.choice(range(1, 6)))
    print('Game Start!')
    combat(monster2)
    time.sleep(2)
    respawn()
    if game_stats['health'] <= 0:
        print('Returning to menu..')
        heal()
        pass
    else:
        print('Next monster coming..')
        combat(monster2)
def hard():
    print('hard mode selected')
    time.sleep(random.choice(range(1, 6)))
    print('Loading...')
    time.sleep(random.choice(range(1, 6)))
    print('Game Start!')
    combat(monster3)
    time.sleep(2)
    respawn()
    if game_stats['health'] <= 0:
        print('Returning to menu..')
        heal()
        pass
    else:
        print('Next monster coming..')
        combat(monster3)
def combat(mon):
    if mon == monster1:
        power = range(10, 16)
    elif mon == monster2:
        power = range(15, 21)
    else:
        power = range(30, 41)
    while True:
        if game_stats['weapon_stats']['speed'] > mon['speed']:
            print('You attacked the monster first')
            attack = random.choice(missrate)
            if attack == 'hit':
                print('You hit the monster')
                crit = random.choice(critrate)
                if crit == 'hit':
                    print('Critical hit!')
                    print('You did ' + str(game_stats['weapon_stats']['power']*2) + ' damage to the monster')
                    mon['health'] = mon['health'] - game_stats['weapon_stats']['power']*2
                    if mon['health'] <= 0:
                        print('monster down')
                        break
                    else:
                        print('The monster now attacks you')
                        mon['power'] = random.choice(power)
                        attack = random.choice(missrate)
                        if attack == 'hit':
                            print('The monster hit you')
                            crit = random.choice(critrate)
                            if crit == 'hit':
                                print('Critical hit!')
                                print('The monster did ' + str(mon['power']*2) + ' damage to you')
                                game_stats['health'] = game_stats['health'] - mon['power']*2
                                if game_stats['health'] <= 0:
                                    print('Oh no..Game over')
                                    break
                                else:
                                    continue
                            else:
                                print('The monster did ' + str(mon['power']) + ' damage to you')
                                game_stats['health'] = game_stats['health'] - mon['power']
                                if game_stats['health'] <= 0:
                                    print('Oh no..Game over')
                                    break
                                else:
                                    continue
                        else:
                            print('The monster miss you')
                            continue
                else:
                    print('You did ' + str(game_stats['weapon_stats']['power']) + ' damage to the monster')
                    mon['health'] = mon['health'] - game_stats['weapon_stats']['power']
                    if mon['health'] <= 0:
                        print('monster down')
                        break
                    else:
                        print('The monster now attacks you')
                        mon['power'] = random.choice(power)
                        attack = random.choice(missrate)
                        if attack == 'hit':
                            print('The monster hit you')
                            crit = random.choice(critrate)
                            if crit == 'hit':
                                print('Critical hit!')
                                print('The monster did ' + str(mon['power']*2) + ' damage to you')
                                game_stats['health'] = game_stats['health'] - mon['power']*2
                                if game_stats['health'] <= 0:
                                    print('Oh no..Game over')
                                    break
                                else:
                                    continue
                            else:
                                print('The monster did ' + str(mon['power']) + ' damage to you')
                                game_stats['health'] = game_stats['health'] - mon['power']
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
                mon['power'] = random.choice(power)
                attack = random.choice(missrate)
                if attack == 'hit':
                    print('The monster hit you')
                    crit = random.choice(critrate)
                    if crit == 'hit':
                        print('Critical hit!')
                        print('The monster did ' + str(monster2['power']*2) + ' damage to you')
                        game_stats['health'] = game_stats['health'] - mon['power']*2
                        if game_stats['health'] <= 0:
                            print('Oh no..Game over')
                            break
                        else:
                            continue
                    else:
                        print('The monster did ' + str(monster2['power']) + ' damage to you')
                        game_stats['health'] = game_stats['health'] - mon['power']
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
            mon['power'] = random.choice(power)
            attack = random.choice(missrate)
            if attack == 'hit':
                print('The monster hit you')
                crit = random.choice(critrate)
                if crit == 'hit':
                    print('Critical hit!')
                    print('The monster did ' + str(mon['power']*2) + ' damage to you')
                    game_stats['health'] = game_stats['health'] - mon['power']*2
                    if game_stats['health'] <= 0:
                        print('Oh no..Game over')
                        break
                    else:
                        print('You now attack the monster')
                        attack = random.choice(missrate)
                        if attack == 'hit':
                            print('You hit the monster')
                            crit = random.choice(critrate)
                            if crit == 'hit':
                                print('Critical hit!')
                                print('You did ' + str(game_stats['weapon_stats']['power']*2) + ' damage to the monster')
                                mon['health'] = mon['health'] - game_stats['weapon_stats']['power']*2
                                if mon['health'] <= 0:
                                    print('monster down')
                                    break
                                else:
                                    continue
                            else:
                                print('You did ' + str(game_stats['weapon_stats']['power']) + ' damage to the monster')
                                mon['health'] = mon['health'] - game_stats['weapon_stats']['power']
                                if mon['health'] <= 0:
                                    print('monster down')
                                    break
                                else:
                                    continue
                        else:
                            print('You miss the monster')
                            continue
                else:
                    print('The monster did ' + str(mon['power']) + ' damage to you')
                    game_stats['health'] = game_stats['health'] - mon['power']
                    if game_stats['health'] <= 0:
                        print('Oh no..Game over')
                        break
                    else:
                        print('You now attack the monster')
                        attack = random.choice(missrate)
                        if attack == 'hit':
                            print('You hit the monster')
                            crit = random.choice(critrate)
                            if crit == 'hit':
                                print('Critical hit!')
                                print('You did ' + str(game_stats['weapon_stats']['power']*2) + ' damage to the monster')
                                mon['health'] = mon['health'] - game_stats['weapon_stats']['power']*2
                                if mon['health'] <= 0:
                                    print('monster down')
                                    break
                                else:
                                    continue
                            else:
                                print('You did ' + str(game_stats['weapon_stats']['power']) + ' damage to the monster')
                                mon['health'] = mon['health'] - game_stats['weapon_stats']['power']
                                if mon['health'] <= 0:
                                    print('monster down')
                                    break
                                else:
                                    continue
                        else:
                            print('You miss the monster')
                            continue
            else:
                print('The monster miss you')
                print('You now attack the monster')
                attack = random.choice(missrate)
                if attack == 'hit':
                    print('You hit the monster')
                    crit = random.choice(critrate)
                    if crit == 'hit':
                        print('You did ' + str(game_stats['weapon_stats']['power']*2) + ' damage to the monster')
                        mon['health'] = mon['health'] - game_stats['weapon_stats']['power']*2
                        if mon['health'] <= 0:
                            print('monster down')
                            break
                        else:
                            continue
                    else:
                        print('You did ' + str(game_stats['weapon_stats']['power']) + ' damage to the monster')
                        mon['health'] = mon['health'] - game_stats['weapon_stats']['power']
                        if mon['health'] <= 0:
                            print('monster down')
                            break
                        else:
                            continue
                else:
                    print('You miss the monster')
                    continue
#program starts
what = ['What?', 'Can you repeat that', 'Try again', 'No']
print('Your current weapon are your hands, you can get a weapon in the storage room')
print('Type "p" to start the game.')
print('Type "s" to see your player stats.')
print('Type "w" to see the list of weapons.')
print('Type "st" to see your storage.')
print('Type "b" to exit and end the game *note that all your stats will be lost.')
print('Type "m" to see the menu')
while True:
    start = input('What would you like to do? ')
    if start == 'p':
        play()
    elif start == 's':
        stats()
    else:
        if start == 'w':
            weapons()
        elif start == 'st':
            storage()
        else:
            if start == 'b':
                break
            elif start == 'm':
                menu()
            else:
                print(random.choice(what))
print('Thanks for playing!')



    
