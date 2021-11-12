import os


#Install dependencies:
for i in open("requirements.txt", "r"):
    os.system("pip install " + i)
        
os.system("python winbak.py")