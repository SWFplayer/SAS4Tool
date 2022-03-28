import encodingDecoding as d
import time, os, random
import main
import json

NUMS = '123456789'

# WEAPONS

pistolNM = '[1] HVM 001\n[2] CM 202\n[3] RIA 313\n[4] Sabre\n[5] RIA 1010\n[6] Poison Claw\n[7] CM 205\n[8] Trailblazer\n[9] CM 225\n[10] Ronson 45\n[11] Mustang\n[12] GG17 (Faction war exclusive)\n\n>'
pistolRD = '[1] HVM 001\n[2] CM 202\n[3] RIA 313\n[4] Sabre\n[5] RIA 1010\n[6] Poison Claw\n[7] CM 205\n[8] Trailblazer\n[9] CM 225\n[10] Ronson 45\n[11] Mustang\n\n>'
pistolBL = '[1] Poison Claw\n[2] Ronson 45\n[3] Trailblazer\n[4] Mustang\n\n>'

smgNM = '[1] RIA 7\n[2] HVM 002\n[3] Phantom\n[4] CM 330\n[5] RIA T7\n[6] CM 307\n[7] CM 351\n[8] Ronson 50\n[9] Ronson 55\n\n>'
smgRD = '[1] RIA 7\n[2] HVM 002\n[3] Phantom\n[4] CM 330\n[5] RIA T7\n[6] CM 307\n[7] CM 351\n[8] Ronson 50\n[9] Ronson 55\n\n>'
smgBL = '[1] RIA 7\n[2] HVM 002\n[3] Phantom\n[4] CM 330\n[5] RIA T7\n[6] CM 307\n[7] CM 351\n[8] Ronson 50\n[9] Ronson 55\n\n>'

assaultNM = '[1] HVM 005 G-Class\n[2] RIA 20 Para\n[3] RIA 20 DSC\n[4] RIA 20 Striker\n[5] Raptor\n[6] CM 440 Titan\n[7] CM 401 Planet Stormer\n[8] Heartburn\n[9] CM Gigavolt\n[10] Ronson 65-a\n[11] Ronson 70\n[12] CM 451 Starburst\n[13] Hard Thorn\n[14] Mixmaster\n[15] Festungsbrecher (Faction war exclusive)\n[16] Sub-Light COM2\n\n>'
assaultRD = '[1] HVM 005 G-Class\n[2] RIA 20 Para\n[3] RIA 20 DSC\n[4] RIA 20 Striker\n[5] Raptor\n[6] CM 440 Titan\n[7] CM 401 Planet Stormer\n[8] Heartburn\n[9] CM Gigavolt\n[10] Ronson 65-a\n[11] Ronson 70\n[12] CM 451 Starburst\n[13] Hard Thorn\n[14] Mixmaster\n[15] Sub-Light COM2\n\n>'
assaultBL = '[1] HVM 005 G-Class\n[2] RIA 20 Para\n[3] RIA 20 DSC\n[4] RIA 20 Striker\n[5] Raptor\n[6] CM 440 Titan\n[7] CM 401 Planet Stormer\n[8] Heartburn\n[9] CM Gigavolt\n[10] Ronson 65-a\n[11] Ronson 70\n[12] CM 451 Starburst\n[13] Hard Thorn\n[14] Mixmaster\n[15] Sub-Light COM2\n\n>'

shotgunNM = '[1] HVM 004\n[2] RIA 30 Strikeforce\n[3] Stripper\n[4] Shotlite Tempest\n[5] 1887 Shockfield\n[6] Thundershock (Faction war exclusive)\n\n>'
shotgunRD = '[1] HVM 004\n[2] RIA 30 Strikeforce\n[3] Stripper\n[4] Shotlite Tempest\n[5] 1887 Shockfield\n\n>'
shotgunBL = '[1] HVM 004\n[2] RIA 30 Strikeforce\n[3] Stripper\n[4] Shotlite Tempest\n[5] 1887 Shockfield\n\n>'

sniperNM = '[1] RIA 50\n[2] CM 800 Jupiter\n[3] HIKS S300\n[4] Hornet\n\n>'
sniperRD = '[1] RIA 50\n[2] CM 800 Jupiter\n[3] HIKS S300\n[4] Hornet\n\n>'
sniperBL = '[1] RIA 50\n[2] CM 800 Jupiter\n[3] HIKS S300\n[4] Hornet\n\n>'

rocketNM = '[1] HVM MPG\n[2] T-101 Feldhaubitz\n[3] Lone Star\n[4] Depth Charge (Faction war exclusive)\n[5] Gebirgskanone\n[6] T-102 Jagdfaust\n[7] Luftplatzen\n[8] HIKS 3100\n[9] Havoc (Faction war exclusive)\n\n>'
rocketRD = '[1] HVM MPG\n[2] T-101 Feldhaubitz\n[3] Lone Star\n[4] Gebirgskanone\n[5] T-102 Jagdfaust\n[6] Luftplatzen\n[7] HIKS 3100\n\n>'
rocketBL = '[1] HVM MPG\n[2] T-101 Feldhaubitz\n[3] Lone Star\n[4] Gebirgskanone\n[5] T-102 Jagdfaust\n[6] Luftplatzen\n[7] HIKS 3100\n\n>'

flameNM = '[1] Ronson WP Flamethrower\n[2] Phoenix (Faction war exclusive)\n[3] Avalanche (Faction war exclusive)\n\n>'
flameRD = '[1] Ronson WP Flamethrower\n\n>'
flameBL = '[1] Ronson WP Flamethrower\n\n>'

lmgNM = '[1] HVM 008\n[2] Ronson LBM\n[3] RIA 40\n[4] RIA 45 Para\n[5] CM 505\n[6] RIA 530 BabyCOM\n[7] Tombstone\n[8] Proposition\n[9] RIA T40\n[10] Supermarine\n[11] Kraken (Faction war exclusive)\n\n>'
lmgRD = '[1] HVM 008\n[2] Ronson LBM\n[3] RIA 40\n[4] RIA 45 Para\n[5] CM 505\n[6] RIA 530 BabyCOM\n[7] Tombstone\n[8] Proposition\n[9] RIA T40\n[10] Supermarine\n\n>'
lmgBL = '[1] HVM 008\n[2] Ronson LBM\n[3] RIA 40\n[4] RIA 45 Para\n[5] CM 505\n[6] RIA 530 BabyCOM\n[7] Tombstone\n[8] Proposition\n[9] RIA T40\n[10] Supermarine\n\n>'

diskNM = '[1] Shredder\n[2] Exterminator (Faction war exclusive)\n\n>'
diskRD = '[1] Shredder\n\n>'
diskBL = '[1] Shredder\n\n>'

laserNM = '[1] Hotspot\n[2] Krakatoa\n\n>'
laserRD = '[1] Hotspot\n\n>'
laserBL = '[1] Hotspot\n\n>'

# EQUIPMENT

helmetNM = '[1] HVM Kevlar Helmet\n[2] Trooper Helmet\n[3] HVM Carbon Fibre Helmet\n[4] Shotlite Hummingbird H1\n[5] Dynamo Helmet (Faction war exclusive)\n[6] Special Forces Helmet\n[7] R1 Interceptor Helm\n[8] Hardplate Helm\n[9] Medusa Helmet\n[10] Graphene Combat Hood\n[11] Dragonfly Helmet\n[12] Overwatch Helmet (Faction war exclusive)\n[13] Titan IRN HUD\n[14] Mastodon Helm (Faction war exclusive)\n[15] Vulkan Helmet (Faction war exclusive)\n[16] Mako Helmet (Faction war exclusive)\n\n>'
helmetRD = '[1] HVM Kevlar Helmet\n[2] Trooper Helmet\n[3] HVM Carbon Fibre Helmet\n[4] Shotlite Hummingbird H1\n[5] Special Forces Helmet\n[6] R1 Interceptor Helm\n[7] Hardplate Helm\n[8] Medusa Helmet\n[9] Graphene Combat Hood\n[10] Dragonfly Helmet\n[11] Titan IRN HUD\n\n>'
helmetBL = '[1] HVM Kevlar Helmet\n[2] Trooper Helmet\n[3] HVM Carbon Fibre Helmet\n[4] Shotlite Hummingbird H1\n[5] Special Forces Helmet\n[6] R1 Interceptor Helm\n[7] Hardplate Helm\n[8] Medusa Helmet\n[9] Graphene Combat Hood\n[10] Dragonfly Helmet\n[11] Titan IRN HUD\n\n>'

vestNM = '[1] HVM Kevlar Vest\n[2] Trooper Vest\n[3] HVM Carbon Fibre Vest\n[4] Shotlite Hummingbird V1\n[5] Dynamo Chest (Faction war exclusive)\n[6] Special Forces Vest\n[7] R4 Guardian Vest\n[8] Rubicon Power Assist\n[9] Heavy Trooper Vest\n[10] Medusa Vest\n[11] Hardplate Chest\n[12] Dragonfly Vest\n[13] Graphene Body Suit Top\n[14] Titan Teslashock\n[15] Overwatch Chest (Faction war exclusive)\n[16] Mastodon Chest (Faction war exclusive)\n[17] Mako Vest (Faction war exclusive)\n[18] Vulkan Vest (Faction war exclusive)\n\n>'
vestRD = '[1] HVM Kevlar Vest\n[2] Trooper Vest\n[3] HVM Carbon Fibre Vest\n[4] Shotlite Hummingbird V1\n[5] Special Forces Vest\n[6] R4 Guardian Vest\n[7] Rubicon Power Assist\n[8] Heavy Trooper Vest\n[9] Medusa Vest\n[10] Hardplate Chest\n[11] Dragonfly Vest\n[12] Graphene Body Suit Top\n[13] Titan Teslashock\n\n>'
vestBL = '[1] HVM Kevlar Vest\n[2] Trooper Vest\n[3] HVM Carbon Fibre Vest\n[4] Shotlite Hummingbird V1\n[5] Special Forces Vest\n[6] R4 Guardian Vest\n[7] Rubicon Power Assist\n[8] Heavy Trooper Vest\n[9] Medusa Vest\n[10] Hardplate Chest\n[11] Dragonfly Vest\n[12] Graphene Body Suit Top\n[13] Titan Teslashock\n\n>'

glovesNM = '[1] HVM Kevlar Gloves\n[2] Trooper Gloves\n[3] HVM Carbon Fibre Gloves\n[4] Shotlite Hummingbird G1\n[5] Dynamo Gloves (Faction war exclusive)\n[6] Special Forces Gloves\n[7] R6 Flamejuggler Gloves\n[8] Dragonfly Gloves\n[9] Hardplate Gauntlets\n[10] Medusa Gloves\n[11] Graphene Gloves\n[12] Overwatch Gloves (Faction war exclusive)\n[13] Titan IDS 01\n[14] Mastodon Gauntlets (Faction war exclusive)\n[15] Mako Gloves (Faction war exclusive)\n[16] Vulkan Gloves (Faction war exclusive)\n\n>'
glovesRD = '[1] HVM Kevlar Gloves\n[2] Trooper Gloves\n[3] HVM Carbon Fibre Gloves\n[4] Shotlite Hummingbird G1\n[5] Special Forces Gloves\n[6] R6 Flamejuggler Gloves\n[7] Dragonfly Gloves\n[8] Hardplate Gauntlets\n[9] Medusa Gloves\n[10] Graphene Gloves\n[11] Titan IDS 01\n[14]\n\n>'
glovesBL = '[1] HVM Kevlar Gloves\n[2] Trooper Gloves\n[3] HVM Carbon Fibre Gloves\n[4] Shotlite Hummingbird G1\n[5] Special Forces Gloves\n[6] R6 Flamejuggler Gloves\n[7] Dragonfly Gloves\n[8] Hardplate Gauntlets\n[9] Medusa Gloves\n[10] Graphene Gloves\n[11] Titan IDS 01\n[14]\n\n>'

pantsNM = '[1] HVM Kevlar Pants\n[2] Trooper Pants\n[3] HVM Carbon Fibre Pants\n[4] Shotlite Hummingbird P1\n[5] Dynamo Pants (Faction war exclusive)\n[6] Special Forces Pants\n[7] R7 Guardian Pants\n[8] Hardplate Pants\n[9] Medusa Pants\n[10] Dragonfly Pants\n[11] Graphene Body Suit Bottom\n[12] Titan MEM Trooper\n[13] Overwatch Pants (Faction war exclusive)\n[14] Mastodon Legs (Faction war exclusive)\n[15] Mako Pants (Faction war exclusive)\n[16] Vulkan Pants (Faction war exclusive)\n\n>'
pantsRD = '[1] HVM Kevlar Pants\n[2] Trooper Pants\n[3] HVM Carbon Fibre Pants\n[4] Shotlite Hummingbird P1\n[5] Special Forces Pants\n[6] R7 Guardian Pants\n[7] Hardplate Pants\n[8] Medusa Pants\n[9] Dragonfly Pants\n[10] Graphene Body Suit Bottom\n[11] Titan MEM Trooper\n\n>'
pantsBL = '[1] HVM Kevlar Pants\n[2] Trooper Pants\n[3] HVM Carbon Fibre Pants\n[4] Shotlite Hummingbird P1\n[5] Special Forces Pants\n[6] R7 Guardian Pants\n[7] Hardplate Pants\n[8] Medusa Pants\n[9] Dragonfly Pants\n[10] Graphene Body Suit Bottom\n[11] Titan MEM Trooper\n\n>'

bootsNM = '[1] HVM Combat Boots\n[2] Trooper Boots\n[3] Special Forces Boots\n[4] Shotlite Starwalk Boots\n[5] Dynamo Boots (Faction war exclusive)\n[6] HVM Carbon Fibre Boots\n[7] R8 Huntsman Boots\n[8] Hardplate Boots\n[9] Medusa Boots\n[10] Dragonfly Boots\n[11] Graphene Boots\n[12] Titan MEM Sprint\n[13] Overwatch Boots (Faction war exclusive)\n[14] Vulkan Boots (Faction war exclusive)\n[15] Mastodon Boots (Faction war exclusive)\n[16] Mako Boots (Faction war exclusive)\n\n>'
bootsRD = '[1] HVM Combat Boots\n[2] Trooper Boots\n[3] Special Forces Boots\n[4] Shotlite Starwalk Boots\n[5] HVM Carbon Fibre Boots\n[6] R8 Huntsman Boots\n[7] Hardplate Boots\n[8] Medusa Boots\n[9] Dragonfly Boots\n[10] Graphene Boots\n[11] Titan MEM Sprint\n\n>'
bootsBL = '[1] HVM Combat Boots\n[2] Trooper Boots\n[3] Special Forces Boots\n[4] Shotlite Starwalk Boots\n[5] HVM Carbon Fibre Boots\n[6] R8 Huntsman Boots\n[7] Hardplate Boots\n[8] Medusa Boots\n[9] Dragonfly Boots\n[10] Graphene Boots\n[11] Titan MEM Sprint\n\n>'

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
    except ValueError as err:
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
    except ValueError as err:
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
    except ValueError as err:
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
        blackbox = int(input('Set your black strongboxes ammount\n\n>'))
    except ValueError as err:
        main.title()
        print("Please, enter a valid number.")
        time.sleep(3)
        return blackBox()
    main.title()
    print("Loading, please wait...")
    d.decodeProfileSave()
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
    except ValueError as err:
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
    except ValueError as err:
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
        tickets = int(input('Set your SAS cash ammount\n\n>'))
    except ValueError as err:
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
        gun == 2
    elif gun == '2':
        gun == 3
    elif gun == '3':
        gun == 4
    elif gun == '4':
        gun == 5
    elif gun == '5':
        gun == 6
    elif gun == '6':
        gun == 7
    elif gun == '7':
        gun == 8
    elif gun == '8':
        gun == 9
    elif gun == '9':
        gun == 10
    elif gun == '10':
        gun == 11
    elif gun == '11':
        gun == 12
    elif gun == '12':
        gun == 13
    elif gun == '13':
        gun == 14
    elif gun == '14':
        gun == 15
    elif gun == '15':
        gun == 16
    elif gun == '16':
        gun == 17
    elif gun == '17':
        gun == 18
    elif gun == '18':
        gun == 19
    elif gun == '19':
        gun == 20
    elif gun == '20':
        gun == 21
    elif gun == '21':
        gun == 22
    elif gun == '22':
        gun == 23
    elif gun == '23':
        gun == 24
    elif gun == '24':
        gun == 25
    elif gun == '25':
        gun == 26
    elif gun == '26':
        gun == 27
    elif gun == '27':
        gun == 28
    elif gun == '28':
        gun == 29
    elif gun == '29':
        gun == 30
    elif gun == '30':
        main.title()
        print('Loading, please wait...')
        d.decodeProfileSave()
        with open('Profile_unpacked.json', 'r+') as f:
            data = json.load(f)
            f.seek( 0 )
            f.truncate()
            data['PurchasedIAP']['PurchasedIAPArray'][2]['Value'] = True
            data['PurchasedIAP']['PurchasedIAPArray'][3]['Value'] = True
            data['PurchasedIAP']['PurchasedIAPArray'][4]['Value'] = True
            data['PurchasedIAP']['PurchasedIAPArray'][5]['Value'] = True
            data['PurchasedIAP']['PurchasedIAPArray'][6]['Value'] = True
            data['PurchasedIAP']['PurchasedIAPArray'][7]['Value'] = True
            data['PurchasedIAP']['PurchasedIAPArray'][8]['Value'] = True
            data['PurchasedIAP']['PurchasedIAPArray'][9]['Value'] = True
            data['PurchasedIAP']['PurchasedIAPArray'][10]['Value'] = True
            data['PurchasedIAP']['PurchasedIAPArray'][11]['Value'] = True
            data['PurchasedIAP']['PurchasedIAPArray'][12]['Value'] = True
            data['PurchasedIAP']['PurchasedIAPArray'][13]['Value'] = True
            data['PurchasedIAP']['PurchasedIAPArray'][14]['Value'] = True
            data['PurchasedIAP']['PurchasedIAPArray'][15]['Value'] = True
            data['PurchasedIAP']['PurchasedIAPArray'][16]['Value'] = True
            data['PurchasedIAP']['PurchasedIAPArray'][17]['Value'] = True
            data['PurchasedIAP']['PurchasedIAPArray'][18]['Value'] = True
            data['PurchasedIAP']['PurchasedIAPArray'][19]['Value'] = True
            data['PurchasedIAP']['PurchasedIAPArray'][20]['Value'] = True
            data['PurchasedIAP']['PurchasedIAPArray'][21]['Value'] = True
            data['PurchasedIAP']['PurchasedIAPArray'][22]['Value'] = True
            data['PurchasedIAP']['PurchasedIAPArray'][23]['Value'] = True
            data['PurchasedIAP']['PurchasedIAPArray'][24]['Value'] = True
            data['PurchasedIAP']['PurchasedIAPArray'][25]['Value'] = True
            data['PurchasedIAP']['PurchasedIAPArray'][26]['Value'] = True
            data['PurchasedIAP']['PurchasedIAPArray'][27]['Value'] = True
            data['PurchasedIAP']['PurchasedIAPArray'][28]['Value'] = True
            data['PurchasedIAP']['PurchasedIAPArray'][29]['Value'] = True
            data['PurchasedIAP']['PurchasedIAPArray'][30]['Value'] = True
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
    r = int(gun)+1
    main.title()
    print('Loading, please wait...')
    d.decodeProfileSave()
    with open('Profile_unpacked.json', 'r+') as f:
        data = json.load(f)
        f.seek( 0 )
        f.truncate()
        data['PurchasedIAP']['PurchasedIAPArray'][r]['Value'] = True
        json.dump( data, f, indent=4, sort_keys=False )
    if os.path.exists('Profile.save'):
        os.remove('Profile.save')
    d.encodeProfileSave()
    os.remove('Profile_unpacked.json')
    main.title()
    print('Profile.save has been successfuly updated.')
    time.sleep(3)
    return main.mainMenu()

def weaponCfg(strongbox, weaponID, equipVersion, profile):
    main.title()
    try:
        grade = int(input('Set your weapon grade (0-12)\n\n>'))
        if grade > 12:
            main.title()
            print('Please enter a valid value.')
            time.sleep(3)
            return weaponCfg()
    except ValueError as err:
        main.title()
        print('Please enter a valid number.')
        time.sleep(3)
        return weaponCfg()
    main.title()
    try:
        augmentSlots = int(input('Set your weapon augment slots (0-4)\n\n>'))
        if augmentSlots > 4:
            main.title()
            print('Please enter a valid value.')
            time.sleep(3)
            return equipCfg()
    except ValueError as err:
        main.title()
        print('Please enter a valid number.')
        time.sleep(3)
        return weaponCfg()
    main.title()
    try:
        bonusGrade = int(input('Set your weapon bonus stats (0-10)\n\n>'))
        if bonusGrade > 10:
            main.title()
            print('Please enter a valid value.')
            time.sleep(3)
            return weaponCfg()
    except ValueError as err:
        main.title()
        print('Please enter a valid number.')
        time.sleep(3)
        return weaponCfg()
    main.title()
    print('Loading, please wait...')
    d.decodeProfileSave()
    with open('Profile_unpacked.json', 'r+') as f:
        box = json.loads(strongbox)
        data = json.load(f)
        f.seek( 0 )
        f.truncate()
        box['ID'] = int(weaponID)
        box['EquipVersion'] = int(equipVersion)
        box['Grade'] = int(grade)
        box['AugmentSlots'] = int(augmentSlots)
        box['BonusStatsLevel'] = int(bonusGrade)
        data['Inventory'][f'{profile}']['Strongboxes']['Claimed'].append(int(0))
        data['Inventory'][f'{profile}']['Strongboxes']['Claimed'].append(box)
        data['Inventory'][f'{profile}']['Strongboxes']['Claimed'].append(int(1))
        data['Inventory'][f'{profile}']['Strongboxes']['Claimed'].append(int(0))
        json.dump(data, f, indent=4, sort_keys=False)
    if os.path.exists('Profile.save'):
        os.remove('Profile.save')
    d.encodeProfileSave()
    os.remove('Profile_unpacked.json')
    main.title()
    print('Profile.save has been successfuly updated.')
    time.sleep(3)
    return main.mainMenu()

def weapons():
    strongbox = '''
    {
        "ID": 0,
        "EquipVersion": 0,
        "Grade": 0,
        "EquippedSlot": -1,
        "AugmentSlots": 0,
        "InventoryIndex": 1,
        "Seen": false,
        "BonusStatsLevel": 0,
        "Equipped": false,
        "ContainsKey": false,
        "ContainsAugmentCore": false,
        "BlackStrongboxSeed": 0,
        "UseDefaultOpenLogic": true
    }'''
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
        main.title()
        weaponVersion = input('[1] Normal\n[2] Red\n[3] Black\n\n>')
        if weaponVersion == '1':
            main.title()
            equipVersion = 0
            weapon = input(pistolNM)
            if weapon == '1':
                weaponID = 22
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '2':
                weaponID = 23
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '3':
                weaponID = 9
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '4':
                weaponID = 84
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '5':
                weaponID = 141
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '6':
                weaponID = 16
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '7':
                weaponID = 21
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '8':
                weaponID = 6
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '9':
                weaponID = 145
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '10':
                weaponID = 37
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '11':
                weaponID = 98
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '12':
                weaponID = 221
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return weapons()
        elif weaponVersion == '2':
            main.title()
            equipVersion = 1
            weapon = input(pistolRD)
            if weapon == '1':
                weaponID = 78
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '2':
                weaponID = 75
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '3':
                weaponID = 110
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '4':
                weaponID = 67
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '5':
                weaponID = 161
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '6':
                weaponID = 111
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '7':
                weaponID = 70
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '8':
                weaponID = 116
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '9':
                weaponID = 165
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '10':
                weaponID = 77
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '11':
                weaponID = 68
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return weapons()
        elif weaponVersion == '3':
            main.title()
            equipVersion = 2
            weapon = input(pistolBL)
            if weapon == '1':
                weaponID = 10111
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '2':
                weaponID = 10077
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '3':
                weaponID = 10116
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '4':
                weaponID = 10068
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return weapons()
        else:
            main.title()
            print('Invalid Option.')
            time.sleep(3)
            return weapons()
    elif weaponType == '2':
        main.title()
        weaponVersion = input('[1] Normal\n[2] Red\n[3] Black\n\n>')
        if weaponVersion == '1':
            main.title()
            equipVersion = 0
            weapon = input(smgNM)
            if weapon == '1':
                weaponID = 30
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '2':
                weaponID = 17
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '3':
                weaponID = 89
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '4':
                weaponID = 148
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '5':
                weaponID = 8
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '6':
                weaponID = 11
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '7':
                weaponID = 24
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '8':
                weaponID = 160
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '9':
                weaponID = 19
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return weapons()
        elif weaponVersion == '2':
            main.title()
            equipVersion = 1
            weapon = input(smgRD)
            if weapon == '1':
                weaponID = 97
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '2':
                weaponID = 94
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '3':
                weaponID = 106
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '4':
                weaponID = 168
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '5':
                weaponID = 103
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '6':
                weaponID = 87
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '7':
                weaponID = 113
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '8':
                weaponID = 180
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '9':
                weaponID = 105
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return weapons()
        elif weaponVersion == '3':
            main.title()
            equipVersion = 2
            weapon = input(smgBL)
            if weapon == '1':
                weaponID = 10097
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '2':
                weaponID = 10094
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '3':
                weaponID = 10106
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '4':
                weaponID = 10168
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '5':
                weaponID = 10103
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '6':
                weaponID = 10087
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '7':
                weaponID = 10113
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '8':
                weaponID = 10180
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '9':
                weaponID = 10105
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return weapons()
    elif weaponType == '3':
        main.title()
        weaponVersion = input('[1] Normal\n[2] Red\n[3] Black\n\n>')
        if weaponVersion == '1':
            main.title()
            equipVersion = 0
            weapon = input(assaultNM)
            if weapon == '1':
                weaponID = 31
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '2':
                weaponID = 14
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '3':
                weaponID = 72
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '4':
                weaponID = 41
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '5':
                weaponID = 90
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '6':
                weaponID = 146
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '7':
                weaponID = 7
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '8':
                weaponID = 156
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '9':
                weaponID = 15
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '10':
                weaponID = 10
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '11':
                weaponID = 158
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '12':
                weaponID = 36
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '13':
                weaponID = 28
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '14':
                weaponID = 26
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '15':
                weaponID = 222
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '16':
                weaponID = 12
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return weapons()
        elif weaponVersion == '2':
            main.title()
            equipVersion = 1
            weapon = input(assaultRD)
            if weapon == '1':
                weaponID = 87
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '2':
                weaponID = 79
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '3':
                weaponID = 69
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '4':
                weaponID = 102
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '5':
                weaponID = 88
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '6':
                weaponID = 166
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '7':
                weaponID = 109
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '8':
                weaponID = 176
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '9':
                weaponID = 115
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '10':
                weaponID = 100
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '11':
                weaponID = 178
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '12':
                weaponID = 71
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '13':
                weaponID = 99
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '14':
                weaponID = 76
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '15':
                weaponID = 93
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return weapons()
        elif weaponVersion == '3':
            main.title()
            equipVersion = 2
            weapon = input(assaultBL)
            if weapon == '1':
                weaponID = 10087
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '2':
                weaponID = 10079
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '3':
                weaponID = 10069
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '4':
                weaponID = 10102
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '5':
                weaponID = 10088
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '6':
                weaponID = 10166
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '7':
                weaponID = 10109
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '8':
                weaponID = 10176
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '9':
                weaponID = 10115
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '10':
                weaponID = 10100
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '11':
                weaponID = 10178
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '12':
                weaponID = 10071
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '13':
                weaponID = 10099
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '14':
                weaponID = 10076
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '15':
                weaponID = 10093
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return weapons()
    elif weaponType == '4':
        main.title()
        weaponVersion = input('[1] Normal\n[2] Red\n[3] Black\n\n>')
        if weaponVersion == '1':
            main.title()
            equipVersion = 0
            weapon = input(shotgunNM)
            if weapon == '1':
                weaponID = 33
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '2':
                weaponID = 29
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '3':
                weaponID = 13
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '4':
                weaponID = 159
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '5':
                weaponID = 61
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '6':
                weaponID = 231
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return weapons()
        elif weaponVersion == '2':
            main.title()
            equipVersion = 1
            weapon = input(shotgunRD)
            if weapon == '1':
                weaponID = 101
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '2':
                weaponID = 96
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '3':
                weaponID = 85
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '4':
                weaponID = 179
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '5':
                weaponID = 66
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return weapons()
        elif weaponVersion == '3':
            main.title()
            equipVersion = 2
            weapon = input(shotgunBL)
            if weapon == '1':
                weaponID = 10101
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '2':
                weaponID = 10096
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '3':
                weaponID = 10085
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '4':
                weaponID = 10179
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '5':
                weaponID = 10066
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return weapons()
    elif weaponType == '5':
        main.title()
        weaponVersion = input('[1] Normal\n[2] Red\n[3] Black\n\n>')
        if weaponVersion == '1':
            main.title()
            equipVersion = 0
            weapon = input(sniperNM)
            if weapon == '1':
                weaponID = 43
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '2':
                weaponID = 149
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '3':
                weaponID = 39
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '4':
                weaponID = 83
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return weapons()
        elif weaponVersion == '2':
            main.title()
            equipVersion = 1
            weapon = input(sniperRD)
            if weapon == '1':
                weaponID = 107
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '2':
                weaponID = 169
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '3':
                weaponID = 82
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '4':
                weaponID = 81
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return weapons()
        elif weaponVersion == '3':
            main.title()
            equipVersion = 2
            weapon = input(sniperBL)
            if weapon == '1':
                weaponID = 10107
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '2':
                weaponID = 10169
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '3':
                weaponID = 10082
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '4':
                weaponID = 10081
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return weapons()
    elif weaponType == '6':
        main.title()
        weaponVersion = input('[1] Normal\n[2] Red\n[3] Black\n\n>')
        if weaponVersion == '1':
            main.title()
            equipVersion = 0
            weapon = input(rocketNM)
            if weapon == '1':
                weaponID = 34
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '2':
                weaponID = 40
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '3':
                weaponID = 151
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '4':
                weaponID = 228
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '5':
                weaponID = 33
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '6':
                weaponID = 44
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '7':
                weaponID = 154
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '8':
                weaponID = 153
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '9':
                weaponID = 224
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return weapons()
        elif weaponVersion == '2':
            main.title()
            equipVersion = 1
            weapon = input(rocketRD)
            if weapon == '1':
                weaponID = 73
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '2':
                weaponID = 108
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '3':
                weaponID = 171
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '4':
                weaponID = 91
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '5':
                weaponID = 92
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '6':
                weaponID = 174
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '7':
                weaponID = 173
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return weapons()
        elif weaponVersion == '3':
            main.title()
            equipVersion = 2
            weapon = input(rocketBL)
            if weapon == '1':
                weaponID = 10073
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '2':
                weaponID = 10108
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '3':
                weaponID = 10171
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '4':
                weaponID = 10091
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '5':
                weaponID = 10092
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '6':
                weaponID = 10174
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '7':
                weaponID = 10173
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return weapons()
    elif weaponType == '7':
        main.title()
        weaponVersion = input('[1] Normal\n[2] Red\n[3] Black\n\n>')
        if weaponVersion == '1':
            main.title()
            equipVersion = 0
            weapon = input(flameNM)
            if weapon == '1':
                weaponID = 18
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '2':
                weaponID = 223
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '3':
                weaponID = 227
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return weapons()
        elif weaponVersion == '2':
            main.title()
            equipVersion = 1
            weapon = input(flameRD)
            if weapon == '1':
                weaponID = 74
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return weapons()
        elif weaponVersion == '3':
            main.title()
            equipVersion = 2
            weapon = input(flameRD)
            if weapon == '1':
                weaponID = 10074
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return weapons()
    elif weaponType == '8':
        main.title()
        weaponVersion = input('[1] Normal\n[2] Red\n[3] Black\n\n>')
        if weaponVersion == '1':
            main.title()
            equipVersion = 0
            weapon = input(lmgNM)
            if weapon == '1':
                weaponID = 38
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '2':
                weaponID = 25
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '3':
                weaponID = 142
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '4':
                weaponID = 144
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '5':
                weaponID = 20
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '6':
                weaponID = 147
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '7':
                weaponID = 150
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '8':
                weaponID = 152
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '9':
                weaponID = 143
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '10':
                weaponID = 114
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '11':
                weaponID = 225
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return weapons()
        elif weaponVersion == '2':
            main.title()
            equipVersion = 1
            weapon = input(lmgRD)
            if weapon == '1':
                weaponID = 95
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '2':
                weaponID = 104
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '3':
                weaponID = 162
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '4':
                weaponID = 164
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '5':
                weaponID = 80
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '6':
                weaponID = 167
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '7':
                weaponID = 170
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '8':
                weaponID = 172
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '9':
                weaponID = 163
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '10':
                weaponID = 35
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return weapons()
        elif weaponVersion == '3':
            main.title()
            equipVersion = 2
            weapon = input(lmgBL)
            if weapon == '1':
                weaponID = 10095
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '2':
                weaponID = 10104
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '3':
                weaponID = 10162
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '4':
                weaponID = 10164
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '5':
                weaponID = 10080
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '6':
                weaponID = 10167
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '7':
                weaponID = 10170
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '8':
                weaponID = 10172
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '9':
                weaponID = 10163
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '10':
                weaponID = 10035
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return weapons()
    elif weaponType == '9':
        main.title()
        weaponVersion = input('[1] Normal\n[2] Red\n[3] Black\n\n>')
        if weaponVersion == '1':
            main.title()
            equipVersion = 0
            weapon = input(diskNM)
            if weapon == '1':
                weaponID = 157
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '2':
                weaponID = 226
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return weapons()
        elif weaponVersion == '2':
            main.title()
            equipVersion = 1
            weapon = input(diskRD)
            if weapon == '1':
                weaponID = 177
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return weapons()
        elif weaponVersion == '3':
            main.title()
            equipVersion = 2
            weapon = input(diskBL)
            if weapon == '1':
                weaponID = 10177
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return weapons()
    elif weaponType == '10':
        main.title()
        weaponVersion = input('[1] Normal\n[2] Red\n[3] Black\n\n>')
        if weaponVersion == '1':
            main.title()
            equipVersion = 0
            weapon = input(laserNM)
            if weapon == '1':
                weaponID = 155
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            elif weapon == '2':
                weaponID = 229
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return weapons()
        elif weaponVersion == '2':
            main.title()
            equipVersion = 1
            weapon = input(laserRD)
            if weapon == '1':
                weaponID = 175
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return weapons()
        elif weaponVersion == '3':
            main.title()
            equipVersion = 2
            weapon = input(laserRD)
            if weapon == '1':
                weaponID = 10175
                weaponCfg(strongbox, weaponID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return weapons()

def equipCfg(strongbox2, equipID, equipVersion, profile):
    main.title()
    try:
        grade = int(input('Set your equipment grade (0-12)\n\n>'))
        if grade > 12:
            main.title()
            print('Please enter a valid value.')
            time.sleep(3)
            return equipCfg()
    except ValueError as err:
        main.title()
        print('Please enter a valid number.')
        time.sleep(3)
        return equipCfg()
    main.title()
    try:
        augmentSlots = int(input('Set your weapon augment slots (0-3)\n\n>'))
        if augmentSlots > 3:
            main.title()
            print('Please enter a valid value.')
            time.sleep(3)
            return equipCfg()
    except ValueError as err:
        main.title()
        print('Please enter a valid number.')
        time.sleep(3)
        return equipCfg()
    main.title()
    try:
        bonusGrade = int(input('Set your weapon bonus stats (0-10)\n\n>'))
        if bonusGrade > 10:
            main.title()
            print('Please enter a valid value.')
            time.sleep(3)
            return equipCfg()
    except ValueError as err:
        main.title()
        print('Please enter a valid number.')
        time.sleep(3)
        return equipCfg()
    main.title()
    print('Loading, please wait...')
    d.decodeProfileSave()
    with open('Profile_unpacked.json', 'r+') as f:
        box = json.loads(strongbox2)
        data = json.load(f)
        f.seek( 0 )
        f.truncate()
        box['ID'] = int(equipID)
        box['EquipVersion'] = int(equipVersion)
        box['Grade'] = int(grade)
        box['AugmentSlots'] = int(augmentSlots)
        box['BonusStatsLevel'] = int(bonusGrade)
        data['Inventory'][f'{profile}']['Strongboxes']['Claimed'].append(int(1))
        data['Inventory'][f'{profile}']['Strongboxes']['Claimed'].append(box)
        data['Inventory'][f'{profile}']['Strongboxes']['Claimed'].append(int(1))
        data['Inventory'][f'{profile}']['Strongboxes']['Claimed'].append(int(0))
        json.dump(data, f, indent=4, sort_keys=False)
    if os.path.exists('Profile.save'):
        os.remove('Profile.save')
    d.encodeProfileSave()
    os.remove('Profile_unpacked.json')
    main.title()
    print('Profile.save has been successfuly updated.')
    time.sleep(3)
    return main.mainMenu()

def equipment():
    strongbox2 = '''
    {
        "ID": 0,
        "EquipVersion": 0,
        "Grade": 0,
        "EquippedSlot": 1,
        "AugmentSlots": 1,
        "InventoryIndex": 4,
        "Seen": false,
        "BonusStatsLevel": 0,
        "Equipped": false,
        "ContainsKey": false,
        "ContainsAugmentCore": false,
        "BlackStrongboxSeed": 0,
        "UseDefaultOpenLogic": true
    }'''
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
    equipType = input('[1] Helmet\n[2] Vest\n[3] Gloves\n[4] Pants\n[5] Boots\n\n>')
    if equipType == '1':
        main.title()
        equipmentVersion = input('[1] Normal\n[2] Red\n[3] Black\n\n>')
        if equipmentVersion == '1':
            main.title()
            equipVersion = 0
            equip = input(helmetNM)
            if equip == '1':
                equipID = 125
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '2':
                equipID = 110
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '3':
                equipID = 184
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '4':
                equipID = 165
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '5':
                equipID = 232
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '6':
                equipID = 107
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '7':
                equipID = 106
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '8':
                equipID = 173
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '9':
                equipID = 194
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '10':
                equipID = 99
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '11':
                equipID = 206
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '12':
                equipID = 227
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '13':
                equipID = 119
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '14':
                equipID = 237
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '15':
                equipID = 217
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '16':
                equipID = 222
                equipCfg(strongbox2, equipID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return equipment()
        elif equipmentVersion == '2':
            main.title()
            equipVersion = 1
            equip = input(helmetRD)
            if equip == '1':
                equipID = 155
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '2':
                equipID = 162
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '3':
                equipID = 185
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '4':
                equipID = 158
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '5':
                equipID = 143
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '6':
                equipID = 136
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '7':
                equipID = 175
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '8':
                equipID = 195
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '9':
                equipID = 139
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '10':
                equipID = 207
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '11':
                equipID = 130
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return equipment()
        elif equipmentVersion == '3':
            main.title()
            equipVersion = 2
            equip = input(helmetBL)
            if equip == '1':
                equipID = 10155
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '2':
                equipID = 10162
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '3':
                equipID = 10185
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '4':
                equipID = 10158
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '5':
                equipID = 10143
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '6':
                equipID = 10136
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '7':
                equipID = 10175
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '8':
                equipID = 10195
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '9':
                equipID = 10139
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '10':
                equipID = 10207
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '11':
                equipID = 10130
                equipCfg(strongbox2, equipID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return equipment()
    elif equipType == '2':
        main.title()
        equipmentVersion = input('[1] Normal\n[2] Red\n[3] Black\n\n>')
        if equipmentVersion == '1':
            main.title()
            equipVersion = 0
            equip = input(vestNM)
            if equip == '1':
                equipID = 101
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '2':
                equipID = 104
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '3':
                equipID = 186
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '4':
                equipID = 168
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '5':
                equipID = 233
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '6':
                equipID = 100
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '7':
                equipID = 118
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '8':
                equipID = 105
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '9':
                equipID = 112
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '10':
                equipID = 196
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '11':
                equipID = 176
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '12':
                equipID = 208
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '13':
                equipID = 115
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '14':
                equipID = 123
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '15':
                equipID = 228
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '16':
                equipID = 238
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '17':
                equipID = 223
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '18':
                equipID = 218
                equipCfg(strongbox2, equipID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return equipment()
        elif equipmentVersion == '2':
            main.title()
            equipVersion = 1
            equip = input(vestRD)
            if equip == '1':
                equipID = 142
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '2':
                equipID = 148
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '3':
                equipID = 187
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '4':
                equipID = 156
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '5':
                equipID = 154
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '6':
                equipID = 141
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '7':
                equipID = 137
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '8':
                equipID = 164
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '9':
                equipID = 197
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '10':
                equipID = 177
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '11':
                equipID = 209
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '12':
                equipID = 161
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '13':
                equipID = 157
                equipCfg(strongbox2, equipID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return equipment()
        elif equipmentVersion == '3':
            main.title()
            equipVersion = 2
            equip = input(vestBL)
            if equip == '1':
                equipID = 142
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '2':
                equipID = 10148
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '3':
                equipID = 10187
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '4':
                equipID = 10156
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '5':
                equipID = 10154
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '6':
                equipID = 10141
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '7':
                equipID = 10137
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '8':
                equipID = 10164
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '9':
                equipID = 10197
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '10':
                equipID = 10177
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '11':
                equipID = 10209
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '12':
                equipID = 10161
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '13':
                equipID = 10157
                equipCfg(strongbox2, equipID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return equipment()
    elif equipType == '3':
        main.title()
        equipmentVersion = input('[1] Normal\n[2] Red\n[3] Black\n\n>')
        if equipmentVersion == '1':
            main.title()
            equipVersion = 0
            equip = input(glovesNM)
            if equip == '1':
                equipID = 98
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '2':
                equipID = 102
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '3':
                equipID = 190
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '4':
                equipID = 151
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '5':
                equipID = 235
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '6':
                equipID = 128
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '7':
                equipID = 117
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '8':
                equipID = 212
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '9':
                equipID = 180
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '10':
                equipID = 200
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '11':
                equipID = 113
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '12':
                equipID = 230
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '13':
                equipID = 111
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '14':
                equipID = 240
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '15':
                equipID = 225
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '16':
                equipID = 220
                equipCfg(strongbox2, equipID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return equipment()
        elif equipmentVersion == '2':
            main.title()
            equipVersion = 1
            equip = input(glovesRD)
            if equip == '1':
                equipID = 146
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '2':
                equipID = 133
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '3':
                equipID = 191
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '4':
                equipID = 145
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '5':
                equipID = 132
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '6':
                equipID = 181
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '7':
                equipID = 159
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '8':
                equipID = 213
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '9':
                equipID = 201
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '10':
                equipID = 134
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '11':
                equipID = 135
                equipCfg(strongbox2, equipID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return equipment()
        elif equipmentVersion == '3':
            main.title()
            equipVersion = 2
            equip = input(glovesBL)
            if equip == '1':
                equipID = 10146
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '2':
                equipID = 10133
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '3':
                equipID = 10191
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '4':
                equipID = 10145
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '5':
                equipID = 10132
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '6':
                equipID = 10181
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '7':
                equipID = 10159
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '8':
                equipID = 10213
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '9':
                equipID = 10201
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '10':
                equipID = 10134
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '11':
                equipID = 10135
                equipCfg(strongbox2, equipID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return equipment()
    elif equipType == '4':
        main.title()
        equipmentVersion = input('[1] Normal\n[2] Red\n[3] Black\n\n>')
        if equipmentVersion == '1':
            main.title()
            equipVersion = 0
            equip = input(pantsNM)
            if equip == '1':
                equipID = 108
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '2':
                equipID = 129
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '3':
                equipID = 188
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '4':
                equipID = 169
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '5':
                equipID = 234
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '6':
                equipID = 126
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '7':
                equipID = 120
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '8':
                equipID = 178
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '9':
                equipID = 198
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '10':
                equipID = 210
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '11':
                equipID = 117
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '12':
                equipID = 121
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '13':
                equipID = 229
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '14':
                equipID = 239
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '15':
                equipID = 224
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '16':
                equipID = 219
                equipCfg(strongbox2, equipID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return equipment()
        elif equipmentVersion == '2':
            main.title()
            equipVersion = 1
            equip = input(pantsRD)
            if equip == '1':
                equipID = 147
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '2':
                equipID = 166
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '3':
                equipID = 153
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '4':
                equipID = 152
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '5':
                equipID = 189
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '6':
                equipID = 138
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '7':
                equipID = 179
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '8':
                equipID = 211
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '9':
                equipID = 199
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '10':
                equipID = 163
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '11':
                equipID = 171
                equipCfg(strongbox2, equipID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return equipment()
        elif equipmentVersion == '3':
            main.title()
            equipVersion = 2
            equip = input(pantsBL)
            if equip == '1':
                equipID = 10147
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '2':
                equipID = 10166
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '3':
                equipID = 10153
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '4':
                equipID = 10152
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '5':
                equipID = 10189
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '6':
                equipID = 10138
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '7':
                equipID = 10179
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '8':
                equipID = 10211
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '9':
                equipID = 10199
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '10':
                equipID = 10163
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '11':
                equipID = 10171
                equipCfg(strongbox2, equipID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return equipment()
    elif equipType == '5':
        main.title()
        equipmentVersion = input('[1] Normal\n[2] Red\n[3] Black\n\n>')
        if equipmentVersion == '1':
            main.title()
            equipVersion = 0
            equip = input(bootsNM)
            if equip == '1':
                equipID = 114
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '2':
                equipID = 109
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '3':
                equipID = 116
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '4':
                equipID = 144
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '5':
                equipID = 236
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '6':
                equipID = 192
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '7':
                equipID = 122
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '8':
                equipID = 182
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '9':
                equipID = 202
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '10':
                equipID = 214
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '11':
                equipID = 103
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '12':
                equipID = 124
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '13':
                equipID = 231
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '14':
                equipID = 221
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '15':
                equipID = 241
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '16':
                equipID = 226
                equipCfg(strongbox2, equipID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return equipment()
        elif equipmentVersion == '2':
            main.title()
            equipVersion = 1
            equip = input(bootsRD)
            if equip == '1':
                equipID = 131
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '2':
                equipID = 160
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '3':
                equipID = 149
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '4':
                equipID = 152
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '5':
                equipID = 193
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '6':
                equipID = 140
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '7':
                equipID = 205
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '8':
                equipID = 183
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '9':
                equipID = 215
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '10':
                equipID = 170
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '11':
                equipID = 167
                equipCfg(strongbox2, equipID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return equipment()
        elif equipmentVersion == '3':
            main.title()
            equipVersion = 2
            equip = input(bootsBL)
            if equip == '1':
                equipID = 10131
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '2':
                equipID = 10160
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '3':
                equipID = 10149
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '4':
                equipID = 10152
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '5':
                equipID = 10193
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '6':
                equipID = 10140
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '7':
                equipID = 10205
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '8':
                equipID = 10183
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '9':
                equipID = 10215
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '10':
                equipID = 10170
                equipCfg(strongbox2, equipID, equipVersion, profile)
            elif equip == '11':
                equipID = 10167
                equipCfg(strongbox2, equipID, equipVersion, profile)
            else:
                main.title()
                print('Invalid Option.')
                time.sleep(3)
                return equipment()

def setSupport():
    turretjson = '''
    {
        "TurretId": 0,
        "TurretCount": 0
    }'''
    
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
    supply = input('[1] Frag grenades\n[2] Cryo grenades\n[3] HVM turrets\n[4] Cryo turrets\n[5] Heavyshot\n[6] Flugkorper\n[7] Flame turret\n[8] CM Supernova\n[9] CM Zeus\n\n>')
    if supply == '1':
        main.title()
        try:
            a = int(input('Set your supply ammount\n\n>'))
        except ValueError as err:
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
    elif supply == '2':
        main.title()
        try:
            a = int(input('Set your supply ammount\n\n>'))
        except ValueError as err:
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
    elif supply == '3':
        main.title()
        try:
            a = int(input('Set your supply ammount\n\n>'))
        except ValueError as err:
            main.title()
            print('Invalid value')
            time.sleep(3)
            return setSupport()
        main.title()
        print('Loading, please wait...')
        d.decodeProfileSave()
        with open('Profile_unpacked.json', 'r+') as f:
            data = json.load(f)
            p = json.loads(turretjson)
            f.seek( 0 )
            f.truncate()
            turretID = 133
            try:
                data['Inventory'][f'{profile}']['Turrets'][0]['TurretId'] = 133
                data['Inventory'][f'{profile}']['Turrets'][0]['TurretCount'] = int(a)
                json.dump( data, f )
            except IndexError:
                p['TurretsId'] = turretID
                p['TurretsCount'] = int(a)
                data['Inventory'][f'{profile}']['Turrets'].append(p)
                json.dump( data, f )
                pass
        if os.path.exists('Profile.save'):
            os.remove('Profile.save')
        d.encodeProfileSave()
        os.remove('Profile_unpacked.json')
        main.title()
        print('Profile.save has been successfuly updated.')
        time.sleep(3)
        return main.mainMenu()
    elif supply == '4':
        main.title()
        try:
            a = int(input('Set your supply ammount\n\n>'))
        except ValueError as err:
            main.title()
            print('Invalid value')
            time.sleep(3)
            return setSupport()
        main.title()
        print('Loading, please wait...')
        d.decodeProfileSave()
        with open('Profile_unpacked.json', 'r+') as f:
            data = json.load(f)
            p = json.loads(turretjson)
            f.seek( 0 )
            f.truncate()
            turretID = 134
            try:
                data['Inventory'][f'{profile}']['Turrets'][1]['TurretId'] = 134
                data['Inventory'][f'{profile}']['Turrets'][1]['TurretCount'] = int(a)
                json.dump( data, f )
            except IndexError:
                p['TurretsId'] = turretID
                p['TurretsCount'] = int(a)
                data['Inventory'][f'{profile}']['Turrets'].append(p)
                json.dump( data, f )
                pass
        if os.path.exists('Profile.save'):
            os.remove('Profile.save')
        d.encodeProfileSave()
        os.remove('Profile_unpacked.json')
        main.title()
        print('Profile.save has been successfuly updated.')
        time.sleep(3)
        return main.mainMenu()
    elif supply == '5':
        main.title()
        try:
            a = int(input('Set your supply ammount\n\n>'))
        except ValueError as err:
            main.title()
            print('Invalid value')
            time.sleep(3)
            return setSupport()
        main.title()
        print('Loading, please wait...')
        d.decodeProfileSave()
        with open('Profile_unpacked.json', 'r+') as f:
            data = json.load(f)
            p = json.loads(turretjson)
            f.seek( 0 )
            f.truncate()
            turretID = 135
            try:
                data['Inventory'][f'{profile}']['Turrets'][2]['TurretId'] = 135
                data['Inventory'][f'{profile}']['Turrets'][2]['TurretCount'] = int(a)
                json.dump( data, f )
            except IndexError:
                p['TurretsId'] = turretID
                p['TurretsCount'] = int(a)
                data['Inventory'][f'{profile}']['Turrets'].append(p)
                json.dump( data, f )
                pass
        if os.path.exists('Profile.save'):
            os.remove('Profile.save')
        d.encodeProfileSave()
        os.remove('Profile_unpacked.json')
        main.title()
        print('Profile.save has been successfuly updated.')
        time.sleep(3)
        return main.mainMenu()
    elif supply == '6':
        main.title()
        try:
            a = int(input('Set your supply ammount\n\n>'))
        except ValueError as err:
            main.title()
            print('Invalid value')
            time.sleep(3)
            return setSupport()
        main.title()
        print('Loading, please wait...')
        d.decodeProfileSave()
        with open('Profile_unpacked.json', 'r+') as f:
            data = json.load(f)
            p = json.loads(turretjson)
            f.seek( 0 )
            f.truncate()
            turretID = 136
            try:
                data['Inventory'][f'{profile}']['Turrets'][3]['TurretId'] = 136
                data['Inventory'][f'{profile}']['Turrets'][3]['TurretCount'] = int(a)
                json.dump( data, f )
            except IndexError:
                p['TurretsId'] = turretID
                p['TurretsCount'] = int(a)
                data['Inventory'][f'{profile}']['Turrets'].append(p)
                json.dump( data, f )
                pass
        if os.path.exists('Profile.save'):
            os.remove('Profile.save')
        d.encodeProfileSave()
        os.remove('Profile_unpacked.json')
        main.title()
        print('Profile.save has been successfuly updated.')
        time.sleep(3)
        return main.mainMenu()
    elif supply == '7':
        main.title()
        try:
            a = int(input('Set your supply ammount\n\n>'))
        except ValueError as err:
            main.title()
            print('Invalid value')
            time.sleep(3)
            return setSupport()
        main.title()
        print('Loading, please wait...')
        d.decodeProfileSave()
        with open('Profile_unpacked.json', 'r+') as f:
            data = json.load(f)
            p = json.loads(turretjson)
            f.seek( 0 )
            f.truncate()
            turretID = 137
            try:
                data['Inventory'][f'{profile}']['Turrets'][4]['TurretId'] = 137
                data['Inventory'][f'{profile}']['Turrets'][4]['TurretCount'] = int(a)
                json.dump( data, f )
            except IndexError:
                p['TurretsId'] = turretID
                p['TurretsCount'] = int(a)
                data['Inventory'][f'{profile}']['Turrets'].append(p)
                json.dump( data, f )
                pass
        if os.path.exists('Profile.save'):
            os.remove('Profile.save')
        d.encodeProfileSave()
        os.remove('Profile_unpacked.json')
        main.title()
        print('Profile.save has been successfuly updated.')
        time.sleep(3)
        return main.mainMenu()
    elif supply == '8':
        main.title()
        try:
            a = int(input('Set your supply ammount\n\n>'))
        except ValueError as err:
            main.title()
            print('Invalid value')
            time.sleep(3)
            return setSupport()
        main.title()
        print('Loading, please wait...')
        d.decodeProfileSave()
        with open('Profile_unpacked.json', 'r+') as f:
            data = json.load(f)
            p = json.loads(turretjson)
            f.seek( 0 )
            f.truncate()
            turretID = 138
            try:
                data['Inventory'][f'{profile}']['Turrets'][5]['TurretId'] = 138
                data['Inventory'][f'{profile}']['Turrets'][5]['TurretCount'] = int(a)
                json.dump( data, f )
            except IndexError:
                p['TurretsId'] = turretID
                p['TurretsCount'] = int(a)
                data['Inventory'][f'{profile}']['Turrets'].append(p)
                json.dump( data, f )
                pass
        if os.path.exists('Profile.save'):
            os.remove('Profile.save')
        d.encodeProfileSave()
        os.remove('Profile_unpacked.json')
        main.title()
        print('Profile.save has been successfuly updated.')
        time.sleep(3)
        return main.mainMenu()
    elif supply == '9':
        main.title()
        try:
            a = int(input('Set your supply ammount\n\n>'))
        except ValueError as err:
            main.title()
            print('Invalid value')
            time.sleep(3)
            return setSupport()
        main.title()
        print('Loading, please wait...')
        d.decodeProfileSave()
        with open('Profile_unpacked.json', 'r+') as f:
            data = json.load(f)
            p = json.loads(turretjson)
            f.seek( 0 )
            f.truncate()
            turretID = 139
            try:
                data['Inventory'][f'{profile}']['Turrets'][6]['TurretId'] = 139
                data['Inventory'][f'{profile}']['Turrets'][6]['TurretCount'] = int(a)
                json.dump( data, f )
            except IndexError:
                p['TurretsId'] = turretID
                p['TurretsCount'] = int(a)
                data['Inventory'][f'{profile}']['Turrets'].append(p)
                json.dump( data, f )
                pass
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

def collection():
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
        data['CollectionArrayWeapon'][0]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][1]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][2]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][3]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][4]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][5]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][6]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][7]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][8]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][9]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][10]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][11]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][12]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][13]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][14]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][15]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][16]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][17]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][18]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][19]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][20]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][21]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][22]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][23]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][24]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][25]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][26]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][27]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][28]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][29]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][30]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][31]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][32]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][33]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][34]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][35]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][36]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][37]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][38]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][39]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][40]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][41]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][42]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][43]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][44]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][45]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][46]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][47]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][48]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][49]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][50]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][51]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][52]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][53]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][54]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][55]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][56]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][57]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][58]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][59]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][60]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][61]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][62]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][63]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][64]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][65]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][66]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][67]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][68]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][69]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][70]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][71]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][72]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][73]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][74]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][75]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][76]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][77]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][78]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][79]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][80]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][81]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][82]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][83]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][84]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][85]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][86]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][87]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][88]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][89]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][90]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][91]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][92]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][93]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][94]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][95]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][96]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][97]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][98]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][99]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][100]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][101]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][102]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][103]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][104]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][105]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][106]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][107]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][108]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][109]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][110]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][111]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][112]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][113]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][114]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][115]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][116]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][117]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][118]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][119]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][120]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][121]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][122]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][123]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][124]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][125]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][126]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][127]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][128]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][129]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][130]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][131]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][132]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][133]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][134]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][135]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][136]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][137]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][138]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][139]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][140]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][141]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][142]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][143]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][144]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][145]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][146]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][147]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][148]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][149]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][150]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][151]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][152]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][153]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][154]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][155]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][156]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][157]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][158]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][159]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][160]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][161]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][162]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][163]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][164]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][165]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][166]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][167]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][168]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][169]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][170]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][171]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][172]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][173]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][174]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][175]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][176]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][177]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][178]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][179]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][180]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][181]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][182]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][183]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][184]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][185]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][186]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][187]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][188]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][189]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][190]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][191]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][192]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][193]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][194]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][195]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][196]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][197]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][198]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][199]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][200]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][201]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][202]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][203]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][204]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][205]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][206]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][207]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][208]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][209]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][210]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][211]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][212]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][213]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][214]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][215]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][216]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][217]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][218]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][219]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][220]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][221]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][222]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][223]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][224]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][225]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][226]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][227]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][228]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][229]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][230]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][231]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][232]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][233]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][234]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][235]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][236]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][237]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][238]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][239]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][240]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][241]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][242]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][243]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][244]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][245]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][246]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][247]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][248]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][249]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][250]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][251]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][252]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][253]['CollectionUnlocked'] = st
        data['CollectionArrayWeapon'][254]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][0]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][1]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][2]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][3]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][4]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][5]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][6]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][7]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][8]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][9]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][10]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][11]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][12]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][13]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][14]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][15]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][16]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][17]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][18]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][19]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][20]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][21]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][22]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][23]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][24]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][25]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][26]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][27]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][28]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][29]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][30]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][31]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][32]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][33]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][34]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][35]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][36]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][37]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][38]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][39]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][40]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][41]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][42]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][43]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][44]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][45]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][46]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][47]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][48]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][49]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][50]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][51]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][52]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][53]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][54]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][55]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][56]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][57]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][58]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][59]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][60]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][61]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][62]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][63]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][64]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][65]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][66]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][67]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][68]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][69]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][70]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][71]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][72]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][73]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][74]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][75]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][76]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][77]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][78]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][79]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][80]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][81]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][82]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][83]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][84]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][85]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][86]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][87]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][88]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][89]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][90]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][91]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][92]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][93]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][94]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][95]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][96]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][97]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][98]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][99]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][100]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][101]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][102]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][103]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][104]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][105]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][106]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][107]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][108]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][109]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][110]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][111]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][112]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][113]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][114]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][115]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][116]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][117]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][118]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][119]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][120]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][121]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][122]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][123]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][124]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][125]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][126]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][127]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][128]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][129]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][130]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][131]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][132]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][133]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][134]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][135]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][136]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][137]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][138]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][139]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][140]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][141]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][142]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][143]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][144]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][145]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][146]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][147]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][148]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][149]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][150]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][151]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][152]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][153]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][154]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][155]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][156]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][157]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][158]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][159]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][160]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][161]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][162]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][163]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][164]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][165]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][166]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][167]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][168]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][169]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][170]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][171]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][172]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][173]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][174]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][175]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][176]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][177]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][178]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][179]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][180]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][181]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][182]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][183]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][184]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][185]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][186]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][187]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][188]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][189]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][190]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][191]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][192]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][193]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][194]['CollectionUnlocked'] = st
        data['CollectionArrayArmour'][195]['CollectionUnlocked'] = st
        json.dump( data, f, indent=4, sort_keys=False )
    