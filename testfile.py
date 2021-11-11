from tkinter.constants import Y
import wmi
from hurry.filesize import size, alternative

# DRIVE_TYPES = {
#   0 : "Unknown",
#   1 : "No Root Directory",
#   2 : "Removable Disk",
#   3 : "Local Disk",
#   4 : "Network Drive",
#   5 : "Compact Disc",
#   6 : "RAM Disk"
# }

c = wmi.WMI ()

print("Wich drive do you want to backup? ")
for disk in wmi.WMI().Win32_LogicalDisk(DriveType=3):
    # print(disk)
    disk_space = size(int(disk.Size), system=alternative)
    # print(disk_space + " space in total on drive " + disk.caption)
    print ("Drive " + disk.caption + "   " + disk_space)



source_disk = input("Select drive (Letters only): ").upper()
if len(source_disk) =< 1: #check If source_disk is more than 1 character. 
    ask_later = True
#Make letter uppercase, and filter out everything except letters.
source_disk = source_disk.upper()
source_disk = source_disk.join(filter(set("ABCDEFGHIJKLMNOPQRSTUVWXYZ").__contains__, source_disk))
source_disk = source_disk[0]

if ask_later == True and input("Current selected drive is " + source_disk + " Is this correct?").upper() == Y:  
    return(source_disk)
else: return(source_disk)
