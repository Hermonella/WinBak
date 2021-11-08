        if str(x.endswith("/*")):        #If string ends with /* (wildcard character) it will copy the string, remove the /* and add that to the list.
            y = x.rstrip(x[-1])     #It does this to ignore the folder wich all subcontent shall be ignored.
            list_of_files.insert(0, y) 