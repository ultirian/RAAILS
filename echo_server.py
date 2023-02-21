#!/usr/bin/python

# echo-server.py

import socket
from halo import Halo

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

# Rotating line on windows, on linux dots to show that the server is listening. https://github.com/manrajgrover/halo
spinner = Halo(text='Loading', spinner='dots')
spinner.start()
    
    # socket.AF_INET = IPv4
    # socket.SOCK_STREAM = TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
    # Binds to host and port, but returns first address from DNS Resolution.
    s.bind((HOST, PORT))
    #.listen() enables a server to accept connections. It makes the server a “listening” socket
    s.listen()
    #.accept creates new socket object for conn to loop over blocking calls to con.recv()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            # Returns empty bypes object b'' 
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

spinner.stop()