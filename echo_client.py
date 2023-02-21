#!/usr/bin/python

#echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # set a timeout of a few seconds
    s.settimeout(3)
    #connect via HOST + PORT
    try:
        #attempt connection
        s.connect((HOST, PORT))
    except:
        #failure 
        print('Failed to connect')
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received {data!r}")