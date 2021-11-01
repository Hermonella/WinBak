import shutil
from pathlib import Path
import os

source_dir: str = Path('C:/WORKFOLDER/WinBak/Test Folders/Source')
target_dir: str = Path('C:/WORKFOLDER/WinBak/Test Folders/Destination')

list_of_files = []

# shutil.rmtree(target_dir)

source_drive_letter = "C"

excluded_files_and_folders = [
r'://WORKFOLDER//WinBak//Test Folders//Source//Folder2',
r'://WORKFOLDER//WinBak//Test Folders//Source//Folder4'
]

print ("Excluded: ")
print (excluded_files_and_folders)
working_excluded_files_and_folders = []
#Create the working Excluded list: 
for items in excluded_files_and_folders:
    
    working_excluded_files_and_folders.append(Path(source_drive_letter + items))

print("working Excluded: ")
print(working_excluded_files_and_folders)

# list_of_files_to_copy = any(excluded_files in source_dir for excluded_files in source_dir)
# print(list_of_files_to_copy)

# for folder, subfolder, file in os.walk(source_dir):
    # print (root)
    # print (dirs)
    # print (filenames)
    # x = os.path.join(root, dirs, filenames)
    # if x in excluded_files:
    #     continue
for root, dirs, files in os.walk(source_dir, topdown=False):
    for name in dirs:
        x = (os.path.join(root, name))
        list_of_files.append(x)
    for name in files:
        x = (os.path.join(root, name))  
        list_of_files.append(x)
    for item in list_of_files:
        item = source_drive_letter + item
        # print ("item: " + item)
        if item in working_excluded_files_and_folders:
           list_of_files.remove(item)
        
for items in list_of_files: 
    print (items)


# #ignores excluded directories and .exe files
# def get_ignored(path, filenames):
#     print("Ignored")
#     ret = []
#     for filename in filenames:
#         if os.path.join(path, filename) in to_exclude:
#             ret.append(filename)
#         elif filename.endswith(".exe"):
#             ret.append(filename)
#     return ret

# shutil.copytree(source_dir , target_dir ,ignore=get_ignored)

# for f in os.listdir(target_dir):
#     print(f)