import socket


def sayhello():
    host, port = "127.0.0.1", 4444

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b"hello")
        while True:
            data = s.recv(1024)
            if not data:
                break
            print(data)


sayhello()
