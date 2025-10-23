import socketserver


class SimpleTcp(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        print(f'Received = {data}'.encode("utf-8"))
        self.request.send('Thanks'.encode("utf-8"))
        return
