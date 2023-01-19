import socket
import random
from threading import Thread
from datetime import datetime
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5002 # server's port
separator_token = "<SEP>" # we will use this to separate the client name & message
# TCP socket
s = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
# connect to the server
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")
name = input("Wag1 Bruv, state ur name for the mandem: ")
def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        print("\n" + message)
t = Thread(target=listen_for_messages)
t.daemon = True
# start the thread
t.start()
while True:
    to_send =  input()
    if to_send.lower() == 'q':
        break
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    to_send = f"[{date_now}] {name}{separator_token}{to_send}"
    s.send(to_send.encode())
# close the socket
s.close()