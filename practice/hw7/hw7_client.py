
import socket

SERVER_ADDRESS = ('localhost', 9991)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input('Enter the message("send mboxId message" or "receive mboxId" or "quit"): ')

    # 전송
    client_socket.sendto(msg.encode(), SERVER_ADDRESS)

    if msg.strip().lower() == "quit":
        break

    # 서버 응답 받기
    data, _ = client_socket.recvfrom(1024)
    print(data.decode())

client_socket.close()
