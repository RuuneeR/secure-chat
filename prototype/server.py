import socketserver
import threading


class ThreadedRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = str(self.request.recv(1024), "ascii")
        thread = threading.current_thread()
        response = bytes(f"{thread.name}: {data}", "ascii")
        self.request.sendall(response)


class ThreadedTcpServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


if __name__ == "__main__":
    host, port = "localhost", 0
    server = ThreadedTcpServer((host, port), ThreadedRequestHandler)
    with server:
        ip, port = server.server_address
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        print(f"server loop running in thread {server_thread.name}")
