import socket

ip_server = "127.0.0.1"
port_server = 8005


def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip_server, port_server))

    while True:
        message = input("[*] Enter Message = ")
