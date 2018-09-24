#Project 2
#Dictionaries in Action
#Truong Le
#9/24/18
import random
import time
#welcome
print('Welcome to monster hunt!')
username = input('What is your username? ')
print('Hello ' + username + '!')
#weapons
default = 'fists'
fists = {
    'speed': 30,
    'power': 20,
}
game_stats = {
    'user': username,
    'health': 100,
    'xp': 0,
    'money': 0,
    'monsters_killed': 0,
    'weapon': default,
    'weapon_stats': eval(default),
}
def stats():
    for key, value in game_stats.items():
        print('%s: %s' % (key, value))
musket = {
    'speed': 40,
    'power': 50,
}
throwing_knife = {
    'speed': 60,
    'power': 25,
}
shotgun = {
    'speed': 50,
    'power': 40,
}
flamegun = {
    'speed': 30,
    'power': 10,
}
def switch(new_weapon):
    if new_weapon == 'fists':
        print('You switch out your ' + game_stats['weapon'] + ' to your fists')
        game_stats['weapon'] = 'fists'
        game_stats['weapon_stats'] = fists
    else:
        print('You switch out your ' + game_stats['weapon'] + ' to the ' + new_weapon)
        game_stats['weapon'] = new_weapon
        game_stats['weapon_stats'] = eval(new_weapon)
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
    'cost': 50,
    'xp': 50,
}
monster2 = {
    'speed': 60,
    'power': random.choice(range(15, 21)),
    'health': 80,
    'cost': 100,
    'xp': 75,
}
monster3 = {
    'speed': 70,
    'power': random.choice(range(30, 41)),
    'health': 100,
    'cost': 150,
    'xp': 100,
}
#bosses
boss1 = {
    'speed': 50,
    'power': random.choice(range(10, 21)),
    'health': 70,
    'cost': 100,
    'xp': 150,
}
boss2 = {
    'speed': 70,
    'power': random.choice(range(20, 31)),
    'health': 80,
    'cost': 200,
    'xp': 200,
}
boss3 = {
    'speed': 90,
    'power': random.choice(range(10, 81)),
    'health': 150,
    'cost': 500,
    'xp': 225,
}
#missrate
missrate = ['hit', 'miss']
#critrate
critrate = ['hit', 'miss', 'miss', 'miss', 'miss', 'miss', 'miss', 'miss', 'miss', 'miss',]
#menu
def storage():
    print('Here you can switch out your weapons')
    time.sleep(2)
    while True:
        print('"sf" to put away your weapons and use your bare hands')
        print('"sm" to get the a powerful musket')
        print('"stk" to get some knifes')
        print('"ss" to get a shotgun')
        print('"sfg" to get the flamegun')
        print('"b" to go back')
        pickin = input('What would you like? ')
        if pickin == 'sf':
            switch('fists')
            break
        elif pickin == 'sm':
            switch('musket')
            break
        else:
            if pickin == 'stk':
                switch('throwing_knife')
                break
            elif pickin == 'ss':
                switch('shotgun')
                break
            else:
                if pickin == 'sfg':
                    switch('flamegun')
                    break
                elif pickin == 'b':
                    time.sleep(2)
                    break
                else:
                    print(random.choice(what))
                    time.sleep(2)
                    continue
    time.sleep(2)
    print('Exiting storage..')
    time.sleep(2)
def menu():
    print('"p" to start the game.')
    print('"s" to see your player stats.')
    print('"w" to see the list of weapons.')
    print('"st" to see the market.')
    print('"b" to exit and end the game *note that all your stats will be lost.')
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
def money(cost):
    game_stats['money'] = game_stats['money'] - cost

def upgrade(checkout):
    time.sleep(2)
    if checkout == 'f':
        if fists['speed'] == 30:
            fist1 = input('Would you like to buy level 1 fists for $100? (y/n) ')
            if fist1 == 'y':
                if game_stats['money'] < 100:
                    print('You dont have enough money')
                else:
                    money(100)
                    fists['speed'] = 40
                    fists['power'] = 30
                    print('Thank you for coming')
            elif fist1 == 'n':
                print('come again')
            else:
                print(random.choice(what))
        elif fists['speed'] == 40:
            fist2 = input('Would you like to buy level 2 fists for $200? (y/n) ')
            if fist2 == 'y':
                if game_stats['money'] < 200:
                    print('You dont have enough money')
                else:
                    money(200)
                    fists['speed'] = 50
                    fists['power'] = 40
                    print('Thank you for coming')
            elif fist2 == 'n':
                print('come again')
            else:
                print(random.choice(what))
        else:
            if fists['speed'] == 50:
                fist3 = input('Would you like to buy level 3 fists for $300? (y/n) ')
                if fist3 == 'y':
                    if game_stats['money'] < 300:
                        print('You dont have enough money')
                    else:
                        money(300)
                        fists['speed'] = 60
                        fists['power'] = 50
                        print('Thank you for coming')
                elif fist3 == 'n':
                    print('come again')
                else:
                    print(random.choice(what))
            else:
                print('Looks like your fists are max')
    elif checkout == 'm':
        if musket['speed'] == 40:
            musket1 = input('Would you like to buy level 1 musket for $200? (y/n) ')
            if musket1 == 'y':
                if game_stats['money'] < 200:
                    print('You dont have enough money')
                else:
                    money(200)
                    musket['speed'] = 60
                    musket['power'] = 60
                    print('Thank you for coming')
            elif musket1 == 'n':
                print('come again')
            else:
                print(random.choice(what))
        elif musket['speed'] == 60:
            musket2 = input('Would you like to buy level 2 musket for $300? (y/n) ')
            if musket2 == 'y':
                if game_stats['money'] < 300:
                    print('You dont have enough money')
                else:
                    money(300)
                    musket['speed'] = 70
                    musket['power'] = 75
                    print('Thank you for coming')
            elif musket2 == 'n':
                print('come again')
            else:
                print(random.choice(what))
        else:
            if musket['speed'] == 70:
                musket3 = input('Would you like to buy level 3 musket for $500? (y/n) ')
                if musket3 == 'y':
                    if game_stats['money'] < 500:
                        print('You dont have enough money')
                    else:
                        money(300)
                        musket['speed'] = 80
                        musket['power'] = 90
                        print('Thank you for coming')
                elif musket3 == 'n':
                    print('come again')
                else:
                    print(random.choice(what))
            else:
                print('Looks like your musket is max')
    else:
        if checkout == 'tg':
            if throwing_knife['speed'] == 60:
                knife1 = input('Would you like to buy level 1 knife for $100? (y/n) ')
                if knife1 == 'y':
                    if game_stats['money'] < 100:
                        print('You dont have enough money')
                    else:
                        money(100)
                        throwing_knife['speed'] = 70
                        throwing_knife['power'] = 35
                        print('Thank you for coming')
                elif knife1 == 'n':
                    print('come again')
                else:
                    print(random.choice(what))
            elif throwing_knife['speed'] == 70:
                knife2 = input('Would you like to buy level 2 knife for $200? (y/n) ')
                if knife2 == 'y':
                    if game_stats['money'] < 200:
                        print('You dont have enough money')
                    else:
                        money(200)
                        throwing_knife['speed'] = 80
                        throwing_knife['power'] = 50
                        print('Thank you for coming')
                elif knife2 == 'n':
                    print('come again')
                else:
                    print(random.choice(what))
            else:
                if throwing_knife['speed'] == 80:
                    knife3 = input('Would you like to buy level 3 knife for $400? (y/n) ')
                    if knife3 == 'y':
                        if game_stats['money'] < 400:
                            print('You dont have enough money')
                        else:
                            money(400)
                            throwing_knife['speed'] = 90
                            throwing_knife['power'] = 60
                            print('Thank you for coming')
                    elif knife3 == 'n':
                        print('come again')
                    else:
                        print(random.choice(what))
                else:
                    print('Looks like your knife is max')
        elif checkout == 's':
            if shotgun['speed'] == 50:
                shotgun1 = input('Would you like to buy level 1 shotgun for $150? (y/n) ')
                if shotgun1 == 'y':
                    if game_stats['money'] < 150:
                        print('You dont have enough money')
                    else:
                        money(150)
                        shotgun['speed'] = 60
                        shotgun['power'] = 50
                        print('Thank you for coming')
                elif shotgun1 == 'n':
                    print('come again')
                else:
                    print(random.choice(what))
            elif shotgun['speed'] == 60:
                shotgun2 = input('Would you like to buy level 2 shotgun for $300? (y/n) ')
                if shotgun2 == 'y':
                    if game_stats['money'] < 300:
                        print('You dont have enough money')
                    else:
                        money(300)
                        shotgun['speed'] = 65
                        shotgun['power'] = 65
                        print('Thank you for coming')
                elif shotgun2 == 'n':
                    print('come again')
                else:
                    print(random.choice(what))
            else:
                if shotgun['speed'] == 65:
                    shotgun3 = input('Would you like to buy level 3 shotgun for $400? (y/n) ')
                    if shotgun3 == 'y':
                        if game_stats['money'] < 400:
                            print('You dont have enough money')
                        else:
                            money(400)
                            shotgun['speed'] = 70
                            shotgun['power'] = 70
                            print('Thank you for coming')
                    elif shotgun3 == 'n':
                        print('come again')
                    else:
                        print(random.choice(what))
                else:
                    print('Looks like your knife is max')
        else:
            if flamegun['speed'] == 30:
                flamegun1 = input('Would you like to buy level 1 flamegun for $300? (y/n) ')
                if flamegun1 == 'y':
                    if game_stats['money'] < 300:
                        print('You dont have enough money')
                    else:
                        money(300)
                        flamegun['speed'] = 50
                        flamegun['power'] = 30
                        print('Thank you for coming')
                elif flamegun1 == 'n':
                    print('come again')
                else:
                    print(random.choice(what))
            elif flamegun['speed'] == 50:
                flamegun2 = input('Would you like to buy level 2 flamegun for $400? (y/n) ')
                if flamegun2 == 'y':
                    if game_stats['money'] < 400:
                        print('You dont have enough money')
                    else:
                        money(400)
                        flamegun['speed'] = 70
                        flamegun['power'] = 60
                        print('Thank you for coming')
                elif flamegun2 == 'n':
                    print('come again')
                else:
                    print(random.choice(what))
            else:
                if flamegun['speed'] == 70:
                    flamegun3 = input('Would you like to buy level 3 flamegun for $600? (y/n) ')
                    if flamegun3 == 'y':
                        if game_stats['money'] < 600:
                            print('You dont have enough money')
                        else:
                            money(600)
                            flamegun['speed'] = 90
                            flamegun['power'] = 90
                            print('Thank you for coming')
                    elif flamegun3 == 'n':
                        print('come again')
                    else:
                        print(random.choice(what))
                else:
                    print('Looks like your knife is max')
def health(checkout):
    time.sleep(2)
    if checkout == 's':
        if game_stats['money'] < 50:
            print('You dont have enough money')
        else:
            money(50)
            game_stats['health'] = game_stats['health'] + 30
            if game_stats['health'] > 100:
                heal()
                print('You bought the small health pack, your health is now ' + str(game_stats['health']))
            else:
                print('You bought the small health pack, your health is now ' + str(game_stats['health']))
    elif checkout == 'm':
        if game_stats['money'] < 100:
            print('You dont have enough money')
        else:
            money(100)
            game_stats['health'] = game_stats['health'] + 50
            if game_stats['health'] > 100:
                heal()
                print('You bought the medium health pack, your health is now ' + str(game_stats['health']))
            else:
                print('You bought the medium health pack, your health is now ' + str(game_stats['health']))
    else:
        if checkout == 'l':
            if game_stats['money'] < 200:
                print('You dont have enough money')
            else:
                money(200)
                heal()
                print('You bought the large health pack, your health is now ' + str(game_stats['health']))
        else:
            if game_stats['money'] < 400:
                print('You dont have enough money')
            else:
                money(400)
                game_stats['health'] = 300
                print('You bought the armor, your health is now ' + str(game_stats['health']))
    time.sleep(2)
    print('Thank you for coming')
def market():
    print('Welcome to the market!')
    print('Here you can buy items to improve your gameplay')
    print('You can also upgrade your weapons')
    time.sleep(2)
    while True:
        time.sleep(2)
        print('"ug" for upgrading weapons')
        print('"h" for heal packs and armor')
        print('"b" to go back')
        pickin = input('What would you like to buy? ')
        time.sleep(2)
        if pickin == 'ug':
            while True:
                print('"f" for fists')
                print('"m" for musket')
                print('"tf" for throwing_knifes')
                print('"s" for shotgun')
                print('"fg" for flamegun')
                print('"b" to go back')
                buy_upgrade = input('What would you like to upgrade? ')
                if buy_upgrade == 'f':
                    print('fists')
                    upgrade('f')
                    break
                elif buy_upgrade == 'm':
                    print('musket')
                    upgrade('m')
                    break
                else:
                    if buy_upgrade == 'tf':
                        print('throwin_knife')
                        upgrade('tf')
                        break
                    elif buy_upgrade == 's':
                        print('shotgun')
                        upgrade('s')
                        break
                    else:
                        if buy_upgrade == 'fg':
                            print('flamegun')
                            upgrade('fg')
                            break
                        elif buy_upgrade == 'b':
                            time.sleep(2)
                            break
                        else:
                            print(random.choice(what))
                            time.sleep(2)
                            continue
        elif pickin == 'h':
            while True:
                print('"s" for small health pack, $50')
                print('"m" for medium health pack, $100')
                print('"l" for large health pack, $200')
                print('"a" for body armor, $400')
                print('"b" to go back')
                pickin = input('What would you like to buy? ')
                if pickin == 's':
                    health('s')
                    break
                elif pickin == 'm':
                    health('m')
                    break
                else:
                    if pickin == 'l':
                        health('l')
                        break
                    elif pickin == 'a':
                        health('a')
                        break
                    else:
                        if pickin == 'b':
                            time.sleep(2)
                            break
                        else:
                            print(random.choice(what))
                            time.sleep(2)
                            continue
        else:
            if pickin == 'b':
                break
            else:
                print(random.choice(what))
                time.sleep(2)
                continue
    time.sleep(2)
    print('Leaving store..')
    time.sleep(2)
def play():
    time.sleep(2)
    while True:
        print('"e" for easy')
        print('"n" for normal')
        print('"h" for hard')
        print('"m" for market')
        print('"b" to go back')
        gamestarts = input('What the difficulty you want to try? ')
        if gamestarts == 'e':
            playing(monster1, boss1)
            break
        elif gamestarts == 'n':
            playing(monster2, boss2)
            break
        else:
            if gamestarts == 'h':
                playing(monster3, boss3)
                break
            elif gamestarts =='m':
                market()
            else:
                if gamestarts == 'b':
                    time.sleep(2)
                    break
                else:
                    print(random.choice(what))
                    time.sleep(2)
                    continue
def next_round(mon):
    print('Next monster coming..')
    time.sleep(2)
    combat(mon)
    time.sleep(2)
    respawn()
def playing(difficulty, final):
    if difficulty == monster1:
        print('easy mode selected')
    elif difficulty == monster2:
        print('normal mode selected')
    else:
        print('hard mode selected')
    time.sleep(random.choice(range(1, 6)))
    print('Loading...')
    time.sleep(random.choice(range(1, 6)))
    print('Game Start!')
    while True:
        next_round(difficulty)
        if game_stats['health'] <= 0:
            game_stats['health'] = 50
            print('You will respawn with 50 health')
            break
        else:
            next_round(difficulty)
            if game_stats['health'] <= 0:
                game_stats['health'] = 50
                print('You will respawn with 50 health')
                break
            else:
                next_round(final)
                if game_stats['health'] <= 0:
                    game_stats['health'] = 50
                    print('You will respawn with 50 health')
                    break
                else:
                    print('Congrats')
                    break
    print('Returning to menu..')
    time.sleep(2)
def combat(mon):
    if mon == monster1:
        power = range(10, 16)
    elif mon == monster2:
        power = range(15, 21)
    else:
        if mon == monster3:
            power = range(30, 41)
        elif mon == boss1:
            power = range(10, 21)
        else:
            if mon == boss2:
                power = range(20, 31)
            else:
                power = range(10, 81)
    while True:
        if game_stats['weapon_stats']['speed'] > mon['speed']:
            print('You attacked the monster first')
            attack = random.choice(missrate)
            if attack == 'hit':
                print('You hit the monster')
                crit = random.choice(critrate)
                if crit == 'hit':
                    you_crit_mon(mon)
                    if mon['health'] <= 0:
                        mon_down(mon)
                        break
                    else:
                        print('The monster now attacks you')
                        mon['power'] = random.choice(power)
                        attack = random.choice(missrate)
                        if attack == 'hit':
                            print('The monster hit you')
                            crit = random.choice(critrate)
                            if crit == 'hit':
                                mon_crit_you(mon)
                                if game_stats['health'] <= 0:
                                    print('Oh no..Game over')
                                    break
                                else:
                                    continue
                            else:
                                mon_fight(mon)
                                if game_stats['health'] <= 0:
                                    print('Oh no..Game over')
                                    break
                                else:
                                    continue
                        else:
                            print('The monster miss you')
                            continue
                else:
                    you_fight(mon)
                    if mon['health'] <= 0:
                        mon_down(mon)
                        break
                    else:
                        print('The monster now attacks you')
                        mon['power'] = random.choice(power)
                        attack = random.choice(missrate)
                        if attack == 'hit':
                            print('The monster hit you')
                            crit = random.choice(critrate)
                            if crit == 'hit':
                                mon_crit_you(mon)
                                if game_stats['health'] <= 0:
                                    print('Oh no..Game over')
                                    break
                                else:
                                    continue
                            else:
                                mon_fight(mon)
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
                        mon_crit_you(mon)
                        if game_stats['health'] <= 0:
                            print('Oh no..Game over')
                            break
                        else:
                            continue
                    else:
                        mon_fight(mon)
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
                    mon_crit_you(mon)
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
                                you_crit_mon(mon)
                                if mon['health'] <= 0:
                                    mon_down(mon)
                                    break
                                else:
                                    continue
                            else:
                                you_fight(mon)
                                if mon['health'] <= 0:
                                    mon_down(mon)
                                    break
                                else:
                                    continue
                        else:
                            print('You miss the monster')
                            continue
                else:
                    mon_fight(mon)
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
                                you_crit_mon(mon)
                                if mon['health'] <= 0:
                                    mon_down(mon)
                                    break
                                else:
                                    continue
                            else:
                                you_fight(mon)
                                if mon['health'] <= 0:
                                    mon_down(mon)
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
                        you_crit_mon(mon)
                        if mon['health'] <= 0:
                            mon_down(mon)
                            break
                        else:
                            continue
                    else:
                        you_fight(mon)
                        if mon['health'] <= 0:
                            mon_down(mon)
                            break
                        else:
                            continue
                else:
                    print('You miss the monster')
                    continue
def you_fight(mon):
    print('You did ' + str(game_stats['weapon_stats']['power']) + ' damage to the monster')
    mon['health'] = mon['health'] - game_stats['weapon_stats']['power']
def mon_fight(mon):
    print('The monster did ' + str(mon['power']) + ' damage to you')
    game_stats['health'] = game_stats['health'] - mon['power']
def you_crit_mon(mon):
    print('Critical hit!')
    print('You did ' + str(game_stats['weapon_stats']['power']*2) + ' damage to the monster')
    mon['health'] = mon['health'] - game_stats['weapon_stats']['power']*2
def mon_crit_you(mon):
    print('Critical hit!')
    print('The monster did ' + str(mon['power']*2) + ' damage to you')
    game_stats['health'] = game_stats['health'] - mon['power']*2
def mon_down(mon):
    print('monster down')
    game_stats['monsters_killed'] = game_stats['monsters_killed'] + 1
    game_stats['money'] = game_stats['money'] + mon['cost']
    game_stats['xp'] = game_stats['xp'] + mon['xp']
#program starts
what = ['What?', 'Can you repeat that', 'Try again', 'No']
print('Your current weapon are your hands, you can get a weapon in the storage room')
print('"p" to start the game.')
print('"s" to see your player stats.')
print('"w" to see the list of weapons.')
print('"st" to see your storage.')
print('"b" to exit and end the game *note that all your data will be lost.')
print('"m" to see the menu')
def os():
    while True:
        start = input('What would you like to do? ')
        if start == 'p':
            play()
            continue
        elif start == 's':
            stats()
            continue
        else:
            if start == 'w':
                weapons()
                continue
            elif start == 'st':
                storage()
                continue
            else:
                if start == 'b':
                    time.sleep(2)
                    break
                elif start == 'm':
                    menu()
                    continue
                else:
                    print(random.choice(what))
                    time.sleep(2)
                    continue
os()
print('Thanks for playing!')



    
