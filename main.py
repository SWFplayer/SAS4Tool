from colorama import Fore, init
from encodingDecoding import *
import time, os
from os import system, name
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
[1] Set faction guild
[2] Set planet currency
\n>''')
    if o1options == '1':
        if os.path.exists('Profile_packed.save'):
            os.remove('Profile_packed.save')
        title()
        factionCode = input('Please, move your "Profile.save" to the current folder.\n\nType your faction code (Ex: XKLFHL)\n\n>')
        title()
        factionGuild = input('Type your faction guild (Ex: SPARTANS)\n\n>')
        title()
        print("Loading, please wait...")
        decodeProfileSave()
        time.sleep(5)
        with open('Profile_unpacked.json', 'r+') as f:
            data = json.load(f)
            f.seek( 0 )
            f.truncate()
            data['CurrentFactionWarMatch'] = factionCode.upper()
            data['CurrentFactionWarFaction'] = factionGuild.upper()
            json.dump(data, f)
        encodeProfileSave()
        time.sleep(5)
        os.remove('Profile_unpacked.json')
        title()
        print('Profile.save has been successfuly updated.')
        time.sleep(3)
        return mainMenu()
    elif o1options == '2':
        title()
    else:
        title()
        print('Invalid option.')

def o2():
    title()

def mainMenu():
    title()
    mainMenuOptions = input('''
[1] Factions
[2] Profiles
[3] Set premium guns
[4] Set revive tokens
[5] Unlock all collections
\n>''')
    if mainMenuOptions == '1':
        o1()
    elif mainMenuOptions == '2':
        o2()
    else:
        title()
        print('Invalid option.')
        time.sleep(3)
        return mainMenu()

def main():
    mainMenu()

if __name__ == '__main__':
    main()