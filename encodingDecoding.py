import io, json, os
from dgdata import *
import main
import time
import createFile as c

def decodeProfileSave():
    try:
        with io.open( "Profile.save", "rb" ) as fd:
            decoded_bytes = dgdata_decode( fd.read() )
            json_string = decoded_bytes.tobytes().decode( "utf-8" )

        parsed = json.loads(json_string)
        fixed = json.dumps(parsed, indent=4, sort_keys=False)

        with open('Profile_unpacked.json', 'w') as f:
            f.write(fixed)
    except FileNotFoundError:
        main.title()
        if os.path.exists('IDs.json'):
            os.remove('IDs.json')
        print("Profile.save does not exist in the current directory, please try again.")
        time.sleep(3)
        return main.mainMenu()

def encodeProfileSave():
    try:
        with io.open( "Profile_unpacked.json", "rb" ) as fd:
            encode_bytes = dgdata_encode( fd.read() )

        with open('Profile.save', 'wb') as f:
            f.write(encode_bytes)
    except FileNotFoundError:
        if os.path.exists('IDs.json'):
            os.remove('IDs.json')
        main.title()
        print("Profile_unpacked.json does not exist in the current directory, please try again.")
        time.sleep(3)
        return main.mainMenu()
