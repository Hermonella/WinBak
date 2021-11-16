import os
import platform
import shutil



dep = [
    "hurry.filesize==0.9",
    "tqdm==4.62.3",
    "GitPython"
]


#Install dependencies:
for i in dep:
    os.system("pip3 install " + i)

if platform.system() == "Windows":
    os.system("pip3 install wmi")
    os.system("pip3 install tk")
if platform.system() == 'Linux':
    os.system("pip3 install psutil")
    print("\nInstalling tkinter via apt-get. For some reason this can't be done via pip...")
    os.system("sudo apt install python3-tk -y")
    print("\nSame for git.")
    os.system("sudo apt install git -y")
    

print("\n\n\n\n\n\n")
# shutil.rmtree("/tmp/WinBak/")
#Download WinBak from Github. SMB is too hard at this stage og the script.
from git import Repo
if not os.getcwd() == "/tmp/WinBak":
    Repo.clone_from(
        "https://github.com/Hermonella/WinBak.git",
        "/tmp/WinBak",
        branch='Copy-From-Linux-Live-USB')

    # os.chdir("/tmp/WinBak")
    os.system("cd /tmp/WinBak")
    os.system("sudo python3 setup.py")

input("Press Enter")


# os.system("python winbak.py")