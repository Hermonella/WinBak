import os
import platform
import shutil

if platform.system() == 'Linux':
    os.system("sudo apt install git -y")

WinBak_tmp_folder = "/tmp/WinBak"
print("\n\n\n\n\n\n")
#Download WinBak from Github. SMB is too hard at this stage og the script.
if not os.getcwd() == WinBak_tmp_folder:
    if os.path.isdir(WinBak_tmp_folder):
        shutil.rmtree(WinBak_tmp_folder)
        # os.rmdir(WinBak_tmp_folder)
    else: pass

    from git import Repo
    Repo.clone_from(
        "https://github.com/Hermonella/WinBak.git",
        WinBak_tmp_folder,
        branch='Copy-From-Linux-Live-USB')

    # os.chdir(WinBak_tmp_folder)
    os.chdir(WinBak_tmp_folder)
    # os.system("cd /tmp/WinBak")
    os.system("sudo python3 setup.py")




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
    

print("\n\n")
x= os.getcwd()
print(x)
input("Press Enter")


# os.system("python winbak.py")