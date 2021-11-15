import os
import platform

dep = [
    "hurry.filesize==0.9",
    "tqdm==4.62.3",
]


#Install dependencies:
for i in dep:
    os.system("pip install " + i)

if platform.system() == "Windows":
    os.system("pip install wmi")
    os.system("pip install tkinter")
if platform.system() == 'Linux':
    os.system("pip install psutil")
    print("\nInstalling tkinter via apt-get. For some reason this can't be done via pip...")
    os.system("sudo apt-get install python3-tk -y")
    

os.system("python winbak.py")