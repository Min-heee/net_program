def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 9002))
    server_socket.listen()  # backlog 인자 생략 (기본값 사용)
    
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        
        client_socket.send(b"Welcome to Server")
        
        try:
            while True:
                data = client_socket.recv(1024)
                if not data or data.decode().strip().lower() == 'exit':
                    break
                client_socket.send(data.decode().upper().encode())
        finally:
            client_socket.close()
            print(f"Connection with {addr} closed")

if __name__ == "__main__":
    start_server()