#!/usr/bin/python
import os
import time
print("Made By Darkwar")
print('\033[91m' + 'Installing please wait')
time.sleep(2)
os.system("pkg update && pkg upgrade")
os.system("pkg install curl php nano python python2 nmap wget git hydra apache2 neofetch fish tor")
os.system("git clone https://github.com/xHak9x/SocialPhish")
os.system("git clone https://github.com/Tuhinshubhra/RED_HAWK.git")
os.system("git clone https://github.com/sqlmapproject/sqlmap")
time.sleep(1)
os.system("termux-setup-storage")
print("Install complete Good luck")
time.sleep(1)
os.system("neofetch")
os.system("rm -fr start.py")
os.system("rm -fr LICENSE")
os.system("rm -fr README.md")
