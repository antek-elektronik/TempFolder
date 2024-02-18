#keep this file in a safe location. Run it two times to be sure, and from now on it should work automatically. Enjoy!

#temp folder generator
#Antoni Gzara 2024

import os.path

import getpass
import os
USER_NAME = getpass.getuser()


def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" "%s"' % file_path)


import ctypes.wintypes
CSIDL_PERSONAL = 5       # My Documents
SHGFP_TYPE_CURRENT = 0   # Get current, not default value

buf= ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)

print("temp folder script")
print("Antoni Gzara 2024\n\n\n")

data = input("do you want to continue? y/n\n")
if(data != "y"):
    quit()

add_to_startup()
print("added script to startup folder")


documentsPath = buf.value
path = documentsPath + "\\##TempFolder\\"

exists = os.path.isdir(path)

if(exists):
    print("folder found!")
    for filename in os.listdir(path):
        print(f"file found! name: \"{filename}\"")
        if os.path.isfile(os.path.join(path, filename)):
            os.remove(os.path.join(path, filename))
    print("data deleted!")
    
    input("\n\n\n<press any key to close>")

    '''
    number = input("select what option you want: \n - any key: close\n1.settings\n::")
    if(number == "1"):
        print("option not available yet")
    '''

else:
    os.mkdir(path)
    print("no directory found, new one got created! Run the program again to delete the data from a new folder.")
    
