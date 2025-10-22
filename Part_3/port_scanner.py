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


def ip_scan(ip, start_port, end_port):
    print(f'[*] Start Scan Port : {ip}')
    tcp_scan(ip, start_port, end_port)
    print(f'[*] Finish Scan Port : {ip}')


def domain_scan(domain, start_port, end_port):
    print(f'[*] Start Scan Port : {domain}')
    ip = socket.gethostbyname(domain)
    tcp_scan(ip, start_port, end_port)
    print(f'[*] Finish Scan Port : {domain}')


if __name__ == '__main__':
    socket.setdefaulttimeout(0.1)
    if len(sys.argv) < 4:
        print('[*] Usage: python port_scanner.py <ip> <start port> <end port>')
        print('[*] Usage: python port_scanner.py <domain> <start port> <end port>')
    elif len(sys.argv) >= 4:
        name = sys.argv[1]
        start_port = int(sys.argv[2])
        end_port = int(sys.argv[3])
    if len(sys.argv) == 4:
        ip_scan(name, start_port, end_port)
    elif len(sys.argv) == 5:
        domain_scan(name, start_port, end_port)
