import socket
import threading

ip_server = '127.0.0.1'
port_server = 8005


def handle_client(client_socket, client_addr):
    try:
        while True:
            request = client_socket.recv(1024).decode("utf-8")
            if request.lower() == 'close':
                client_socket.send('Closed'.encode("utf-8"))
                break
            print(f'[*] Received = {request}')
            client_socket.send('Accepted'.encode("utf-8"))
    except Exception as e:
        print(f'Error = {e}')
    finally:
        client_socket.close()
        print(f'{client_addr[0]}:{client_addr[1]}')
