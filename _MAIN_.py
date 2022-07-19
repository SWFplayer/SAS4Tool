from _GLOBAL_OPTIONS_ import factionsOptionMenu, addPremiumItems, addRevive, AddNightmareTickets, removeAds, unlockProfiles
from _PROFILE_OPTIONS_ import addItemsMenu, changeUsername, addCash, setFreeSkillReset, setLevel, setBlackStronboxes, addBlackKeys, addAugmentCores, setSupportItems, addMultiplayerStats
from _UTILS_ import mainTitle
from _EDIT_MANUALLY_ import profileManualEdit
from _SET_PROFILE_PATH_ import setProfilePath
from _FIX_INVENTORY_CRASH_ import fixInventory
from os import _exit, path
from win32console import SetConsoleTitle
from string import ascii_letters
from time import sleep
from json import dump, load
from msvcrt import getch, kbhit
from sys import stdout

mainMenuSelection = ['Global', 'Profile', 'Edit manually', 'Settings', 'About', 'Exit']
configMenuSelection = ['Set Profile', 'Set Profile Path Folder', 'Back up Profile.save [WORK IN PROGRESS]', 'Fix Inventory', 'Back']
globalMenuSelection = ['Factions', 'Premium Items', 'Revive Tokens', 'Premium Nightmare Tickets', 'Remove ads (ADS ON MOBILE)', 'Unlock profile (5-6)', 'Back']
profileMenuSelection = ['Add items', 'Change username', 'Add SAS Cash', 'Set free skill reset', 'Set level', 'Add black Strongboxes', 'Add random Strongboxes [PLACE HOLDER (THIS FEATURE IS WORK IN PROGRESS)]', 'Add black keys', 'Add augment cores', 'Add support items', 'Set stats', 'Back']

def about():
    mainTitle()
    print('''
Developed by: <\\>#0077 | 0daxelagnia

Special thanks to: BlapertureMesa ( cso-idn-player ) and hemisemidemipresent

Official Github repository: https://github.com/0daxelagnia/SAS4Tool/

Latest version: 2.0.0

Made with <3 for the SAS 4 cheats community!



(Press any key to go back)''')
    sleep(0.25)
    while True:
        if kbhit():
            return mainMenu()

def globalMenu():
    SetConsoleTitle('SAS4Tool - Global Menu')
    mainTitle()
    for i in range(len(globalMenuSelection)):
        print(f'[{ascii_letters[26+i]}] - {globalMenuSelection[i]}')
    sleep(0.25)
    while True:
        if kbhit():
            key = getch()
            if key == b'a':
                factionsOptionMenu()
                return mainMenu()
            if key == b'b':
                addPremiumItems()
                return mainMenu()
            if key == b'c':
                addRevive()
                return mainMenu()
            if key == b'd':
                AddNightmareTickets()
                return mainMenu()
            if key == b'e':
                removeAds()
                return mainMenu()
            if key == b'f':
                unlockProfiles()
                return mainMenu()
            if key == b'g':
                return mainMenu()

def profileMenu():
    SetConsoleTitle('SAS4Tool - Profile Menu')
    mainTitle()
    for i in range(len(profileMenuSelection)):
        print(f'[{ascii_letters[26+i]}] - {profileMenuSelection[i]}')
    sleep(0.25)
    while True:
        if kbhit():
            key = getch()
            if key == b'a':
                addItemsMenu()
                return mainMenu()
            if key == b'b':
                changeUsername()
                return mainMenu()
            if key == b'c':
                addCash()
                return mainMenu()
            if key == b'd':
                setFreeSkillReset()
                return mainMenu()
            if key == b'e':
                setLevel()
                return mainMenu()
            if key == b'f':
                setBlackStronboxes()
                return mainMenu()
            if key == b'g':
                pass
            if key == b'h':
                addBlackKeys()
                return mainMenu()
            if key == b'i':
                addAugmentCores()
                return mainMenu()
            if key == b'j':
                setSupportItems()
                return mainMenu()
            if key == b'k':
                addMultiplayerStats()
                return mainMenu()
            if key == b'l':
                return mainMenu()

def setProfileConfig(consoleProfileList):
    SetConsoleTitle('SAS4Tool - Set profile')
    mainTitle()
    print('Select a profile:\n')
    for i in range(len(consoleProfileList)):
        print(f'[{ascii_letters[26+i]}] - {consoleProfileList[i]}')
    sleep(0.25)
    with open('config.json', 'r+') as f:
        data = load(f)
        f.seek(0)
        f.truncate()
        while True:
            if kbhit():
                key = getch()
                if key == b'a':
                    data['consoleDefaultProfile'] = 'Profile 1'
                    data['defaultProfile'] = 'Profile0'
                    dump(data, f)
                    break
                if key == b'b':
                    data['consoleDefaultProfile'] = 'Profile 2'
                    data['defaultProfile'] = 'Profile1'
                    dump(data, f)
                    break
                if key == b'c':
                    data['consoleDefaultProfile'] = 'Profile 3'
                    data['defaultProfile'] = 'Profile2'
                    dump(data, f)
                    break
                if key == b'd':
                    data['consoleDefaultProfile'] = 'Profile 4'
                    data['defaultProfile'] = 'Profile3'
                    dump(data, f)
                    break
                if key == b'e':
                    data['consoleDefaultProfile'] = 'Profile 5'
                    data['defaultProfile'] = 'Profile4'
                    dump(data, f)
                    break
                if key == b'f':
                    data['consoleDefaultProfile'] = 'Profile 6'
                    data['defaultProfile'] = 'Profile5'
                    dump(data, f)
                    break

def configMenu():
    consoleProfileList = ['Profile 1', 'Profile 2', 'Profile 3', 'Profile 4', 'Profile 5', 'Profile 6']
    SetConsoleTitle('SAS4Tool - Config Menu')
    mainTitle()
    for i in range(len(configMenuSelection)):
        print(f'[{ascii_letters[26+i]}] - {configMenuSelection[i]}')
    sleep(0.25)
    while True:
        if kbhit():
            key = getch()
            if key == b'a':
                setProfileConfig(consoleProfileList)
                return mainMenu()
            if key == b'b':
                setProfilePath()
                return mainMenu()
            if key == b'c':
                return mainMenu()
            if key == b'd':
                fixInventory()
                return mainMenu()
            if key == b'e':
                return mainMenu()

def mainMenu():
    SetConsoleTitle('SAS4Tool - Main Menu')
    mainTitle()
    for i in range(len(mainMenuSelection)):
        print(f'[{ascii_letters[26+i]}] - {mainMenuSelection[i]}')
    sleep(0.25)
    while True:
        if kbhit():
            key = getch()
            if key == b'a':
                return globalMenu()
            if key == b'b':
                return profileMenu()
            if key == b'c':
                profileManualEdit()
                return mainMenu()
            if key == b'd':
                configMenu()
                return mainMenu()
            if key == b'e':
                about()
                return mainMenu()
            if key == b'f':
                try:
                    stdout.flush()
                    exit()
                except:
                    stdout.flush()
                    _exit(0)

if __name__ == '__main__':
    contents = {'version': '2.0.0', 'developer': '<\\>#0077', 'defaultProfile': 'Profile0', 'consoleDefaultProfile': 'Profile 1', "profileSavePath": ""}
    if not path.exists('config.json'):
        with open('config.json', 'w') as f:
            f.seek(0)
            f.truncate()
            f = dump(contents, f, indent=4)
    if path.exists('config.json'):
        if path.getsize('config.json') == 0:
            with open('config.json', 'w') as f:
                f.seek(0)
                f.truncate()
                f = dump(contents, f, indent=4)
    mainMenu()