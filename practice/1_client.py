import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 9002))
    
    print(client_socket.recv(1024).decode())  # Welcome 메시지 출력
    
    try:
        while True:
            msg = input("> ")
            client_socket.send(msg.encode())
            if msg.lower() == 'exit':
                break
            print(client_socket.recv(1024).decode())
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()