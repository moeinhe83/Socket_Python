import socket
import threading

ip_server = '127.0.0.1'
port_server = 8005


def handle_client(client_socket, client_addr):
    try:
        while True:
            request = client_socket.recv(1024).decode("utf-8")
            if request.lower() == 'close':
                client_socket.send('[*] Closed'.encode("utf-8"))
                break
            print(f'[*] Received = {request}')
            client_socket.send('[*] Accepted'.encode("utf-8"))
    except Exception as e:
        print(f'[*] Error = {e}')
    finally:
        client_socket.close()
        print(f'{client_addr[0]}:{client_addr[1]}')


def start_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((ip_server, port_server))
        server.listen()
        print(f'[*] Listen On {ip_server}:{port_server}')
        while True:
            client_socket, client_addr = server.accept()
            print(
                f'[*] Accepted  Connection From {client_addr[0]}:{client_addr[1]}')
            thread = threading.Thread(
                target=handle_client,
                args=(client_socket, client_addr)
            )
            thread.start()
    except Exception as e:
        print(f'[*] Error = {e}')
    finally:
        server.close()


start_server()
