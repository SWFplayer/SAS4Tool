from colorama import Fore, init
from encodingDecoding import *
import time
from os import system, name, _exit
import options as opt
init(autoreset=True)

GREEN = Fore.GREEN

def clear():
    system('cls' if name == 'nt' else 'clear')

def title():
    clear()
    print(f'''{GREEN}
                 █████████    █████████    █████████  █████ █████  ███████████    ███████       ███████    █████      
               ███░░░░░███  ███░░░░░███  ███░░░░░███░░███ ░░███  ░█░░░███░░░█  ███░░░░░███   ███░░░░░███ ░░███       
             ░███    ░░░  ░███    ░███ ░███    ░░░  ░███  ░███ █░   ░███  ░  ███     ░░███ ███     ░░███ ░███       
            ░░█████████  ░███████████ ░░█████████  ░███████████    ░███    ░███      ░███░███      ░███ ░███       
            ░░░░░░░░███ ░███░░░░░███  ░░░░░░░░███ ░░░░░░░███░█    ░███    ░███      ░███░███      ░███ ░███       
           ███    ░███ ░███    ░███  ███    ░███       ░███░     ░███    ░░███     ███ ░░███     ███  ░███      █
         ░░█████████  █████   █████░░█████████        █████     █████    ░░░███████░   ░░░███████░   ███████████
         ░░░░░░░░░  ░░░░░   ░░░░░  ░░░░░░░░░        ░░░░░     ░░░░░       ░░░░░░░       ░░░░░░░    ░░░░░░░░░░░\n\n''')

def o1():
    title()
    o1options = input('''
[1] Set factions war guild
[2] Set factions war credits
\n>''')
    if o1options == '1':
        opt.factionGuild()
    elif o1options == '2':
        opt.factionCredits()
    else:
        title()
        print('Invalid option.')
        time.sleep(3)
        return o1()

def o2():
    title()
    o2options = input('''
[1] Set revive tokens
[2] Set black keys
[3] Set black strongboxes
[4] Set augment cores
[5] Set sas cash
[6] Remove ads
[7] Set nightmare premium tickets
[8] Add 2 pay to unlock profiles
[9] Set support items
[10] Set mastery to max level
[11] Set free skill reset
[12] Change profile username
[13] Set player level
\n>''')
    if o2options == '1':
        opt.reviveTokens()
    elif o2options == '2':
        opt.blackKeys()
    elif o2options == '3':
        opt.blackBox()
    elif o2options == '4':
        opt.augCores()
    elif o2options == '5':
        opt.sasCash()
    elif o2options == '6':
        opt.removeAds()
    elif o2options == '7':
        opt.premiumTickets()
    elif o2options == '8':
        opt.premProfile()
    elif o2options == '9':
        opt.setSupport()
    elif o2options == '10':
        opt.mastery()
    elif o2options == '11':
        opt.skillReset()
    elif o2options == '12':
        opt.changeProfileName()
    elif o2options == '13':
        opt.setLVL()
    else:
        title()
        print('Invalid option.')
        time.sleep(3)
        return o2()

def o3():
    opt.premGuns()

def o4():
    opt.collection()

def o5():
    title()
    o5options = input('[1] Add weapons\n[2] Add equipment\n\n>')
    if o5options == '1':
        opt.weapons()
    elif o5options == '2':
        opt.equipment()
    else:
        title()
        print('Invalid option.')
        time.sleep(3)
        return o5()

def mainMenu():
    title()
    mainMenuOptions = input('''
[1] Factions Options
[2] Profile Options
[3] Set premium guns
[4] Unlock all collections
[5] Add Weapon/Armor to the inventory
[6] Decode/Encode Profile.save to a json file
[7] Exit
\n>''')
    if mainMenuOptions == '1':
        o1()
    elif mainMenuOptions == '2':
        o2()
    elif mainMenuOptions == '3':
        o3()
    elif mainMenuOptions == '4':
        o4()
    elif mainMenuOptions == '5':
        o5()
    elif mainMenuOptions == '6':
        opt.decodeEnc()
    elif mainMenuOptions == '7':
        title()
        print('Exiting...')
        time.sleep(1)
        _exit(0)
    else:
        title()
        print('Invalid option.')
        time.sleep(3)
        return mainMenu()

def main():
    mainMenu()

if __name__ == '__main__':
    main()