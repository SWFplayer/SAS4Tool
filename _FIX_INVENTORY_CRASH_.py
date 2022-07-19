from _UTILS_ import mainTitle
from win32console import SetConsoleTitle
from json import dump, load
from msvcrt import getch, kbhit
from _UTILS_ import mainTitle, decode_profile as decode_pf, encode_profile as encode_pf, ProfilePath
from os import path, remove
from time import sleep

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

def fixInventory():
    PATH = ProfilePath()
    SetConsoleTitle('SAS4Tool - Fix Inventory')
    mainTitle()
    print('This function removes all strongboxes added to your inventory.\n\n[A] - Start\n[B] - Back')
    while True:
        if kbhit():
            key = getch()
            if key == b'a':
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
                    data['Inventory'][profile]['Strongboxes']['Claimed'] = []
                    dump(data, open(f'{PATH}\\Profile_unpacked.json', 'w'))
                ENDFUNC()
                break
            if key == b'b':
                return None
            