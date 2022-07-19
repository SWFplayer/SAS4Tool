from time import sleep
from _UTILS_ import ProfilePath, encode_profile as encode_pf, decode_profile as decode_pf, mainTitle
from json import load, dump
from os import path, remove
from string import ascii_letters
from win32console import SetConsoleTitle
from msvcrt import getch, kbhit




def ENDFUNC():
    PATH = ProfilePath()
    if path.exists(f'{PATH}\\Profile.save'):
        remove(f'{PATH}\\Profile.save')
    encode_pf()
    if path.exists(f'{PATH}\\Profile_unpacked.json'):
        remove(f'{PATH}\\Profile_unpacked.json')
    if path.exists(f'{PATH}\\IDs.json'):
        remove(f'{PATH}\\IDs.json')
    mainTitle()
    print('Done!')
    sleep(1)
    pass

def setFactionGuild():
    PATH = ProfilePath()
    SetConsoleTitle('SAS4Tool - Factions/Guild')
    GUILDS = ['GUARDIANS', 'NOMADS', 'OUTLAWS', 'VANGUARD', 'SPARTANS']
    mainTitle()
    try:
        code = input('Enter faction code\n\n> ')
    except ValueError:
        mainTitle()
        print('Code only can contain letters')
        sleep(1)
        return setFactionGuild()
    mainTitle()
    for i in range(len(GUILDS)):
        print(f'[{ascii_letters[26+i]}] - {GUILDS[i]}')
    sleep(0.25)
    while True:
        if kbhit():
            key = getch()
            if key == b'a':
                guild = GUILDS[0]
                break
            if key == b'b':
                guild = GUILDS[1]
                break
            if key == b'c':
                guild = GUILDS[2]
                break
            if key == b'd':
                guild = GUILDS[3]
                break
            if key == b'e':
                guild = GUILDS[4]
                break
    mainTitle()
    print('Loading...')
    decode_pf()
    with open(f'{PATH}\\Profile_unpacked.json', 'r+') as f:
        data = load(f)
        f.seek(0)
        f.truncate()
        data['CurrentFactionWarMatch'] = code.upper()
        data['CurrentFactionWarFaction'] = guild.upper()
        dump(data, f)
    ENDFUNC()

def setFactionCredits():
    SetConsoleTitle('SAS4Tool - Factions/Credits')
    mainTitle()
    print('''
[A] - Zeta credits
[B] - Epsilon credits
[C] - Sigma credits
[D] - Xi credits
[E] - Omicron credits
[F] - Faction credits
[G] - All credits
[H] - Back''')
    sleep(0.25)
    while True:
        if kbhit():
            key = getch()
            if key == b'a':
                SetCredits('planet', 0)
                break
            if key == b'b':
                SetCredits('planet', 1)
                break
            if key == b'c':
                SetCredits('planet', 2)
                break
            if key == b'd':
                SetCredits('planet', 3)
                break
            if key == b'e':
                SetCredits('planet', 4)
                break
            if key == b'f':
                SetCredits('faction', 0)
                break
            if key == b'g':
                SetCredits('all', 0)
            if key == b'h':
                return None
    
def SetCredits(Type, Planet):
    PATH = ProfilePath()
    mainTitle()
    try:
        amount = int(input(f'Enter {Type} credits\n\n> '))
    except ValueError:
        mainTitle()
        print('Credits only can contain numbers')
        sleep(1)
        return SetCredits(Type, Planet)
    mainTitle()
    print('Loading...')
    decode_pf()
    with open(f'{PATH}\\Profile_unpacked.json', 'r+') as f:
        data = load(f)
        f.seek(0)
        f.truncate()
        if Type == 'planet':
            data['FactionWarPlanetArray'][Planet]['Currency'] = amount
            dump(data, f)
        if Type == 'faction':
            data['FactionWarCredits'] = amount
            dump(data, f)
        if Type == 'all':
            data['FactionWarCredits'] = amount
            data['FactionWarPlanetArray'][Planet]['Currency'] = amount
            dump(data, f)
    ENDFUNC()

def factionsOptionMenu():
    SetConsoleTitle('SAS4Tool - Factions')
    mainTitle()
    print('''
[A] - Factions Guild
[B] - Factions Credits
[C] - Back''')
    sleep(0.25)
    while True:
        if kbhit():
            key = getch()
            if key == b'a':
                setFactionGuild()
                break
            if key == b'b':
                setFactionCredits()
                break
            if key == b'c':
                return None
    pass

def addPremiumItems():
    PATH = ProfilePath()
    SetConsoleTitle('SAS4Tool - Premium items')
    mainTitle()
    PREMIUM_LIST = ['Ahab', 'Banshee', 'Bayonet', 'Calamity', 'CM 000 Kelvin', 'CM 352 Quasar', 'CM 369 Starfury', 'CM 467', 'CM 505 Alpha Ltd. Edition', 'CM Laser Drill', 'CM Proton Arc', 'Contagion', 'Donderbus', 'Handkanone', 'HIKS 888 CAW', 'HIKS A10', 'HIKS S4000', 'Planet Stormer Ltd. Edition', 'RIA 15 SE', 'RIA 75', 'RIA 8A', 'Ricochet', 'Ronson 5X5', 'Ronson WPX Incinerator', 'Supermarine Alpha Ltd. Edition', 'T-189 MGL', 'Torment', 'Vitrol', 'Zerfallen']
    print('''
[A] - Remove Premium Item
[B] - Add Premium Item
[C] - Back''')
    sleep(0.25)
    while True:
        if kbhit():
            key = getch()
            if key == b'a':
                opt = 0
                break
            if key == b'b':
                opt = 1
                break
            if key == b'c':
                return None
    mainTitle()
    for i in range(len(PREMIUM_LIST)):
        print(f'[{i+1}] - {PREMIUM_LIST[i]}')
    try:
        inp = int(input('\n> '))
    except ValueError:
        mainTitle()
        print('Code only can contain numbers')
        sleep(1)
        return addPremiumItems()
    if inp > len(PREMIUM_LIST) or inp < 1:
        mainTitle()
        print('Invalid option.')
        sleep(1)
        return addPremiumItems()
    mainTitle()
    print('Loading...')
    decode_pf()
    with open(f'{PATH}\\Profile_unpacked.json', 'r+') as f:
        data = load(f)
        f.seek(0)
        f.truncate()
        if opt == 0:
            data['PurchasedIAP']['PurchasedIAPArray'][inp + 1]['Value'] = False
            dump(data, f)
        if opt == 1:
            data['PurchasedIAP']['PurchasedIAPArray'][inp + 1]['Value'] = True
            dump(data, f)
    ENDFUNC()

def addRevive():
    PATH = ProfilePath()
    SetConsoleTitle('SAS4Tool - Revive tokens')
    mainTitle()
    try:
        amount = int(input('Enter revive amount\n\n> '))
    except ValueError:
        mainTitle()
        print('amount only can contain numbers')
        sleep(1)
        return addRevive()
    if amount < 0:
        mainTitle()
        print('amount must be greater than 0')
        sleep(1)
        return addRevive()
    mainTitle()
    print('Loading...')
    decode_pf()
    with open(f'{PATH}\\Profile_unpacked.json', 'r+') as f:
        data = load(f)
        f.seek(0)
        f.truncate()
        data['Global']['ReviveTokens'] = amount
        dump(data, f)
    ENDFUNC()

def AddNightmareTickets():
    PATH = ProfilePath()
    SetConsoleTitle('SAS4Tool - Premium Nightmare tickets')
    mainTitle()
    try:
        amount = int(input('Enter nightmare tickets amount\n\n> '))
    except ValueError:
        mainTitle()
        print('amount only can contain numbers')
        sleep(1)
        return AddNightmareTickets()
    if amount < 0:
        mainTitle()
        print('amount must be greater than 0')
        sleep(1)
        return AddNightmareTickets()
    mainTitle()
    print('Loading...')
    decode_pf()
    with open(f'{PATH}\\Profile_unpacked.json', 'r+') as f:
        data = load(f)
        f.seek(0)
        f.truncate()
        data['Global']['AvailablePremiumTickets'] = amount
        dump(data, f)
    ENDFUNC()

def removeAds():
    PATH = ProfilePath()
    SetConsoleTitle('SAS4Tool - Remove ads')
    mainTitle()
    print('''
[A] - Deactivate Ads
[B] - Activate Ads
[C] - Back''')
    while True:
        if kbhit():
            key = getch()
            if key == b'a':
                boolean = True
                break
            if key == b'b':
                boolean = False
                break
            if key == b'c':
                return None
    mainTitle()
    print('Loading...')
    decode_pf()
    with open(f'{PATH}\\Profile_unpacked.json', 'r+') as f:
        data = load(f)
        f.seek(0)
        f.truncate()
        data['Global']['ForceRemoveAds'] = boolean
        dump(data, f)
    ENDFUNC()

def unlockProfiles():
    PATH = ProfilePath()
    SetConsoleTitle('SAS4Tool - Lock/Unlock profiles')
    mainTitle()
    print('''
[A] - Unlock profiles
[B] - Lock profiles
[C] - Back''')
    while True:
        if kbhit():
            key = getch()
            if key == b'a':
                boolean = True
                break
            if key == b'b':
                boolean = False
                break
            if key == b'c':
                return None
    mainTitle()
    print('Loading...')
    decode_pf()
    with open(f'{PATH}\\Profile_unpacked.json', 'r+') as f:
        data = load(f)
        f.seek(0)
        f.truncate()
        data['PurchasedIAP']['PurchasedIAPArray'][0]['Value'] = boolean
        data['PurchasedIAP']['PurchasedIAPArray'][1]['Value'] = boolean
        dump(data, f)
    ENDFUNC()