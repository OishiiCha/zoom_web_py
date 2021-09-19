import getpass
import os

f = open("Zoom_Online.desktop", "x")

usr = str(getpass.getuser())
f.write("[Desktop Entry]\nVersion=1.0\nName=BackMeUp\nComment=Opens Zoom Web Client\nExec=/home/"+ usr +"/zoom_online/zoom_online.py\nIcon=/home/"+ usr +"/Pictures/zoom.ico\nTerminal=false\nType=Application\nCategories=Utility;Application;")

os.system("mv ~/zoom_online/Zoom_Online.desktop ~/Desktop/")
os.system("chmod +x ~/Desktop/Zoom_Online.desktop")