import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as f:
    f.connect(('127.0.0.1', 8005))
    f.send(bytes("moeinit.com", "utf-8"))
    print(str(f.recv(1024), 'utf-8'))
