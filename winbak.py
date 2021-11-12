# Included in python
import shutil
import pathlib
import os
import re
import sys
import fnmatch
#These are installed with PiP
from hurry.filesize import size, alternative
import wmi
from tqdm import tqdm
from tkinter import Tk, filedialog

#These are local files
import Excluded_Files_And_Folders 




def func_source_drive_letter():
    # DRIVE_TYPES = {
    #   0 : "Unknown",
    #   1 : "No Root Directory",
    #   2 : "Removable Disk",
    #   3 : "Local Disk",
    #   4 : "Network Drive",
    #   5 : "Compact Disc",
    #   6 : "RAM Disk"
    # }

    print("Wich drive do you want to backup? ")
    for disk in wmi.WMI().Win32_LogicalDisk(DriveType=3):
        # print(disk)
        disk_space = size(int(disk.Size), system=alternative)
        # print(disk_space + " space in total on drive " + disk.caption)
        print ("Drive " + disk.caption + "   " + disk_space)



    source_disk = input("Select drive (Letters only): ").upper()
    ask_later = False
    if len(source_disk) >= 2: #check If source_disk is more than 1 character. 
        ask_later = True
    #Make letter uppercase, and filter out everything except letters.
    source_disk = source_disk.upper()
    source_disk = source_disk.join(filter(set("ABCDEFGHIJKLMNOPQRSTUVWXYZ").__contains__, source_disk))
    source_disk = source_disk[0]

    if ask_later == True:
        confirm_source_letter = input("Current selected drive is " + source_disk + " Is this correct? (Y/N").upper()
        if ask_later == True and confirm_source_letter == "Y":  
            return(source_disk)
        if ask_later == True and confirm_source_letter == "N":  
            func_source_drive_letter()
        if confirm_source_letter == "":
            func_source_drive_letter()
        else: 
            print("Error in Input.")
            sys.exit()
    else: return(source_disk)


# def func_smb_get_server_address(): #Currently not in use, might delete later.
#     smb_server_address = input("SMB IP or Hostname: ")
#     if re.search(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$', smb_server_address):
#         print("IP: " + smb_server_address)
#         pass
#     if re.search(r'^[A-Za-z]+$', smb_server_address):
#         try: 
#             smb_server_address = socket.gethostbyname(smb_server_address)
#             print("Hostname: " + smb_server_address)
#             return(smb_server_address)

#         except Exception as e: 
#             error = str(e)
#             if (error.find("[Errno 11001]") != -1):
#                 print("Error getting IP address. Check spelling of hostname.")
#                 sys.exit
#             else: 
#                 print("Unknown Error: " + str(error))
#                 sys.exit
#     else: 
#         print("Error with Server address. Check speilling.")
#         sys.exit

#Setup TKinter:
root = Tk() #Sett root to Tk()
root.withdraw() #Hides small tkinger window. Try without it once.
root.attributes('-topmost', True) #Open tkinter window over everything else.


# source_dir: str = pathlib.Path('C:/WORKFOLDER/WinBak/Test Folders/Source/')
# target_dir: str = pathlib.Path('C:/WORKFOLDER/WinBak/Test Folders/Destination/')



list_of_files_and_folders = []

debugmode = False

if debugmode == True: 
    source_drive_letter = "c".upper() #This is usually pathlib.path
    # smb_local_machine_name = socket.gethostname()
    # smb_server_backup_target_location = pathlib.Path("C:\WORKFOLDER\WinBak\Test Folders\Destination") #returns Server location Path

else:
    source_drive_letter = func_source_drive_letter()
    print("Select backup target location: ")
    smb_server_backup_target_location = pathlib.Path(filedialog.askdirectory(title = "Select backup target location")) #returns Server location Path
    target_dir = smb_server_backup_target_location
#TODO: The above script needs to handle empty inputs.


#retrive list of exclutions
excluded_files_and_folders = Excluded_Files_And_Folders.create_exluded_folders_list(source_drive_letter, "Exclude") 

includes_files_and_folders = Excluded_Files_And_Folders.create_exluded_folders_list(source_drive_letter, "Include")
#Include list does not work

#Make source_drive_letter correctly formattet: This needs to be done after retriving exclutions
source_drive_letter = source_drive_letter + ":\\"

#Walk down source_drive_letter to find folder and files
# includes = r'|'.join([fnmatch.translate(x) for x in includes_files_and_folders])
# excludes = r'|'.join([fnmatch.translate(x) for x in excluded_files_and_folders]) or r'$.'


includes_files = []
includes_folders = []
for f in includes_files_and_folders:
    f_str = str(f)
    f = pathlib.Path(f)
    if f.is_file():
        includes_files.append(f_str)
    if f.is_dir():
        includes_folders.append(f_str)


includes = r'|'.join([fnmatch.translate(x) for x in includes_files_and_folders])
excludes = r'|'.join([fnmatch.translate(x) for x in excluded_files_and_folders]) or r'$.'

includes_files_pattern = r'|'.join([fnmatch.translate(x) for x in includes_files])

for root, dirs, files in os.walk(source_drive_letter, topdown=True, followlinks=False):
    dirs[:] = [os.path.join(root,d) for d in dirs]
    dirs[:] = [d for d in dirs if not re.match(excludes, d)] #Breakdown: dirs[:](This is the current list or dirs.) = [d(Declare variable) for d in dirs(Normal for loop) if not re.match(excludes, d)(Check if d is not in excludes list)]


    files = [os.path.join(root, f) for f in files]
    # files = [f for f in files if re.match(includes, f)]
    files = [f for f in files if not re.match(excludes, f)]
    # files = [f for f in files if re.match(includes, f)]


    for i in dirs:
        i = pathlib.Path(i)
        list_of_files_and_folders.append(i)
    for i in files:
        i = pathlib.Path(i)
        list_of_files_and_folders.append(i)


#Add included_list entries to the copy list
for folders in includes_folders:
    for root, dirs, files in os.walk(folders, topdown=True, followlinks=False):
        dirs[:] = [os.path.join(root,d) for d in dirs]
        dirs[:] = [d for d in dirs if not re.match(excludes, d)] #Breakdown: dirs[:](This is the current list or dirs.) = [d(Declare variable) for d in dirs(Normal for loop) if not re.match(excludes, d)(Check if d is not in excludes list)]

        files = [os.path.join(root, f) for f in files]
        files = [f for f in files if not re.match(excludes, f)]
        # files = [f for f in files if re.match(includes_files_pattern, f)]

        for i in dirs:
            i = pathlib.Path(i)
            list_of_files_and_folders.append(i)
        for i in files:
            i = pathlib.Path(i)
            list_of_files_and_folders.append(i)
for i in includes_files:
    i = pathlib.Path(i)
    list_of_files_and_folders.append(i)




f = open("list_of_files.log", "w", encoding="utf-8")
for i in list_of_files_and_folders:
    f.write(str(i) + "\n")

f.close()
print("Done listing.")
print("Done listing.")

error_during_copy = False
for items in tqdm(list_of_files_and_folders):
    if items.is_dir():
        x = target_dir / items.relative_to(items.anchor)
        x.mkdir(parents=True, exist_ok=True) #Create directory in Target_dir
    if items.is_file():
        x = target_dir / items.relative_to(items.anchor)
        try:
            os.makedirs(x, exist_ok=True)
            shutil.copy2(items, x)
        except Exception as e:
            print("Error copying file: " + str(items))
            print("Printing error to FILE_COPY_ERROR.log")
            error = open("FILE_COPY_ERROR.log", "a", encoding="utf-8")
            error.write(str(e) + "\n")
            error_during_copy = True
            continue
            
            #Make the above not freak out if a file in included_files are missing



if error_during_copy == True: 
    print("Copy finished with error. Check FILE_COPY_ERROR.log for info.")
    x = input("Print FILE_COPY_ERROR.log to console? (Y/N): ").upper()
    if x == "Y":
        with open("FILE_COPY_ERROR.log", "r") as f:
            print(f.read())
    if x == "N":
        sys.exit()
else:
    print("Copy finished without error. Yhay!")

