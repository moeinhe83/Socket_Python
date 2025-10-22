import socket
import sys


def tcp_scan(ip, start_port, end_port):
    for port in range(start_port, end_port + 1):
        try:
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if not tcp.connect_ex((ip, port)):
                print(f'[*] {ip}:{port} Open')
                tcp.close()
        except Exception:
            pass
