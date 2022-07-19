from base64 import decode
from re import I
from numpy import random
from time import sleep
from _UTILS_ import ProfilePath, encode_profile as encode_pf, decode_profile as decode_pf, mainTitle, isWindowFocused, gunStrongbox, equipmentStrongbox, IDs
from json import load, dump, loads
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

def addItemsMenu():
    SetConsoleTitle('SAS4Tool - Add Items')
    mainTitle()
    print('''
[A] - Add guns
[B] - Add equipment
[C] - Back''')
    while True:
        if kbhit():
            key = getch()
            if key == b'a':
                addGun0()
                break
            if key == b'b':
                addEquipment0()
                break
            if key == b'c':
                break


def addGun2(GunType, gunVer):
    PATH = ProfilePath()
    itemIDs = loads(IDs)
    mainTitle()
    for i in range(len(itemIDs['weaponIDs'][GunType][gunVer])):
        print(f'[{i+1}] - {itemIDs["weaponIDs"][GunType][gunVer][i]["Name"]}')
    try:
        a = int(input('\n> '))
    except ValueError:
        mainTitle()
        print('Invalid input!')
        sleep(1)
        return addGun2(GunType, gunVer)
    if a <= 0 or a > len(itemIDs['weaponIDs'][GunType][gunVer]):
        mainTitle()
        print('Invalid input!')
        sleep(1)
        return addGun2(GunType, gunVer)
    try:
        gun = itemIDs['weaponIDs'][GunType][gunVer][a-1]['ID']
    except IndexError:
        mainTitle()
        print('Invalid input!')
        sleep(1)
        return addGun2(GunType, gunVer)
    mainTitle()
    try:
        aug = int(input('Set item stars/augment slots (0-4)\n\n> '))
    except ValueError:
        mainTitle()
        print('Invalid input!')
        sleep(1)
        return addGun2(GunType, gunVer)
    if aug > 4 or aug < 0:
        mainTitle()
        print('Invalid input!')
        sleep(1)
        return addGun2(GunType, gunVer)
    mainTitle()
    try:
        grade = int(input('Set item grade (0-12)\n\n> '))
    except ValueError:
        mainTitle()
        print('Invalid input!')
        sleep(1)
        return addGun2(GunType, gunVer)
    if grade > 12 or grade < 0:
        mainTitle()
        print('Invalid input!')
        sleep(1)
        return addGun2(GunType, gunVer)
    mainTitle()
    try:
        bonus = int(input('Set item bonus stats (0-10)\n\n> '))
    except ValueError:
        mainTitle()
        print('Invalid input!')
        sleep(1)
        return addGun2(GunType, gunVer)
    if bonus > 10 or bonus < 0:
        mainTitle()
        print('Invalid input!')
        sleep(1)
        return addGun2(GunType, gunVer)
    mainTitle()
    print('Loading...')
    decode_pf()
    with open('config.json', 'r') as f:
        pf = load(f)
        profile = pf['defaultProfile']
    with open(f'{PATH}\\Profile_unpacked.json', 'r+') as f:
        data = load(f)
        IID = loads(IDs)
        f.seek(0)
        f.truncate()
        strongbox = loads(gunStrongbox)
        strongbox['ID'] = gun
        strongbox['EquipVersion'] = gunVer
        strongbox['Grade'] = grade; strongbox['AugmentSlots'] = aug
        strongbox['BonusStatsLevel'] = bonus
        strongbox['InventoryIndex'] = IID['weaponIDs'][f'{GunType}']['Extra'][0]['Type']
        data['Inventory'][profile]['Strongboxes']['Claimed'].append(int(0))
        data['Inventory'][profile]['Strongboxes']['Claimed'].append(strongbox)
        data['Inventory'][profile]['Strongboxes']['Claimed'].append(int(8))
        data['Inventory'][profile]['Strongboxes']['Claimed'].append(int(0))
        dump(data, f)
    ENDFUNC()


def addGun1(GunType):
    itemIDs = loads(IDs)
    ver = ['Normal', 'Red', 'Black', 'Factions', 'Back']
    mainTitle()
    if ver[3] in itemIDs['weaponIDs'][GunType]:
        for i in range(len(ver)):
            print(f'[{ascii_letters[26+i]}] - {ver[i]}')
        while True:
            if kbhit():
                key = getch()
                if key == b'a':
                    gunVer = ver[0]
                    addGun2(GunType, gunVer)
                    break
                if key == b'b':
                    gunVer = ver[1]
                    addGun2(GunType, gunVer)
                    break
                if key == b'c':
                    gunVer = ver[2]
                    addGun2(GunType, gunVer)
                    break
                if key == b'd':
                    gunVer = ver[3]
                    addGun2(GunType, gunVer)
                    break
                if key == b'e':
                    return addGun0()
    if ver[3] not in itemIDs['weaponIDs'][GunType]:
        ver.pop(3)
        for i in range(len(ver)):
            print(f'[{ascii_letters[26+i]}] - {ver[i]}')
        while True:
            if kbhit():
                key = getch()
                if key == b'a':
                    gunVer = ver[0]
                    addGun2(GunType, gunVer)
                    break
                if key == b'b':
                    gunVer = ver[1]
                    addGun2(GunType, gunVer)
                    break
                if key == b'c':
                    gunVer = ver[2]
                    addGun2(GunType, gunVer)
                    break
                if key == b'd':
                    return addGun0()
def addGun0():
    l = ['Pistol', 'SMG', 'Assault_Rifle', 'Shotgun', 'Sniper', 'Rocket_Launcher', 'Flame_Thrower', 'LMG', 'Disk_Thrower', 'Laser', 'Back']
    SetConsoleTitle('SAS4Tool - Add guns')
    mainTitle()
    for i in range(len(l)):
        print(f'[{ascii_letters[26+i]}] - {l[i].replace("_", " ")}')
    while True:
        if kbhit():
            key = getch()
            if key == b'a':
                gunType = l[0]
                break
            if key == b'b':
                gunType = l[1]
                break
            if key == b'c':
                gunType = l[2]
                break
            if key == b'd':
                gunType = l[3]
                break
            if key == b'e':
                gunType = l[4]
                break
            if key == b'f':
                gunType = l[5]
                break
            if key == b'g':
                gunType = l[6]
                break
            if key == b'h':
                gunType = l[7]
                break
            if key == b'i':
                gunType = l[8]
                break
            if key == b'j':
                gunType = l[9]
                break
            if key == b'k':
                return addItemsMenu()
    addGun1(gunType)

def addEquipment2(equipType, equipVer):
    PATH = ProfilePath()
    itemIDs = loads(IDs)
    mainTitle()
    for i in range(len(itemIDs['equipmentIDs'][equipType][equipVer])):
        print(f'[{i+1}] - {itemIDs["equipmentIDs"][equipType][equipVer][i]["Name"]}')
    try:
        a = int(input('\n> '))
    except ValueError:
        mainTitle()
        print('Invalid input!')
        sleep(1)
        return addEquipment2(equipType, equipVer)
    if a <= 0 or a > len(itemIDs['equipmentIDs'][equipType][equipVer]):
        mainTitle()
        print('Invalid input!')
        sleep(1)
        return addEquipment2(equipType, equipVer)
    mainTitle()
    try:
        equip = itemIDs['equipmentIDs'][equipType][equipVer][a-1]
    except IndexError:
        mainTitle()
        print('Invalid input!')
        sleep(1)
        return addEquipment2(equipType, equipVer)
    mainTitle()
    try:
        aug = int(input('Set item stars/augment slots (0-3)\n\n> '))
    except ValueError:
        mainTitle()
        print('Invalid input!')
        sleep(1)
        return addEquipment2(equipType, equipVer)
    if aug > 3 or aug < 0:
        mainTitle()
        print('Invalid input!')
        sleep(1)
        return addEquipment2(equipType, equipVer)
    mainTitle()
    try:
        grade = int(input('Set item grade (0-12)\n\n> '))
    except ValueError:
        mainTitle()
        print('Invalid input!')
        sleep(1)
        return addEquipment2(equipType, equipVer)
    if grade > 12 or grade < 0:
        mainTitle()
        print('Invalid input!')
        sleep(1)
        return addEquipment2(equipType, equipVer)
    mainTitle()
    try:
        bonus = int(input('Set item bonus (0-10)\n\n> '))
    except ValueError:
        mainTitle()
        print('Invalid input!')
        sleep(1)
        return addEquipment2(equipType, equipVer)
    if bonus > 10 or bonus < 0:
        mainTitle()
        print('Invalid input!')
        sleep(1)
        return addEquipment2(equipType, equipVer)
    mainTitle()
    print('Loading...')
    decode_pf()
    with open('config.json', 'r') as f:
        pf = load(f)
        profile = pf['defaultProfile']
    with open(f'{PATH}\\Profile_unpacked.json', 'r+') as f:
        data = load(f)
        IID = loads(IDs)
        strongbox = loads(equipmentStrongbox)
        f.seek(0)
        f.truncate()
        strongbox['ID'] = equip
        strongbox['EquipVersion'] = equipVer
        strongbox['Grade'] = grade
        strongbox['AugmentSlots'] = aug
        strongbox['BonusStatsLevel'] = bonus
        strongbox['EquippedSlot'] = IID['equipmentIDs'][equipType]['Extra'][0]['Type']
        strongbox['InventoryIndex'] = IID['equipmentIDs'][equipType]['Extra'][0]['Type']
        data['Inventory'][profile]['Strongboxes']['Claimed'].append(int(1))
        data['Inventory'][profile]['Strongboxes']['Claimed'].append(strongbox)
        data['Inventory'][profile]['Strongboxes']['Claimed'].append(int(8))
        data['Inventory'][profile]['Strongboxes']['Claimed'].append(int(0))
        dump(data, f)
    ENDFUNC()

def addEquipment1(equipType):
    itemIDs = loads(IDs)
    ver = ['Normal', 'Red', 'Black', 'Factions', 'Back']
    mainTitle()
    if ver[3] in itemIDs['equipmentIDs'][equipType]:
        for i in range(len(ver)):
            print(f'[{ascii_letters[26+i]}] - {ver[i]}')
        while True:
            if kbhit():
                key = getch()
                if key == b'a':
                    equipVer = ver[0]
                    addEquipment2(equipType, equipVer)
                    break
                if key == b'b':
                    equipVer = ver[1]
                    addEquipment2(equipType, equipVer)
                    break
                if key == b'c':
                    equipVer = ver[2]
                    addEquipment2(equipType, equipVer)
                    break
                if key == b'd':
                    equipVer = ver[3]
                    addEquipment2(equipType, equipVer)
                    break
                if key == b'e':
                    return addEquipment0()
    if ver[3] not in itemIDs['equipmentIDs'][equipType]:
        ver.pop(3)
        for i in range(len(ver)):
            print(f'[{ascii_letters[26+i]}] - {ver[i]}')
        while True:
            if kbhit():
                key = getch()
                if key == b'a':
                    equipVer = ver[0]
                    addEquipment2(equipType, equipVer)
                    break
                if key == b'b':
                    equipVer = ver[1]
                    addEquipment2(equipType, equipVer)
                    break
                if key == b'c':
                    equipVer = ver[2]
                    addEquipment2(equipType, equipVer)
                    break
                if key == b'd':
                    return addEquipment0()

def addEquipment0():
    l = ['Helmet', 'Vest', 'Gloves', 'Pants', 'Boots', 'Back']
    SetConsoleTitle('SAS4Tool - Add equipment')
    mainTitle()
    for i in range(len(l)):
        print(f'[{ascii_letters[26+i]}] - {l[i].replace("_", " ")}')
    while True:
        if kbhit():
            key = getch()
            if key == b'a':
                equipType = l[0]
                break
            if key == b'b':
                equipType = l[1]
                break
            if key == b'c':
                equipType = l[2]
                break
            if key == b'd':
                equipType = l[3]
                break
            if key == b'e':
                equipType = l[4]
                break
            if key == b'f':
                return addItemsMenu()
    addEquipment1(equipType)

def changeUsername():
    PATH = ProfilePath()
    SetConsoleTitle('SAS4Tool - Change username')
    mainTitle()
    name = input('Enter new username\n\n> ')
    mainTitle()
    print('Loading...')
    decode_pf()
    with open('config.json', 'r') as f:
        pf = load(f)
        profile = pf['defaultProfile']
    with open(f'{PATH}\\Profile_unpacked.json', 'r+') as f:
        data = load(f)
        f.seek(0)
        f.truncate()
        data['Inventory'][profile]['Name'] = name
        dump(data, f)
    ENDFUNC()

def addCash():
    PATH = ProfilePath()
    SetConsoleTitle('SAS4Tool - Add SAS Cash')
    mainTitle()
    try:
        amount = int(input('Enter cash amount\n\n> '))
    except ValueError:
        mainTitle()
        print('Invalid input!')
        sleep(1)
        return addCash()
    mainTitle()
    print('Loading...')
    decode_pf()
    with open('config.json', 'r') as f:
        pf = load(f)
        profile = pf['defaultProfile']
    with open(f'{PATH}\\Profile_unpacked.json', 'r+') as f:
        data = load(f)
        f.seek(0)
        f.truncate()
        data['Inventory'][profile]['Money'] = amount
        dump(data, f)
    ENDFUNC()

def setFreeSkillReset():
    PATH = ProfilePath()
    SetConsoleTitle('SAS4Tool - Set free skill reset')
    mainTitle()
    print('Loading...')
    decode_pf()
    with open('config.json', 'r') as f:
        pf = load(f)
        profile = pf['defaultProfile']
    with open(f'{PATH}\\Profile_unpacked.json', 'r+') as f:
        data = load(f)
        f.seek(0)
        f.truncate()
        data['Inventory'][profile]['FreeSkillsReset'] = False
        dump(data, f)
    ENDFUNC()

def setLevel():
    PATH = ProfilePath()
    tXp = 0
    xp = [0,1071, 1288, 1655, 2176, 2855, 3696, 4704, 5883, 7237, 8770, 10486, 12390, 14486, 16778, 19270, 21966, 24871, 27989, 31324, 34880, 38661, 42672, 46917, 51400, 56125, 91145, 98978, 107193, 115797, 124795, 134195, 144002, 154222, 164863, 175930, 187430, 199368, 211752, 224587, 237880, 251637, 265865, 280569, 295756, 311433, 327605, 344279, 361461, 379158, 397375, 416120, 435398, 455215, 475579, 496495, 517970, 540009, 562620, 585808, 609580, 844923, 878201, 912282, 947176, 982890, 1019433, 1056813, 1095038, 1134118, 1174060, 1214873, 1256565, 1299144, 1342620, 1387000, 1432293, 1478507, 1525650, 1573732, 1622760, 1672743, 1723689, 1775606, 1828504, 1882390, 1937273, 1993161, 2050062, 2107986, 2166940, 3339899, 3431459, 3524603, 3619342, 3715690, 3813659, 3913262, 4014512, 4117420]
    SetConsoleTitle('SAS4Tool - Set level')
    mainTitle()
    try:
        level = int(input('Enter level\n\n> '))
    except ValueError:
        mainTitle()
        print('Invalid input!')
        sleep(1)
        return setLevel()
    if level > 100 or level < 1:
        mainTitle()
        print('Invalid level!')
        sleep(1)
        return setLevel()
    for i in range(level):
        tXp += xp[i]
    mainTitle()
    print('Loading...')
    decode_pf()
    with open('config.json', 'r') as f:
        pf = load(f)
        profile = pf['defaultProfile']
    with open(f'{PATH}\\Profile_unpacked.json', 'r+') as f:
        data = load(f)
        f.seek(0)
        f.truncate()
        data['Inventory'][profile]['Skills']['PlayerLevel'] = level
        data['Inventory'][profile]['Skills']['PlayerTotalXp'] = tXp
        dump(data, f)
    ENDFUNC()

def setBlackStronboxes():
    PATH = ProfilePath()
    l = []
    SetConsoleTitle('SAS4Tool - Set black Stronboxes')
    mainTitle()
    try:
        amount = int(input('Enter strongboxes amount\n\n> '))
    except ValueError:
        mainTitle()
        print('Invalid input!')
        sleep(1)
        return setBlackStronboxes()
    for _ in range(0, amount): l.append(random.randint(99999999, 1000000000))
    mainTitle()
    print('Loading...')
    decode_pf()
    with open('config.json', 'r') as f:
        pf = load(f)
        profile = pf['defaultProfile']
    with open(f'{PATH}\\Profile_unpacked.json', 'r+') as f:
        data = load(f)
        f.seek(0)
        f.truncate()
        data['Inventory'][profile]['Skills']['AvailableBlackStrongboxes'] = l
        dump(data, f)
    ENDFUNC()

def setRandomStrongboxes():
    # SetConsoleTitle('SAS4Tool - Add random strongboxes')
    # decode_pf()
    # with open('config.json', 'r') as f:
    #     pf = load(f)
    #     profile = pf['defaultProfile']
    # with open(f'{PATH}\\Profile_unpacked.json', 'r') as f:
    #     data = load(f)
    # profileLevel = data['Inventory'][profile]['Skills']['PlayerLevel']
    # if profileLevel < 15: gunVersion = 0
    # if profileLevel >= 15: gunVersion = 1
    pass

def addBlackKeys():
    PATH = ProfilePath()
    SetConsoleTitle('SAS4Tool - Add black keys')
    mainTitle()
    try:
        amount = int(input('Enter black keys amount\n\n> '))
    except ValueError:
        mainTitle()
        print('Invalid input!')
        sleep(1)
        return addBlackKeys()
    mainTitle()
    print('Loading...')
    decode_pf()
    with open('config.json', 'r') as f:
        pf = load(f)
        profile = pf['defaultProfile']
    with open(f'{PATH}\\Profile_unpacked.json', 'r+') as f:
        data = load(f)
        f.seek(0)
        f.truncate()
        data['Inventory'][profile]['Skills']['AvailableBlackKeys'] = amount
        dump(data, f)
    ENDFUNC()

def addAugmentCores():
    PATH = ProfilePath()
    SetConsoleTitle('SAS4Tool - Add augment cores')
    mainTitle()
    try:
        amount = int(input('Enter augment cores amount\n\n> '))
    except ValueError:
        mainTitle()
        print('Invalid input!')
        sleep(1)
        return addAugmentCores()
    mainTitle()
    print('Loading...')
    decode_pf()
    with open('config.json', 'r') as f:
        pf = load(f)
        profile = pf['defaultProfile']
    with open(f'{PATH}\\Profile_unpacked.json', 'r+') as f:
        data = load(f)
        f.seek(0)
        f.truncate()
        data['Inventory'][profile]['Skills']['AvailableEliteAugmentCores'] = amount
        dump(data, f)
    ENDFUNC()

def addTurrets():
    PATH = ProfilePath()
    SetConsoleTitle('SAS4Tool - Add turrets')
    mainTitle()
    turretData = loads(IDs)
    for i in range(len(turretData['TurretsIDs']['Normal'])):
        print(f'[{ascii_letters[26+i]}] - {turretData["TurretsIDs"]["Normal"][i]["Name"]}')
    while True:
        if kbhit():
            key = getch()
            if key == b'a':
                turretIndex = 0
                break
            if key == b'b':
                turretIndex = 1
                break
            if key == b'c':
                turretIndex = 2
                break
            if key == b'd':
                turretIndex = 3
                break
            if key == b'e':
                turretIndex = 4
                break
            if key == b'f':
                turretIndex = 5
                break
            if key == b'g':
                turretIndex = 6
                break
    mainTitle()
    try:
        amount = int(input('Enter turrets amount\n\n> '))
    except ValueError:
        mainTitle()
        print('Invalid input!')
        sleep(1)
        return addTurrets()
    mainTitle()
    print('Loading...')
    decode_pf()
    with open('config.json', 'r') as f:
        pf = load(f)
        profile = pf['defaultProfile']
    with open(f'{PATH}\\Profile_unpacked.json', 'r+') as f:
        data = load(f)
        f.seek(0)
        f.truncate()
        if data['Inventory'][profile]['Skills']['PlayerLevel'] < 30:
            turretVersion = 'Normal'
        if data['Inventory'][profile]['Skills']['PlayerLevel'] >= 30:
            turretVersion = 'Red'
        turretID = turretData['TurretsIDs'][turretVersion][turretIndex]['ID']
        try:
            for i in data['Inventory'][profile]['Turrets']:
                if i['TurretId'] == turretID:
                    turretDataIndex = data['Inventory'][profile]['Turrets'].index(i)
                data['Inventory'][profile]['Turrets'][turretDataIndex]['TurretCount'] = amount
                dump(data, f)
        except NameError:
            data['Inventory'][profile]['Turrets'].append({'TurretId': turretID, 'TurretCount': amount})
            dump(data, f)
    ENDFUNC()

def addGrenades():
    PATH = ProfilePath()
    SetConsoleTitle('SAS4Tool - Set grenades')
    mainTitle()
    print('[A] - Frag Grenade\n[B] - Cryo Grenade\n[C] - Back')
    while True:
        if kbhit():
            key = getch()
            if key == b'a':
                grenade_id = 'grenades_frag'
                break
            if key == b'b':
                grenade_id = 'grenades_cryo'
                break
    mainTitle()
    try:
        amount = int(input('Enter grenades amount\n\n> '))
    except ValueError:
        mainTitle()
        print('Invalid input!')
        sleep(1)
        return addGrenades()
    mainTitle()
    print('Loading...')
    decode_pf()
    with open('config.json', 'r') as f:
        pf = load(f)
        profile = pf['defaultProfile']
    with open(f'{PATH}\\Profile_unpacked.json', 'r+') as f:
        data = load(f)
        f.seek(0)
        f.truncate()
        data['Inventory'][profile]['Ammo'][grenade_id] = amount
        dump(data, f)
    ENDFUNC()

def setSupportItems():
    SetConsoleTitle('SAS4Tool - Set support items')
    mainTitle()
    print('[A] - Add turrets\n[B] - Add grenades\n[C] - Back')
    while True:
        if kbhit():
            key = getch()
            if key == b'a':
                addTurrets()
                break
            if key == b'b':
                addGrenades()
                break
            if key == b'c':
                break
    pass

def addMultiplayerStats():
    PATH = ProfilePath()
    SetConsoleTitle('SAS4Tool - Set multiplayer stats')
    mainTitle()
    print('[A] - MP Kills\n[B] - MP Deaths\n[C] - MP Wins\n[D] - MP Losses\n[E] - Back')
    while True:
        if kbhit():
            key = getch()
            if key == b'a':
                stat = 'multi_kills'
                break
            if key == b'b':
                stat = 'multi_deaths'
                break
            if key == b'c':
                stat = 'multi_games_won'
                break
            if key == b'd':
                stat = 'multi_games_lost'
                break
            if key == b'e':
                return 0
    mainTitle()
    try:
        amount = int(input('Enter stat value\n\n> '))
    except ValueError:
        mainTitle()
        print('Invalid input!')
        sleep(1)
        return addMultiplayerStats()
    mainTitle()
    print('Loading...')
    decode_pf()
    with open('config.json', 'r') as f:
        pf = load(f)
        profile = pf['defaultProfile']
    with open(f'{PATH}\\Profile_unpacked.json', 'r+') as f:
        data = load(f)
        f.seek(0)
        f.truncate()
        for i in data['Inventory'][profile]['StatsData']:
            if i['key'] == stat:
                indx = data['Inventory'][profile]['StatsData'].index(i)
        try:
            data['Inventory'][profile]['StatsData'][indx]['val'] = amount
        except KeyError:
            data['Inventory'][profile]['StatsData'][indx]['val'].append({'key': stat, 'val': amount})
        dump(data, f)
    ENDFUNC()
