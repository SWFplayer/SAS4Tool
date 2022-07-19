from _UTILS_ import mainTitle
from win32console import SetConsoleTitle
from tkinter import filedialog
from json import dump, load
from msvcrt import getch, kbhit

def setProfilePath():
    SetConsoleTitle('SAS4Tool - Set Profile Folder Path')
    mainTitle()
    print('''
[A] - Set Profile Folder Path
[B] - Let SAS4Tool choose the Profile Folder Path
[C] - Back''')
    while True:
        if kbhit():
            key = getch()
            if key == b'a':
                mainTitle()
                print('Select the folder where your profiles are stored.')
                folder_path = filedialog.askdirectory( title='Select the folder where your profiles are stored.' )
                with open('.\\config.json', 'r+') as f:
                    data = load(f)
                    f.seek(0)
                    f.truncate()
                    data['profileSavePath'] = folder_path.replace('\\', '\\\\')
                    dump(data, f)
                break
            if key == b'b':
                mainTitle()
                with open('.\\config.json', 'r+') as f:
                    data = load(f)
                    f.seek(0)
                    f.truncate()
                    data['profileSavePath'] = ''
                    dump(data, f)
                break
            if key == b'c':
                pass
            
    