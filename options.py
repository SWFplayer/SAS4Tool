import encodingDecoding as d
import time, os, random
import main
import json
import createFile as c

NUMS = '123456789'

# TURRETS

TURRETSNM = [54, 56, 58, 62, 63, 60, 55]
TURRETSRD = [133, 134, 135, 136, 137, 138, 139]

def factionGuild():
    main.title()
    factionCode = input('Please, move your "Profile.save" to the current folder.\n\nType your faction code (Ex: XKLFHL)\n\n>')
    main.title()
    factionGuild = input('Type your faction guild (Ex: SPARTANS)\n\n>')
    main.title()
    print("Loading, please wait...")
    d.decodeProfileSave()
    with open('Profile_unpacked.json', 'r+') as f:
        data = json.load(f)
        f.seek( 0 )
        f.truncate()
        data['CurrentFactionWarMatch'] = factionCode.upper()
        data['CurrentFactionWarFaction'] = factionGuild.upper()
        json.dump(data, f)
    if os.path.exists('Profile.save'):
        os.remove('Profile.save')
    d.encodeProfileSave()
    os.remove('Profile_unpacked.json')
    main.title()
    print('Profile.save has been successfuly updated.')
    time.sleep(3)
    return main.mainMenu()

def factionCredits():
    try:
        main.title()
        factionWarCurrency = int(input('Set your ammount for faction war credits\n\n>'))
        main.title()
        planetZCurrency = int(input('Set your planet Zeta credits\n\n>'))
        main.title()
        planetECurrency = int(input('Set your planet Epsilon credits\n\n>'))
        main.title()
        planetSCurrency = int(input('Set your planet Sigma credits\n\n>'))
        main.title()
        planetXCurrency = int(input('Set your planet Xi credits\n\n>'))
        main.title()
        planetOCurrency = int(input('Set your planet Omicron credits\n\n>'))
    except ValueError:
        main.title()
        print("Please, enter a valid number.")
        time.sleep(3)
        return factionCredits()
    main.title()
    print('Loading, please wait...')
    d.decodeProfileSave()
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
    d.encodeProfileSave()
    os.remove('Profile_unpacked.json')
    main.title()
    print('Profile.save has been successfuly updated.')
    time.sleep(3)
    return main.mainMenu()

def reviveTokens():
    main.title()
    try:
        tokens = int(input('Set your revive tokens ammount\n\n>'))
    except ValueError:
        main.title()
        print("Please, enter a valid number.")
        time.sleep(3)
        return reviveTokens()
    d.decodeProfileSave()
    with open('Profile_unpacked.json', 'r+') as f:
        data = json.load(f)
        f.seek( 0 )
        f.truncate()
        data['Global']['ReviveTokens'] = tokens
        json.dump(data, f)
    if os.path.exists('Profile.save'):
        os.remove('Profile.save')
    d.encodeProfileSave()
    os.remove('Profile_unpacked.json')
    main.title()
    print('Profile.save has been successfuly updated.')
    time.sleep(3)
    return main.mainMenu()

def blackKeys():
    main.title()
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
        main.title()
        print('This profile does not exist.')
        time.sleep(3)
        return blackKeys()
    main.title()
    try:
        blackkeys = int(input('Set your black keys ammount\n\n>'))
    except ValueError:
        main.title()
        print("Please, enter a valid number.")
        time.sleep(3)
        return blackKeys()
    main.title()
    print('Loading, please wait...')
    d.decodeProfileSave()
    with open('Profile_unpacked.json', 'r+') as f:
        data = json.load(f)
        f.seek( 0 )
        f.truncate()
        data['Inventory'][f'{profile}']['Skills']['AvailableBlackKeys'] = blackkeys
        json.dump( data, f )
    if os.path.exists('Profile.save'):
        os.remove('Profile.save')
    d.encodeProfileSave()
    os.remove('Profile_unpacked.json')
    main.title()
    print('Profile.save has been successfuly updated.')
    time.sleep(3)
    return main.mainMenu()

def blackBox():
    main.title()
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
        main.title()
        print('This profile does not exist.')
        time.sleep(3)
        return blackBox()
    main.title()
    try:
        print('Large values will slow down the function.\n\n')
        blackbox = int(input('Set your black strongboxes ammount\n\n>'))
    except ValueError:
        main.title()
        print("Please, enter a valid number.")
        time.sleep(3)
        return blackBox()
    main.title()
    print("Loading, please wait...")
    d.decodeProfileSave()
    l = []
    for x in range(0, blackbox): # Ammount of black boxes to generate
        genBox = ''
        for x in range(0, 10):
            chars = random.choice(NUMS)
            genBox = genBox + chars
        l.append(int(genBox))
    with open('Profile_unpacked.json', 'r+') as f:
        data = json.load(f)
        f.seek( 0 )
        f.truncate()
        data['Inventory'][f'{profile}']['Skills']['AvailableBlackStrongboxes'] = l
        json.dump(data, f)
    if os.path.exists('Profile.save'):
        os.remove('Profile.save')
    d.encodeProfileSave()
    os.remove('Profile_unpacked.json')
    main.title()
    print('Profile.save has been successfuly updated.')
    time.sleep(3)
    return main.mainMenu()

def augCores():
    main.title()
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
        main.title()
        print('This profile does not exist.')
        time.sleep(3)
        return augCores()
    main.title()
    try:
        augcores = int(input('Set your augment cores ammount\n\n>'))
    except ValueError:
        main.title()
        print("Please, enter a valid number.")
        time.sleep(3)
        return augCores()
    main.title()
    print('Loading, please wait...')
    d.decodeProfileSave()
    with open('Profile_unpacked.json', 'r+') as f:
        data = json.load(f)
        f.seek( 0 )
        f.truncate()
        data['Inventory'][f'{profile}']['Skills']['AvailableEliteAugmentCores'] = augcores
        json.dump( data, f )
    if os.path.exists('Profile.save'):
        os.remove('Profile.save')
    d.encodeProfileSave()
    os.remove('Profile_unpacked.json')
    main.title()
    print('Profile.save has been successfuly updated.')
    time.sleep(3)
    return main.mainMenu()

def sasCash():
    main.title()
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
        main.title()
        print('This profile does not exist.')
        time.sleep(3)
        return sasCash()
    main.title()
    try:
        money = int(input('Set your SAS cash ammount\n\n>'))
    except ValueError:
        main.title()
        print("Please, enter a valid number.")
        time.sleep(3)
        return main.o2()
    main.title()
    print('Loading, please wait...')
    d.decodeProfileSave()
    with open('Profile_unpacked.json', 'r+') as f:
        data = json.load(f)
        f.seek( 0 )
        f.truncate()
        data['Inventory'][f'{profile}']['Money'] = money
        json.dump( data, f )
    if os.path.exists('Profile.save'):
        os.remove('Profile.save')
    d.encodeProfileSave()
    os.remove('Profile_unpacked.json')
    main.title()
    print('Profile.save has been successfuly updated.')
    time.sleep(3)
    return main.mainMenu()

def removeAds():
    main.title()
    ads = input('Do you want to remove ads?\n\n[1] Yes\n[2] No\n\n>')
    if ads == '1':
        ads = True
    elif ads == '2':
        ads = False
    else:
        main.title()
        print('Invalid option.')
        time.sleep(3)
        return removeAds()
    main.title()
    print('Loading, please wait...')
    d.decodeProfileSave()
    with open('Profile_unpacked.json', 'r+') as f:
        data = json.load(f)
        f.seek( 0 )
        f.truncate()
        data['Global']['ForceRemoveAds'] = ads
        json.dump( data, f )
    if os.path.exists('Profile.save'):
        os.remove('Profile.save')
    d.encodeProfileSave()
    os.remove('Profile_unpacked.json')
    main.title()
    print('Profile.save has been successfuly updated.')
    time.sleep(3)
    return main.mainMenu()

def premiumTickets():
    main.title()
    try:
        tickets = int(input('Set your premium tickets ammount\n\n>'))
    except ValueError:
        main.title()
        print("Please, enter a valid number.")
        time.sleep(3)
        return premiumTickets()
    main.title()
    print('Loading, please wait...')
    d.decodeProfileSave()
    with open('Profile_unpacked.json', 'r+') as f:
        data = json.load(f)
        f.seek( 0 )
        f.truncate()
        data['Global']['AvailablePremiumTickets'] = tickets
        json.dump( data, f )
    if os.path.exists('Profile.save'):
        os.remove('Profile.save')
    d.encodeProfileSave()
    os.remove('Profile_unpacked.json')
    main.title()
    print('Profile.save has been successfuly updated.')
    time.sleep(3)
    return main.mainMenu()

def premProfile():
    main.title()
    premprofile = input('Do you want to unlock 2 extra profiles?\n\n[1] Yes\n[2] No\n\n>')
    if premprofile == '1':
        premprofile = True
    elif premprofile == '2':
        premprofile = False
    else:
        main.title()
        print('Invalid option.')
        time.sleep(3)
        return premProfile()
    main.title()
    print('Loading, please wait...')
    d.decodeProfileSave()
    with open('Profile_unpacked.json', 'r+') as f:
        data = json.load(f)
        f.seek( 0 )
        f.truncate()
        data['PurchasedIAP']['PurchasedIAPArray'][0]['Value'] = premprofile
        data['PurchasedIAP']['PurchasedIAPArray'][1]['Value'] = premprofile
        json.dump( data, f )
    if os.path.exists('Profile.save'):
        os.remove('Profile.save')
    d.encodeProfileSave()
    os.remove('Profile_unpacked.json')
    main.title()
    print('Profile.save has been successfuly updated.')
    time.sleep(3)
    return main.mainMenu()


def premGuns():
    VAL1 = 1
    main.title()
    gun = input('''
[1] Ahab                            [17] HIKS S4000
[2] Banshee                         [18] Planet Stormer Ltd. Edition
[3] Bayonet                         [19] RIA 15 SE
[4] Calamity                        [20] RIA 75
[5] CM 000 Kelvin                   [21] RIA 8A
[6] CM 352 Quasar                   [22] Ricochet
[7] CM 369 Starfury                 [23] Ronson 5X5
[8] CM 467                          [24] Ronson WPX Incinerator
[9] CM 505 Alpha Ltd. edition       [25] Supermarine Alpha Ltd. Edition
[10] CM Laser Drill                 [26] T-189 MGL
[11] CM Proton Arc                  [27] Torment
[12] Contagion                      [28] Vitriol
[13] Donderbus                      [29] Zerfallen
[14] Handkanone                     [30] Unlock All
[15] HIKS 888 CAW
[16] HIKS A10\n\n>''')
    if gun == '1':
        gun = 2
    elif gun == '2':
        gun = 3
    elif gun == '3':
        gun = 4
    elif gun == '4':
        gun = 5
    elif gun == '5':
        gun = 6
    elif gun == '6':
        gun = 7
    elif gun == '7':
        gun = 8
    elif gun == '8':
        gun = 9
    elif gun == '9':
        gun = 10
    elif gun == '10':
        gun = 11
    elif gun == '11':
        gun = 12
    elif gun == '12':
        gun = 13
    elif gun == '13':
        gun = 14
    elif gun == '14':
        gun = 15
    elif gun == '15':
        gun = 16
    elif gun == '16':
        gun = 17
    elif gun == '17':
        gun = 18
    elif gun == '18':
        gun = 19
    elif gun == '19':
        gun = 20
    elif gun == '20':
        gun = 21
    elif gun == '21':
        gun = 22
    elif gun == '22':
        gun = 23
    elif gun == '23':
        gun = 24
    elif gun == '24':
        gun = 25
    elif gun == '25':
        gun = 26
    elif gun == '26':
        gun = 27
    elif gun == '27':
        gun = 28
    elif gun == '28':
        gun = 29
    elif gun == '29':
        gun = 30
    elif gun == '30':
        main.title()
        print('Loading, please wait...')
        d.decodeProfileSave()
        with open('Profile_unpacked.json', 'r+') as f:
            data = json.load(f)
            f.seek( 0 )
            f.truncate()
            for i in range(28):
                VAL1 += 1
                data['PurchasedIAP']['PurchasedIAPArray'][VAL1]['Value'] = True
            json.dump( data, f )
        if os.path.exists('Profile.save'):
            os.remove('Profile.save')
        d.encodeProfileSave()
        os.remove('Profile_unpacked.json')
        main.title()
        print('Profile.save has been successfuly updated.')
        time.sleep(3)
        return main.mainMenu()
    else:
        main.title()
        print('Invalid option.')
        time.sleep(3)
        return premGuns()
    main.title()
    print('Loading, please wait...')
    d.decodeProfileSave()
    with open('Profile_unpacked.json', 'r+') as f:
        data = json.load(f)
        f.seek( 0 )
        f.truncate()
        data['PurchasedIAP']['PurchasedIAPArray'][gun]['Value'] = True
        json.dump( data, f )
    if os.path.exists('Profile.save'):
        os.remove('Profile.save')
    d.encodeProfileSave()
    os.remove('Profile_unpacked.json')
    main.title()
    print('Profile.save has been successfuly updated.')
    time.sleep(3)
    return main.mainMenu()

def weaponConfig(weaponType, weaponCategory, weaponVersion, profile):
    main.title()
    with open('IDs.json', 'r') as idf:
        IDs = json.load(idf)
    for i in range(len(IDs['weaponIDs'][f'{weaponType}'][f'{weaponCategory}'])):
        prnWeap = f'[{i+1}] ' + f'{IDs["weaponIDs"][f"{weaponType}"][f"{weaponCategory}"][i]["Name"]}'
        print(prnWeap)
    weapon = input('\n>')
    strongbox = '''
    {
        "ID": 0,
        "EquipVersion": 0,
        "Grade": 0,
        "EquippedSlot": -1,
        "AugmentSlots": 0,
        "InventoryIndex": 0,
        "Seen": false,
        "BonusStatsLevel": 0,
        "Equipped": false,
        "ContainsKey": false,
        "ContainsAugmentCore": false,
        "BlackStrongboxSeed": 0,
        "UseDefaultOpenLogic": true
    }'''
    main.title()
    try:
        grade = int(input('Set your weapon grade (0-12)\n\n>'))
        if grade > 12:
            main.title()
            print('Please enter a valid value.')
            time.sleep(3)
            return weaponConfig(weaponType, weaponCategory, weaponVersion, profile)
    except ValueError:
        main.title()
        print('Please enter a valid number.')
        time.sleep(3)
        return weaponConfig(weaponType, weaponCategory, weaponVersion, profile)
    main.title()
    try:
        augmentSlots = int(input('Set your weapon augment slots (0-4)\n\n>'))
        if augmentSlots > 4:
            main.title()
            print('Please enter a valid value.')
            time.sleep(3)
            return weaponConfig(weaponType, weaponCategory, weaponVersion, profile)
    except ValueError:
        main.title()
        print('Please enter a valid number.')
        time.sleep(3)
        return weaponConfig(weaponType, weaponCategory, weaponVersion, profile)
    main.title()
    try:
        bonusGrade = int(input('Set your weapon bonus stats (0-10)\n\n>'))
        if bonusGrade > 10:
            main.title()
            print('Please enter a valid value.')
            time.sleep(3)
            return weaponConfig(weaponType, weaponCategory, weaponVersion, profile)
    except ValueError:
        main.title()
        print('Please enter a valid number.')
        time.sleep(3)
        return weaponConfig(weaponType, weaponCategory, weaponVersion, profile)
    main.title()
    print('Loading, please wait...')
    d.decodeProfileSave()
    with open('Profile_unpacked.json', 'r+') as f:
        data = json.load(f)
        strongBox = json.loads(strongbox)
        f.seek( 0 )
        f.truncate()
        strongBox['ID'] = IDs['weaponIDs'][f'{weaponType}'][f'{weaponCategory}'][int(weapon)-1]['ID']
        strongBox['EquipVersion'] = weaponVersion
        strongBox['Grade'] = int(grade)
        strongBox['AugmentSlots'] = int(augmentSlots)
        strongBox['BonusStatsLevel'] = int(bonusGrade)
        strongBox['InventoryIndex'] = IDs['weaponIDs'][f'{weaponType}']['Extra'][0]['Type']
        data['Inventory'][f'{profile}']['Strongboxes']['Claimed'].append(int(0))
        data['Inventory'][f'{profile}']['Strongboxes']['Claimed'].append(strongBox)
        data['Inventory'][f'{profile}']['Strongboxes']['Claimed'].append(int(8))
        data['Inventory'][f'{profile}']['Strongboxes']['Claimed'].append(int(0))
        json.dump( data, f )
    if os.path.exists('Profile.save'):
        os.remove('Profile.save')
    if os.path.exists('IDs.json'):
        os.remove('IDs.json')
    d.encodeProfileSave()
    os.remove('Profile_unpacked.json')
    main.title()
    print('Profile.save has been successfuly updated.')
    time.sleep(3)
    return main.mainMenu()

def weaponCat(weaponType, profile):
    main.title()
    c.createFile()
    with open('IDs.json', 'r') as f:
        data = json.load(f)
        try:
            data['weaponIDs'][f'{weaponType}']['Factions']
        except:
            main.title()
            weaponCategory = input('[1] Normal\n[2] Red\n[3] Black\n\n>')
            if weaponCategory == '1':
                weaponCategory = 'Normal'
                weaponVersion = 0
                weaponConfig(weaponType, weaponCategory, weaponVersion, profile)
            elif weaponCategory == '2':
                weaponCategory = 'Red'
                weaponVersion = 1
                weaponConfig(weaponType, weaponCategory, weaponVersion, profile)
            elif weaponCategory == '3':
                weaponCategory = 'Black'
                weaponVersion = 2
                weaponConfig(weaponType, weaponCategory, weaponVersion, profile)
            else:
                main.title()
                print('Invalid option.')
                time.sleep(3)
                return weaponCat(weaponType)
    main.title()
    weaponCategory = input('[1] Normal\n[2] Red\n[3] Black\n[4] Factions\n\n>')
    if weaponCategory == '1':
        weaponCategory = 'Normal'
        weaponVersion = 0
        weaponConfig(weaponType, weaponCategory, weaponVersion, profile)
    elif weaponCategory == '2':
        weaponCategory = 'Red'
        weaponVersion = 1
        weaponConfig(weaponType, weaponCategory, weaponVersion, profile)
    elif weaponCategory == '3':
        weaponCategory = 'Black'
        weaponVersion = 2
        weaponConfig(weaponType, weaponCategory, weaponVersion, profile)
    elif weaponCategory == '4':
        weaponCategory = 'Factions'
        weaponVersion = 1
        weaponConfig(weaponType, weaponCategory, weaponVersion, profile)
    else:
        main.title()
        print('Invalid option.')
        time.sleep(3)
        return weaponCat()

def weapons():
    main.title()
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
        main.title()
        print('This profile does not exist.')
        time.sleep(3)
        return weapons()
    main.title()
    weaponType = input('[1] Pistols\n[2] SMG\n[3] Assault Rifle\n[4] Shotgun\n[5] Sniper\n[6] Rocket Launcher\n[7] Flame Thrower\n[8] LMG\n[9] Disk Thrower\n[10] Laser\n\n>')
    if weaponType == '1':
        weaponType = 'Pistol'
        weaponCat(weaponType, profile)
    elif weaponType == '2':
        weaponType = 'SMG'
        weaponCat(weaponType, profile)
    elif weaponType == '3':
        weaponType = 'Assault Rifle'
        weaponCat(weaponType, profile)
    elif weaponType == '4':
        weaponType = 'Shotgun'
        weaponCat(weaponType, profile)
    elif weaponType == '5':
        weaponType = 'Sniper'
        weaponCat(weaponType, profile)
    elif weaponType == '6':
        weaponType = 'Rocket Launcher'
        weaponCat(weaponType, profile)
    elif weaponType == '7':
        weaponType = 'Flame Thrower'
        weaponCat(weaponType, profile)
    elif weaponType == '8':
        weaponType = 'LMG'
        weaponCat(weaponType, profile)
    elif weaponType == '9':
        weaponType = 'Disk Thrower'
        weaponCat(weaponType, profile)
    elif weaponType == '10':
        weaponType = 'Laser'
        weaponCat(weaponType, profile)

def equipConfig(equipType, equipCategory, equipVersion, profile):
    main.title()
    with open('IDs.json', 'r') as idf:
        IDs = json.load(idf)
    for i in range(len(IDs['equipmentIDs'][f'{equipType}'][f'{equipCategory}'])):
        prnEquip = f'[{i+1}] ' + f'{IDs["equipmentIDs"][f"{equipType}"][f"{equipCategory}"][i]["Name"]}'
        print(prnEquip)
    equip = input('\n>')
    strongbox2 = '''
    {
        "ID": 0,
        "EquipVersion": 0,
        "Grade": 0,
        "EquippedSlot": -1,
        "AugmentSlots": 1,
        "InventoryIndex": 0,
        "Seen": false,
        "BonusStatsLevel": 0,
        "Equipped": false,
        "ContainsKey": false,
        "ContainsAugmentCore": false,
        "BlackStrongboxSeed": 0,
        "UseDefaultOpenLogic": true
    }'''
    main.title()
    try:
        grade = int(input('Set your equipment grade (0-12)\n\n>'))
        if grade > 12:
            main.title()
            print('Please enter a valid value.')
            time.sleep(3)
            return equipConfig(equipType, equipCategory, equipVersion, profile)
    except ValueError:
        main.title()
        print('Please enter a valid number.')
        time.sleep(3)
        return equipConfig(equipType, equipCategory, equipVersion, profile)
    main.title()
    try:
        augmentSlots = int(input('Set your equipment augment slots (0-3)\n\n>'))
        if augmentSlots > 3:
            main.title()
            print('Please enter a valid value.')
            time.sleep(3)
            return equipConfig(equipType, equipCategory, equipVersion, profile)
    except ValueError:
        main.title()
        print('Please enter a valid number.')
        time.sleep(3)
        return equipConfig(equipType, equipCategory, equipVersion, profile)
    main.title()
    try:
        bonusGrade = int(input('Set your equipment bonus stats (0-10)\n\n>'))
        if bonusGrade > 10:
            main.title()
            print('Please enter a valid value.')
            time.sleep(3)
            return equipConfig(equipType, equipCategory, equipVersion, profile)
    except ValueError:
        main.title()
        print('Please enter a valid number.')
        time.sleep(3)
        return equipConfig(equipType, equipCategory, equipVersion, profile)
    main.title()
    print('Loading, please wait...')
    d.decodeProfileSave()
    with open('Profile_unpacked.json', 'r+') as f:
        data = json.load(f)
        strongBox2 = json.loads(strongbox2)
        f.seek( 0 )
        f.truncate()
        strongBox2['ID'] = IDs['equipmentIDs'][f'{equipType}'][f'{equipCategory}'][int(equip)-1]['ID']
        strongBox2['EquipVersion'] = equipVersion
        strongBox2['Grade'] = int(grade)
        strongBox2['AugmentSlots'] = int(augmentSlots)
        strongBox2['BonusStatsLevel'] = int(bonusGrade)
        strongBox2['InventoryIndex'] = IDs['equipmentIDs'][f'{equipType}']['Extra'][0]['Type']
        data['Inventory'][f'{profile}']['Strongboxes']['Claimed'].append(int(1))
        data['Inventory'][f'{profile}']['Strongboxes']['Claimed'].append(strongBox2)
        data['Inventory'][f'{profile}']['Strongboxes']['Claimed'].append(int(8))
        data['Inventory'][f'{profile}']['Strongboxes']['Claimed'].append(int(0))
        json.dump( data, f )
    if os.path.exists('Profile.save'):
        os.remove('Profile.save')
    if os.path.exists('IDs.json'):
        os.remove('IDs.json')
    d.encodeProfileSave()
    os.remove('Profile_unpacked.json')
    main.title()
    print('Profile.save has been successfuly updated.')
    time.sleep(3)
    return main.mainMenu()

def equipCat(equipType, profile):
    main.title()
    c.createFile()
    with open('IDs.json', 'r') as f:
        data = json.load(f)
        try:
            data['equipmentIDs'][f'{equipType}']['Factions']
        except:
            main.title()
            equipCategory = input('[1] Normal\n[2] Red\n[3] Black\n\n>')
            if equipCategory == '1':
                equipCategory = 'Normal'
                equipVersion = 0
                equipConfig(equipType, equipCategory, equipVersion, profile)
            elif equipCategory == '2':
                equipCategory = 'Red'
                equipVersion = 1
                equipConfig(equipType, equipCategory, equipVersion, profile)
            elif equipCategory == '3':
                equipCategory = 'Black'
                equipVersion = 2
                equipConfig(equipType, equipCategory, equipVersion, profile)
            else:
                main.title()
                print('Invalid option.')
                time.sleep(3)
                return equipCat(equipType)
    main.title()
    equipCategory = input('[1] Normal\n[2] Red\n[3] Black\n[4] Factions\n\n>')
    if equipCategory == '1':
        equipCategory = 'Normal'
        equipVersion = 0
        equipConfig(equipType, equipCategory, equipVersion, profile)
    elif equipCategory == '2':
        equipCategory = 'Red'
        equipVersion = 1
        equipConfig(equipType, equipCategory, equipVersion, profile)
    elif equipCategory == '3':
        equipCategory = 'Black'
        equipVersion = 2
        equipConfig(equipType, equipCategory, equipVersion, profile)
    elif equipCategory == '4':
        equipCategory = 'Factions'
        equipVersion = 1
        equipConfig(equipType, equipCategory, equipVersion, profile)
    else:
        main.title()
        print('Invalid option.')
        time.sleep(3)
        return equipCat()

def equipment():
    main.title()
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
        main.title()
        print('This profile does not exist.')
        time.sleep(3)
        return equipment()
    main.title()
    equipType = input('[1] Helmet\n[2] Vest\n[3] Gloves\n[4] Pants\n[5] Boots\n\n>')
    if equipType == '1':
        equipType = 'Helmet'
        equipCat(equipType, profile)
    elif equipType == '2':
        equipType = 'Vest'
        equipCat(equipType, profile)
    elif equipType == '3':
        equipType = 'Gloves'
        equipCat(equipType, profile)
    elif equipType == '4':
        equipType = 'Pants'
        equipCat(equipType, profile)
    elif equipType == '5':
        equipType = 'Boots'
        equipCat(equipType, profile)
    else:
        main.title()
        print('Invalid option.')
        time.sleep(3)
        return equipment()

def setSupport():
    main.title()
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
        main.title()
        print('This profile does not exist.')
        time.sleep(3)
        return setSupport()
    main.title()
    sType = input('[1] Grenades\n[2] Turrets\n\n>')
    if sType == '1':
        main.title()
        grenadeType = input('[1] Frag grenades\n[2] Cryo grenades\n\n>')
        if grenadeType == '1':
            main.title()
            try:
                a = int(input('Set your supply ammount\n\n>'))
            except ValueError:
                main.title()
                print('Invalid value')
                time.sleep(3)
                return setSupport()
            main.title()
            print('Loading, please wait...')
            d.decodeProfileSave()
            with open('Profile_unpacked.json', 'r+') as f:
                data = json.load(f)
                f.seek( 0 )
                f.truncate()
                data['Inventory'][f'{profile}']['Ammo']['grenades_frag'] = int(a)
                json.dump( data, f )
            if os.path.exists('Profile.save'):
                os.remove('Profile.save')
            d.encodeProfileSave()
            os.remove('Profile_unpacked.json')
            main.title()
            print('Profile.save has been successfuly updated.')
            time.sleep(3)
            return main.mainMenu()
        elif grenadeType == '2':
            main.title()
            try:
                a = int(input('Set your supply ammount\n\n>'))
            except ValueError:
                main.title()
                print('Invalid value')
                time.sleep(3)
                return setSupport()
            main.title()
            print('Loading, please wait...')
            d.decodeProfileSave()
            with open('Profile_unpacked.json', 'r+') as f:
                data = json.load(f)
                f.seek( 0 )
                f.truncate()
                data['Inventory'][f'{profile}']['Ammo']['grenades_cryo'] = int(a)
                json.dump( data, f )
            if os.path.exists('Profile.save'):
                os.remove('Profile.save')
            d.encodeProfileSave()
            os.remove('Profile_unpacked.json')
            main.title()
            print('Profile.save has been successfuly updated.')
            time.sleep(3)
            return main.mainMenu()
        else:
            main.title()
            print('Invalid Option.')
            time.sleep(3)
            return setSupport()
    elif sType == '2':
        main.title()
        c.createFile()
        d.decodeProfileSave()
        with open('IDs.json', 'r') as idf:
            IDs = json.load(idf)
        with open('Profile_unpacked.json', 'r+') as f:
            data = json.load(f)
            f.seek(0)
            f.truncate()
            try:
                if data['Inventory'][f'{profile}']['Skills']['PlayerLevel'] < 30:
                    for i in range(len(IDs['TurretsIDs']['Normal'])):
                        print(f'[{i+1}] ' + IDs['TurretsIDs']['Normal'][i]['Name'])
                    tID = int(input('\n>')) - 1
                    turretID = IDs['TurretsIDs']['Normal'][tID]['ID']
                elif data['Inventory'][f'{profile}']['Skills']['PlayerLevel'] > 30:
                    for i in range(len(IDs['TurretsIDs']['Red'])):
                        print(f'[{i+1}] ' + IDs['TurretsIDs']['Red'][i]['Name'])
                    tID = int(input('\n>')) - 1
                    turretID = IDs['TurretsIDs']['Red'][tID]['ID']
                try:
                    main.title()
                    turretAmmount = int(input('Set your turret ammount\n\n>'))
                except ValueError:
                    main.title()
                    print('Invalid value.')
                    time.sleep(3)
                    return setSupport()
                main.title()
                print('Loading, please wait...')
                try:
                    for i in data['Inventory'][f'{profile}']['Turrets']:
                        if i['TurretId'] == turretID:
                            tIndx = data['Inventory'][f'{profile}']['Turrets'].index(i)
                    data['Inventory'][f'{profile}']['Turrets'][tIndx]['TurretCount'] = turretAmmount
                except NameError:
                    data['Inventory'][f'{profile}']['Turrets'].append({'TurretId': turretID, 'TurretCount': turretAmmount})
            except IndexError:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return setSupport()
            json.dump(data, f)
        if os.path.exists('Profile.save'):
            os.remove('Profile.save')
        if os.path.exists('IDs.json'):
            os.remove('IDs.json')
        d.encodeProfileSave()
        os.remove('Profile_unpacked.json')
        main.title()
        print('Profile.save has been successfuly updated.')
        time.sleep(3)
        return main.mainMenu()

    else:
        main.title()
        print('Invalid Option.')
        time.sleep(3)
        return setSupport()

def collection():
    VAL1 = -1
    VAL2 = -1
    main.title()
    status = input('Do you want to get all collections?\n\n[1] Yes, unlock all collections\n[2] No, lock all collections\n\n>')
    if status == '1':
        st = True
    elif status == '2':
        st = False
    main.title()
    print('Loading, please wait...')
    d.decodeProfileSave()
    with open('Profile_unpacked.json', 'r+') as f:
        data = json.load(f)
        f.seek( 0 )
        f.truncate()
        for i in range(255):
            VAL1 += 1
            data['CollectionArrayWeapon'][VAL1]['CollectionUnlocked'] = st
        for i in range(196):
            VAL2 += 1
            data['CollectionArrayArmour'][VAL2]['CollectionUnlocked'] = st
        json.dump( data, f )
    if os.path.exists('Profile.save'):
        os.remove('Profile.save')
    d.encodeProfileSave()
    os.remove('Profile_unpacked.json')
    main.title()
    print('Profile.save has been successfuly updated.')
    time.sleep(3)
    return main.mainMenu()

def mastery():
    main.title()
    profile = input('Please, select your profile. (From left to right.)\n\n[1] Profile 1\n[2] Profile 2\n[3] Profile 3\n[4] Profile 4\n[5] Profile 5\n[6] Profile 6\n\n>')
    if profile == '1':
        profile = 'MasteryProfile0'
    elif profile == '2':
        profile = 'MasteryProfile1'
    elif profile == '3':
        profile = 'MasteryProfile2'
    elif profile == '4':
        profile = 'MasteryProfile3'
    elif profile == '5':
        profile = 'MasteryProfile4'
    elif profile == '6':
        profile = 'MasteryProfile5'
    else:
        main.title()
        print('This profile does not exist.')
        time.sleep(3)
        return mastery()
    lvl = 5
    xp = 540000
    VAL = -1
    main.title()
    mast = input('Do you want to set you mastery skills to max level?\n\n[1] Yes\n[2] No\n\n>')
    if mast == '1':
        main.title()
        print('Loading, please wait...')
        d.decodeProfileSave()
        with open('Profile_unpacked.json', 'r+') as f:
            data = json.load(f)
            f.seek( 0 )
            f.truncate()
            for i in range(27):
                VAL += 1
                data['MasteryProgress'][f'{profile}'][VAL]['MasteryXp'] = xp
                data['MasteryProgress'][f'{profile}'][VAL]['MasteryLvl'] = lvl
            json.dump( data, f )
        if os.path.exists('Profile.save'):
            os.remove('Profile.save')
        d.encodeProfileSave()
        os.remove('Profile_unpacked.json')
        main.title()
        print('Profile.save has been successfuly updated.')
        time.sleep(3)
        return main.mainMenu()
    elif mast == '2':
        return main.mainMenu()

def skillReset():
    main.title()
    profile = input('Please, select your profile. (From left to right.)\n\n[1] Profile 1\n[2] Profile 2\n[3] Profile 3\n[4] Profile 4\n[5] Profile 5\n[6] Profile 6\n\n>')
    if profile == '1':
        profile = 'Profile0'
    elif profile == '2':
        profile = 'Profile1'
    elif profile == '3':
        profile = 'Profile2'
    elif profile == '4':
        profile = 'rofile3'
    elif profile == '5':
        profile = 'Profile4'
    elif profile == '6':
        profile = 'Profile5'
    else:
        main.title()
        print('This profile does not exist.')
        time.sleep(3)
        return skillReset()
    main.title()
    reset = input('Do you want to get a free skill reset?\n\n[1] Yes\n[2] No, go back\n\n>')
    if reset == '1':
        main.title()
        print('Loading, please wait...')
        d.decodeProfileSave()
        with open('Profile_unpacked.json', 'r+') as f:
            data = json.load(f)
            f.seek( 0 )
            f.truncate()
            data['Inventory'][f'{profile}']['FreeSkillsReset'] = False
            json.dump( data, f )
        if os.path.exists('Profile.save'):
            os.remove('Profile.save')
        d.encodeProfileSave()
        os.remove('Profile_unpacked.json')
        main.title()
        print('Profile.save has been successfuly updated.')
        time.sleep(3)
        return main.mainMenu()
    elif reset == '2':
        return main.mainMenu()
    else:
        main.title()
        print('Invalid Option.')
        time.sleep(3)
        return skillReset()

def changeProfileName():
    main.title()
    profile = input('Please, select your profile. (From left to right.)\n\n[1] Profile 1\n[2] Profile 2\n[3] Profile 3\n[4] Profile 4\n[5] Profile 5\n[6] Profile 6\n\n>')
    if profile == '1':
        profile = 'Profile0'
    elif profile == '2':
        profile = 'Profile1'
    elif profile == '3':
        profile = 'Profile2'
    elif profile == '4':
        profile = 'rofile3'
    elif profile == '5':
        profile = 'Profile4'
    elif profile == '6':
        profile = 'Profile5'
    else:
        main.title()
        print('This profile does not exist.')
        time.sleep(3)
        return changeProfileName()
    main.title()
    username = input('Set your new profile username:\n\n>')
    main.title()
    print('Loading, please wait...')
    d.decodeProfileSave()
    with open('Profile_unpacked.json', 'r+') as f:
        data = json.load(f)
        f.seek( 0 )
        f.truncate()
        data['Inventory'][f'{profile}']['Name'] = f'{username}'
        json.dump( data, f )
    if os.path.exists('Profile.save'):
        os.remove('Profile.save')
    d.encodeProfileSave()
    os.remove('Profile_unpacked.json')
    main.title()
    print('Profile.save has been successfuly updated.')
    time.sleep(3)
    return main.mainMenu()

def decodeEnc():
    main.title()
    option1 = input('[1] Encode\n[2] Decode\n\n>')
    if option1 == '1':
        main.title()
        encode = input('Do you want to encode Profile.save?\n\n[1] Yes\n[2] No\n\n>')
        if encode == '1':
            main.title()
            print('Loading, please wait...')
            d.encodeProfileSave()
            main.mainMenu()
            print('Profile.save succesfully encoded.')
            time.sleep(3)
            return decodeEnc()
        elif encode == '2':
            return main.mainMenu()
        else:
            main.title()
            print('Invalid option.')
            time.sleep(3)
            return decodeEnc()
    elif option1 == '2':
        main.title()
        decode = input('Do you want to decode Profile.save and make changes by your own?\n\n[1] Yes\n[2] No\n\n>')
        if decode == '1':
            main.title()
            print('Loading, please wait...')
            d.decodeProfileSave()
            main.mainMenu()
            print('Profile.save succesfully decoded.')
            time.sleep(3)
            return decodeEnc()
        elif decode == '2':
            return main.mainMenu()
        else:
            main.title()
            print('Invalid option.')
            time.sleep(3)
            return decodeEnc()
    else:
        main.title()
        print('Invalid option.')
        time.sleep(3)
        return decodeEnc()

def setLVL():
    totalXp = 0
    xp = [0, 1071, 1288, 1655, 2176, 2855, 3696, 4704, 5883, 7237, 8770, 10486, 12390, 14486, 16778, 19270, 21966, 24871, 27989, 31324, 34880, 38661, 42672, 46917, 51400, 56125, 91145, 98978, 107193, 115797, 124795, 134195, 144002, 154222, 164863, 175930, 187430, 199368, 211752, 224587, 237880, 251637, 265865, 280569, 295756, 311433, 327605, 344279, 361461, 379158, 397375, 416120, 435398, 455215, 475579, 496495, 517970, 540009, 562620, 585808, 609580, 844923, 878201, 912282, 947176, 982890, 1019433, 1056813, 1095038, 1134118, 1174060, 1214873, 1256565, 1299144, 1342620, 1387000, 1432293, 1478507, 1525650, 1573732, 1622760, 1672743, 1723689, 1775606, 1828504, 1882390, 1937273, 1993161, 2050062, 2107986, 2166940, 3339899, 3431459, 3524603, 3619342, 3715690, 3813659, 3913262, 4014512, 4117420]
    main.title()
    profile = input('Please, select your profile. (From left to right.)\n\n[1] Profile 1\n[2] Profile 2\n[3] Profile 3\n[4] Profile 4\n[5] Profile 5\n[6] Profile 6\n\n>')
    if profile == '1':
        profile = 'Profile0'
    elif profile == '2':
        profile = 'Profile1'
    elif profile == '3':
        profile = 'Profile2'
    elif profile == '4':
        profile = 'rofile3'
    elif profile == '5':
        profile = 'Profile4'
    elif profile == '6':
        profile = 'Profile5'
    else:
        main.title()
        print('This profile does not exist.')
        time.sleep(3)
        return setLVL()
    main.title()
    try:
        level = int(input('Set your level: '))
    except ValueError:
        main.title()
        print('Invalid input.')
        time.sleep(3)
        return setLVL()
    main.title()
    if level < 1 or level > 100:
        main.title()
        print('Invalid level.')
        time.sleep(3)
        return setLVL()
    for i in range(level):
        totalXp += xp[i]
    main.title()
    print("Loading, please wait...")
    d.decodeProfileSave()
    with open('Profile_unpacked.json', 'r+') as f:
        data = json.load(f)
        f.seek( 0 )
        f.truncate()
        data['Inventory'][f'{profile}']['Skills']['PlayerLevel'] = level
        data['Inventory'][f'{profile}']['Skills']['PlayerTotalXp'] = totalXp
        json.dump(data, f)
    if os.path.exists('Profile.save'):
        os.remove('Profile.save')
    d.encodeProfileSave()
    os.remove('Profile_unpacked.json')
    main.title()
    print('Profile.save has been successfuly updated.')
    time.sleep(3)
    return main.mainMenu()

def setMulti(key, profile):
    main.title()
    try:
        ammount = int(input('Set your stat value\n\n>'))
    except ValueError:
        main.title()
        print('Invalid value.')
        time.sleep(3)
        return setMulti(key)
    main.title()
    print('Loading, please wait...')
    d.decodeProfileSave()
    with open('Profile_unpacked.json', 'r+') as f:
        data = json.load(f)
        f.seek( 0 )
        f.truncate()
        for i in data['Inventory'][f'{profile}']['StatsData']:
            if i['key'] == key:
                indx = data['Inventory'][f'{profile}']['StatsData'].index(i)
        try:
            data['Inventory'][f'{profile}']['StatsData'][indx]['val'] = ammount
        except:
            data['Inventory'][f'{profile}']['StatsData'].append({'key': key, 'val': ammount})
        json.dump(data, f, indent=4)
    if os.path.exists('Profile.save'):
        os.remove('Profile.save')
    d.encodeProfileSave()
    os.remove('Profile_unpacked.json')
    main.title()
    print('Profile.save has been successfuly updated.')
    time.sleep(3)
    return main.mainMenu()

def setMultiStats():
    main.title()
    profile = input('Please, select your profile. (From left to right.)\n\n[1] Profile 1\n[2] Profile 2\n[3] Profile 3\n[4] Profile 4\n[5] Profile 5\n[6] Profile 6\n\n>')
    if profile == '1':
        profile = 'Profile0'
    elif profile == '2':
        profile = 'Profile1'
    elif profile == '3':
        profile = 'Profile2'
    elif profile == '4':
        profile = 'rofile3'
    elif profile == '5':
        profile = 'Profile4'
    elif profile == '6':
        profile = 'Profile5'
    else:
        main.title()
        print('This profile does not exist.')
        time.sleep(3)
        return setMultiStats()
    main.title()
    stat = input('[1] Multiplayer Kills\n[2] Multiplayer Deaths\n[3] Multiplayer Wins\n[4] Multiplayer Losses\n\n>')
    if stat == '1':
        key = 'multi_kills'
        setMulti(key, profile)
    elif stat == '2':
        key = 'multi_deaths'
        setMulti(key, profile)
    elif stat == '3':
        key = 'multi_games_won'
        setMulti(key, profile)
    elif stat == '4':
        key = 'multi_games_lost'
        setMulti(key, profile)
    else:
        main.title()
        print('This option does not exist.')
        time.sleep(3)
        return setMultiStats()
