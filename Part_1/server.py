import socket

ip_server = "127.0.0.1"
port_server = 8005


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip_server, port_server))
    server.listen(0)
    print(f"[*] Listen On {ip_server}:{port_server}")

    client_socket, client_addr = server.accept()
    print(f"[*] Connection From {client_addr[0]} : {client_addr[1]}")

    while True:
        request = client_socket.recv(1024)
        request = request.decode("utf-8")
        if request.lower() == "close":
            client_socket.send("Close".encode("utf-8"))
            break
        print(f"Recevied = {request}")
        client_socket.send("ACCEPTED".encode("utf-8"))

    client_socket.close()
    server.close()


start_server()
