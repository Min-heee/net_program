import socket
import threading
import time

clients = []

def client_handler(client_sock, addr):
    while True:
        try:
            msg = client_sock.recv(1024)
            if not msg:
                break
            print(f"{time.asctime()} {addr} {msg.decode()}")

            # 메시지를 다른 클라이언트에게 전송
            for c in clients:
                if c != client_sock:
                    c.send(msg)
        except:
            break

    print(f"{time.asctime()} {addr} disconnected")
    clients.remove(client_sock)
    client_sock.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 2501))
server.listen(5)
print('Server Started')

while True:
    client_sock, addr = server.accept()
    print(f"{time.asctime()} {addr} connected")
    clients.append(client_sock)
    th = threading.Thread(target=client_handler, args=(client_sock, addr))
    th.start()
