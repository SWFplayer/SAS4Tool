from colorama import Fore, init
from encodingDecoding import *
import time, os, random
from os import system, name
init(autoreset=True)

GREEN = Fore.GREEN
NUMS = '123456789'

def factionGuild():
    title()
    factionCode = input('Please, move your "Profile.save" to the current folder.\n\nType your faction code (Ex: XKLFHL)\n\n>')
    title()
    factionGuild = input('Type your faction guild (Ex: SPARTANS)\n\n>')
    title()
    print("Loading, please wait...")
    decodeProfileSave()
    with open('Profile_unpacked.json', 'r+') as f:
        data = json.load(f)
        f.seek( 0 )
        f.truncate()
        data['CurrentFactionWarMatch'] = factionCode.upper()
        data['CurrentFactionWarFaction'] = factionGuild.upper()
        json.dump(data, f)
    if os.path.exists('Profile.save'):
        os.remove('Profile.save')
    encodeProfileSave()
    os.remove('Profile_unpacked.json')
    title()
    print('Profile.save has been successfuly updated.')
    time.sleep(3)
    return mainMenu()

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
        factionGuild()
    elif o1options == '2':
        try:
            title()
            factionWarCurrency = int(input('Set your ammount for faction war credits\n\n>'))
            title()
            planetZCurrency = int(input('Set your planet Zeta credits\n\n>'))
            title()
            planetECurrency = int(input('Set your planet Epsilon credits\n\n>'))
            title()
            planetSCurrency = int(input('Set your planet Sigma credits\n\n>'))
            title()
            planetXCurrency = int(input('Set your planet Xi credits\n\n>'))
            title()
            planetOCurrency = int(input('Set your planet Omicron credits\n\n>'))
        except ValueError as err:
            title()
            print("Please, enter a valid number.")
            time.sleep(3)
            return o1()
        title()
        print('Loading, please wait...')
        decodeProfileSave()
        with open('Profile_unpacked.json', 'r+') as f:
            data = json.load(f)
            f.seek( 0 )
            f.truncate()
            data['FactionWarCredits'] = factionWarCurrency
            data['FactionWarPlanetArray'][0]['Currency'] = planetZCurrency
            data['FactionWarPlanetArray'][1]['Currency'] = planetECurrency
            data['FactionWarPlanetArray'][2]['Currency'] = planetSCurrency
            data['FactionWarPlanetArray'][3]['Currency'] = planetXCurrency
            data['FactionWarPlanetArray'][4]['Currency'] = planetOCurrency
            json.dump(data, f)
        if os.path.exists('Profile.save'):
            os.remove('Profile.save')
        encodeProfileSave()
        os.remove('Profile_unpacked.json')
        title()
        print('Profile.save has been successfuly updated.')
        time.sleep(3)
        return mainMenu()
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
[8] Change player stats
\n>''')
    if o2options == '1':
        title()
        try:
            tokens = int(input('Set your revive tokens ammount\n\n>'))
        except ValueError as err:
            title()
            print("Please, enter a valid number.")
            time.sleep(3)
            return o2()
        decodeProfileSave()
        with open('Profile_unpacked.json', 'r+') as f:
            data = json.load(f)
            f.seek( 0 )
            f.truncate()
            data['Global']['ReviveTokens'] = tokens
            json.dump(data, f)
        if os.path.exists('Profile.save'):
            os.remove('Profile.save')
        encodeProfileSave()
        os.remove('Profile_unpacked.json')
        title()
        print('Profile.save has been successfuly updated.')
        time.sleep(3)
        return mainMenu()
    elif o2options == '2':
        title()
        profile = input('Please, select your profile. (From left to right.)\n\n[1] Profile 1\n\n[2] Profile 2\n\n[3] Profile 3\n\n[4] Profile 4\n\n[5] Profile 5\n\n[6] Profile 6\n\n>')
        if profile == '1':
            profile = 'Profile0'
        elif profile == '2':
            profile = 'Profile1'
        elif profile == '3':
            profile = 'Profile2'
        elif profile == '4':
            profile = 'Profile3'
        elif profile == '5':
            profile = 'Profile4'
        elif profile == '6':
            profile = 'Profile5'
        else:
            title()
            print('This profile does not exist.')
            time.sleep(3)
            return o2()
        title()
        try:
            blackkeys = int(input('Set your back keys ammount\n\n>'))
        except ValueError as err:
            title()
            print("Please, enter a valid number.")
            time.sleep(3)
            return o2()
        title()
        print('Loading, please wait...')
        decodeProfileSave()
        with open('Profile_unpacked.json', 'r+') as f:
            data = json.load(f)
            f.seek( 0 )
            f.truncate()
            data['Inventory'][f'{profile}']['Skills']['AvailableBlackKeys'] = blackkeys
            json.dump( data, f )
        if os.path.exists('Profile.save'):
            os.remove('Profile.save')
        encodeProfileSave()
        os.remove('Profile_unpacked.json')
        title()
        print('Profile.save has been successfuly updated.')
        time.sleep(3)
        return mainMenu()
    elif o2options == '3':
        title()
        profile = input('Please, select your profile. (From left to right.)\n\n[1] Profile 1\n[2] Profile 2\n[3] Profile 3\n[4] Profile 4\n[5] Profile 5\n[6] Profile 6\n\n>')
        if profile == '1':
            profile = 'Profile0'
        elif profile == '2':
            profile = 'Profile1'
        elif profile == '3':
            profile = 'Profile2'
        elif profile == '4':
            profile = 'Profile3'
        elif profile == '5':
            profile = 'Profile4'
        elif profile == '6':
            profile = 'Profile5'
        else:
            title()
            print('This profile does not exist.')
            time.sleep(3)
            return o2()
        title()
        try:
            blackbox = int(input('Set your black strongboxes ammount\n\n>'))
        except ValueError as err:
            title()
            print("Please, enter a valid number.")
            time.sleep(3)
            return o2()
        title()
        print("Loading, please wait...")
        decodeProfileSave()
        for x in range(0, blackbox): # Ammount of black boxes to generate
            genBox = ''
            for x in range(0, 10):
                chars = random.choice(NUMS)
                genBox = genBox + chars
            with open('Profile_unpacked.json', 'r+') as f:
                data = json.load(f)
                f.seek( 0 )
                f.truncate()
                data['Inventory'][f'{profile}']['Skills']['AvailableBlackStrongboxes'].append(int(genBox))
                json.dump(data, f, indent=4, sort_keys=False)
        if os.path.exists('Profile.save'):
            os.remove('Profile.save')
        encodeProfileSave()
        os.remove('Profile_unpacked.json')
        title()
        print('Profile.save has been successfuly updated.')
        time.sleep(3)
        return mainMenu()
    elif o2options == '4':
        title()
    elif o2options == '5':
        title()
    elif o2options == '6':
        title()
    elif o2options == '7':
        title()
    elif o2options == '8':
        title()
    else:
        title()
        print('Invalid option.')
        time.sleep(3)
        return o2()

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