import shutil
import pathlib
import os
import re
import sys
from getpass import getpass, getuser
import socket
from tkinter import Tk, filedialog
import itertools
import fnmatch

def func_smb_get_server_address():
    smb_server_address = input("SMB IP or Hostname: ")
    if re.search(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$', smb_server_address):
        print("IP: " + smb_server_address)
        pass
    if re.search(r'^[A-Za-z]+$', smb_server_address):
        try: 
            smb_server_address = socket.gethostbyname(smb_server_address)
            print("Hostname: " + smb_server_address)
            return(smb_server_address)

        except Exception as e: 
            error = str(e)
            if (error.find("[Errno 11001]") != -1):
                print("Error getting IP address. Check spelling of hostname.")
                sys.exit
            else: 
                print("Unknown Error: " + str(error))
                sys.exit
    else: 
        print("Error with Server address. Check speilling.")
        sys.exit

#Setup TKinter:
root = Tk() #Sett root to Tk()
root.withdraw() #Hides small tkinger window. Try without it once.
root.attributes('-topmost', True) #Open tkinter window over everything else.


source_dir: str = pathlib.Path('C:/WORKFOLDER/WinBak/Test Folders/Source/')
target_dir: str = pathlib.Path('C:/WORKFOLDER/WinBak/Test Folders/Destination/')

list_of_files = []

debugmode = True

if debugmode == True: 
    source_drive_letter = pathlib.Path("C:\\")
    print(source_drive_letter)
    smb_domain = "x"
    smb_user = "x"
    smb_password = "x"
    smb_local_machine_name = socket.gethostname()
    smb_server_backup_target_location = pathlib.Path("C:\WORKFOLDER\WinBak\Test Folders\Destination") #returns Server location Path
    print(smb_server_backup_target_location)

else:
    # source_drive_letter = input("Source Drive Letter: ")
    print("Choose witch drive to backup: ")
    source_drive_letter = pathlib.Path(filedialog.askdirectory(title = "Choose drive to backup"))
    print(source_drive_letter)


    #Set all SMB variables. Such as wich drive to backup, and where to save it.
    smb_domain = input("SMB Domain: ")
    smb_user = input("SMB Username: ") 
    smb_password = getpass(prompt="SMB Password: ")
    smb_local_machine_name = socket.gethostname()
    # smb_server_name = input("SMB Server name: ")
    # smb_server_address = func_smb_get_server_address()
    # smb_server_backup_location = 
    print("Select backup target location: ")
    smb_server_backup_target_location = pathlib.Path(filedialog.askdirectory(title = "Select backup target location")) #returns Server location Path
    # print(smb_server_backup_target_location)

#TODO: The above script needs to handle empty inputs.

excluded_files_and_folders = [
"WORKFOLDER/WinBak/Test Folders/Source/Folder2/*",
"WORKFOLDER/WinBak/Test Folders/Source/Folder4/*"
]


#Create the working Excluded list: 
working_excluded_files_and_folders = []
for items in excluded_files_and_folders:
    constructed_path = pathlib.Path(str(source_drive_letter) + items)
    working_excluded_files_and_folders.append(constructed_path)
    if str(items.endswith("/*")):   #If path ends with /* it will duplicate the path
        x = str(constructed_path)   #So the script will ignore the actual folder too, 
        x = x[:-1]                  #Not just the content of said folder.
        working_excluded_files_and_folders.append(pathlib.Path(x))

for item in working_excluded_files_and_folders:
    print(item)

#Walk down Source_dir to find folder and files
for root, dirs, files in os.walk(source_dir, topdown=False):
    for name in dirs:
        x = (pathlib.Path(os.path.join(root, name)))  
        list_of_files.insert(0, x) #Place folders first in list
    for name in files:
        x = (pathlib.Path(os.path.join(root, name)))  
        list_of_files.append(x)


for excludeditem in working_excluded_files_and_folders: 
    for item in list_of_files:
        x = str(item)
        y = str(excludeditem)
        if (fnmatch.fnmatch(x, y)): #Does not expect list
            print("\nFound exception, Removing:")
            print("Item:         " + str(item))
            print("excludeditem: " + str(excludeditem))
            list_of_files.remove(item)
        else: 
            pass


# for items in list_of_files:
#     print(items)
        

for items in list_of_files:
    if os.path.isdir(items):
        x = target_dir / items.relative_to(items.anchor)
        x.mkdir(parents=True, exist_ok=True) #Create directory in Target_dir
        # print("x: " + str(x)) #Debug
        pass
    if os.path.isfile(items):
        x = target_dir / items.relative_to(items.anchor)
        shutil.copy(items, x)
        pass
    # else: print("Error with: " + str(items))
