import shutil
import os

source_dir: str = r'C:\WORKFOLDER\WinBak\Test Folders\Source'
target_dir: str = r'C:\WORKFOLDER\WinBak\Test Folders\Destination'

# shutil.rmtree(target_dir)

excluded_files = [
'C:\\WORKFOLDER\\WinBak\\Test Folders\\Source\\Folder2',
'C:\\WORKFOLDER\\WinBak\\Test Folders\\Source\\Folder4'
]


# list_of_files_to_copy = any(excluded_files in source_dir for excluded_files in source_dir)
# print(list_of_files_to_copy)

for root, dirs, filenames in os.walk(source_dir):
    # print (root)
    # print (dirs)
    # print (filenames)
    x = os.path.join(root, dirs, filenames)
    if x in excluded_files:
        continue

    print (x)


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