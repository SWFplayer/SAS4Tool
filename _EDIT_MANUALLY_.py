from _UTILS_ import mainTitle, decode_profile as decode_pf, encode_profile as encode_pf, ProfilePath
from time import sleep
from os import path, remove
from msvcrt import getch, kbhit
from json import load, dump



def profileManualEdit():
    PATH = ProfilePath()
    mainTitle()
    print('''
[A] - Decode Profile.save to JSON
[B] - Encode Profile_unpacked.json to Profile.save
[C] - Back''')
    sleep(0.25)
    while True:
        if kbhit():
            key = getch()
            if key == b'a':
                if path.exists(f'{PATH}\\Profile_unpacked.json'):
                    remove(f'{PATH}\\Profile_unpacked.json')
                mainTitle()
                print('Loading...')
                decode_pf()
                with open(f'{PATH}\\Profile_unpacked.json', 'r+') as f:
                    data = load(f)
                    f.seek(0)
                    f.truncate()
                    dump(data, open(f'{PATH}\\Profile_unpacked.json', 'w'), indent=4)
                mainTitle()
                print('Done!')
                sleep(1)
                return profileManualEdit()
            if key == b'b':
                if path.exists(f'{PATH}\\Profile.save'):
                    remove(f'{PATH}\\Profile.save')
                mainTitle()
                print('Loading...')
                with open(f'{PATH}\\Profile_unpacked.json', 'r+') as f:
                    data = load(f)
                    f.seek(0)
                    f.truncate()
                    dump(data, open(f'{PATH}\\Profile_unpacked.json', 'w'), indent=False)
                encode_pf()
                mainTitle()
                print('Done!')
                sleep(1)
                return profileManualEdit()
            if key == b'c':
                break
    pass