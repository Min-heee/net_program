import socket
import threading

def recv_handler(sock):
    while True:
        try:
            msg = sock.recv(1024)
            if not msg:
                break
            print(msg.decode())
        except:
            break

# 서버 주소 및 포트
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 2501))  # 원격이면 IP 변경

# 사용자 ID 입력
my_id = input('ID를 입력하세요: ')
sock.send(('[%s]' % my_id).encode())

# 수신 스레드 시작
th = threading.Thread(target=recv_handler, args=(sock,))
th.daemon = True
th.start()

# 입력하여 서버로 메시지 전송
while True:
    msg = '[' + my_id + '] ' + input()
    sock.send(msg.encode())
