import socket

ip_server = '127.0.0.1'
port_server = 8005


def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip_server, port_server))
    try:
        while True:
            message = input("[*] Enter Message = ")
            client.send(message.encode("utf-8")[:1024])
            response = client.recv(1024)
            response = response.decode("utf-8")
            if response.lower() == 'close':
                break
            print(f'[*] Received : {response}')
    except Exception as e:
        print(f'Error = {e}')
    finally:
        client.close()
        print("Connection Closed")


start_client()
