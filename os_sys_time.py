import os
import time

def start_file(path):
    os.startfile(f"C:\Users\AVL\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code")
    time.sleep(1)

def start_web_site(name):
    os.system(f"start https://calendar.google.com/calendar/u/0/r")
    time.sleep(1)

start_file()
start_web_site()
