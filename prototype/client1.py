import socket


def sayhelloback():
    host, port = "127.0.0.1", 4444
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print(f"connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(data)
                conn.sendall(b"hello back")


sayhelloback()
