import socket
import serial 
import time 

#adapter_addr = 'dc:a6:32:01:8a:70' #rpi adres
#adapter_addr = '3c-9C-0F-87-30-BA' #win adres
adapter_addr = '3c:9c:0F:87:30:ba' #win adres

port = 3  # Normal port for rfcomm?
buf_size = 1024

#ser = serial.Serial('COM4',9600)
#s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

with socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM) as s:
    print(f"Connected")
    s.connect((adapter_addr, port))
    s.sendall(b"Hello, world")
    data = s.recv(1024)
    print(f"Received {data!r}")

