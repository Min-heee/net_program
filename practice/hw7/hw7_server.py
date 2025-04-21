
import socket

mbox = {}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 9991))

print("UDP 서버 실행 중...")

while True:
    data, addr = server_socket.recvfrom(1024)
    msg = data.decode().strip()

    if msg.startswith("send"):
        try:
            _, mbox_id, *message = msg.split()
            mbox_id = int(mbox_id)
            full_message = ' '.join(message)
            mbox.setdefault(mbox_id, []).append(full_message)
            server_socket.sendto(b"OK", addr)
        except:
            server_socket.sendto(b"Invalid send format", addr)

    elif msg.startswith("receive"):
        try:
            _, mbox_id = msg.split()
            mbox_id = int(mbox_id)
            if mbox_id in mbox and mbox[mbox_id]:
                response = mbox[mbox_id].pop(0)
            else:
                response = "No messages"
            server_socket.sendto(response.encode(), addr)
        except:
            server_socket.sendto(b"Invalid receive format", addr)

    elif msg == "quit":
        print("서버 종료")
        break

server_socket.close()
