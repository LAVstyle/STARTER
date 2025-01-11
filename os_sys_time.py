import os
import time

def start_file(path):
    os.startfile(f"{path}")
    time.sleep(1)

def start_web_site(name):
    os.system(f"start {name}")
    time.sleep(1)
