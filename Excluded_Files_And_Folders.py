import os
import re
import platform


# source_drive_letter = "c".upper()
def create_exluded_folders_list(source_drive_letter, exclude_include):
    if exclude_include == "Include":
        files_and_folders_list = "Included_list.txt"
    if exclude_include == "Exclude":
        files_and_folders_list = "Excluded_List.txt"


    excluded_files_and_folders = []
    with open(files_and_folders_list) as f:
        for lines in f:
            if lines[0] != "#":
                lines = lines.strip() #remove \n charachter. Placed outside loop to not create wmtpy entry in list.
                # print(repr(lines))
                if lines != "":

                    lines = str(lines)

                    lines = lines.strip() #Remove whitespace and tabs (\t)

                    if lines.endswith("\n"): #remove new line tag.
                        lines = lines.strip()

                    if lines.startswith('\"') and lines.endswith('\"'):
                        lines = lines[1:-1]

                    # if lines.startswith("\'") and lines.endswith("\'"):
                    #     lines = lines[1:-1]
                    #     print("remove ' : " + lines)

                    #Check if string is a file, or folder.
                    filename, file_extention = os.path.splitext(lines)
                    # if file_extention == "": #If it is a folder make sure it ends with "/" or "*"
                    #     if not (lines.endswith("*")):
                    #         if not (lines.endswith("/")):
                    #             lines = lines + "/*"

                    #Check if item have drive letter, and remove. And add correct letter.
                    if re.match("^[a-zA-Z]:\\\\", lines): #Find drive letter in beginning of string
                        lines = lines[3:]
                        
                    lines = source_drive_letter.upper() + ":\\" + lines #Add correct drive letter.

                    # if lines.endswith("/*"): #If path ends with /* it will duplicate the path So the script will ignore the actual folder too, Not just the content of said folder.
                    #     lines_new_ending = lines.replace("*","")
                    #     excluded_files_and_folders += [lines_new_ending]
                    
                    excluded_files_and_folders += [lines]
                    # print(repr(lines))
    
    # for items in excluded_files_and_folders:
    #     print(str(items))

    # print(excluded_files_and_folders)
    return(excluded_files_and_folders)

# create_exluded_folders_list(source_drive_letter)