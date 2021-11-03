import shutil
import pathlib
import os




source_dir: str = pathlib.Path('C:/WORKFOLDER/WinBak/Test Folders/Source/')
target_dir: str = pathlib.Path('C:/WORKFOLDER/WinBak/Test Folders/Destination/')

list_of_files = []

source_drive_letter = "C"

excluded_files_and_folders = [
":/WORKFOLDER/WinBak/Test Folders/Source/Folder2",
":/WORKFOLDER/WinBak/Test Folders/Source/Folder4"
]


#Create the working Excluded list: 
working_excluded_files_and_folders = []
for items in excluded_files_and_folders:
    
    working_excluded_files_and_folders.append(pathlib.Path(source_drive_letter + items))


for root, dirs, files in os.walk(source_dir, topdown=False):
    for name in dirs:
        x = (pathlib.Path(os.path.join(root, name)))  
        list_of_files.insert(0, x)
    for name in files:
        x = (pathlib.Path(os.path.join(root, name)))  
        list_of_files.append(x)
    for item in list_of_files:
        if item in working_excluded_files_and_folders:
            print("Found exception. removing")
            list_of_files.remove(item)
        else: 
            pass

        

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
