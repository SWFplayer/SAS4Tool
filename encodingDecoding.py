import io, json, os, time
from dgdata import *
import main
from os import walk


def getFolder(dir):
    for root, dirs, files in walk(dir):
        for file in files:
            if file == 'Profile.save' or file == 'Profile_unpacked.json':
                if '\\Data\\Docs\\' in root:
                    return root

mainDir = getFolder('C:\\Program Files (x86)\\Steam\\userdata\\')

fileIn = f'{mainDir}\\Profile.save'
fileOut = f'{mainDir}\\Profile_unpacked.json'

def decodeProfileSave():
    try:
        with io.open( f'{fileIn}', 'rb' ) as fd:
            decoded_bytes = dgdata_decode( fd.read() )
            json_string = decoded_bytes.tobytes().decode( 'utf-8' )

        parsed = json.loads(json_string)
        fixed = json.dumps(parsed, indent=4, sort_keys=False)

        with open( f'{fileOut}', 'w' ) as f:
            f.write(fixed)
    except FileNotFoundError:
        main.title()
        if os.path.exists(f'{mainDir}\\IDs.json'):
            os.remove(f'{mainDir}\\IDs.json')
        print('Profile.save does not exist in the current directory, please try again.')
        time.sleep(3)
        return main.mainMenu()

def encodeProfileSave():
    try:
        with io.open( f'{fileOut}', 'rb' ) as fd:
            encode_bytes = dgdata_encode( fd.read() )

        with open(f'{fileIn}', 'wb') as f:
            f.write(encode_bytes)
    except FileNotFoundError:
        if os.path.exists(f'{mainDir}\\IDs.json'):
            os.remove(f'{mainDir}\\IDs.json')
        main.title()
        print('Profile_unpacked.json does not exist in the current directory, please try again.')
        time.sleep(3)
        return main.mainMenu()

