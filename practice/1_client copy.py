import socket

def main():
    host = "127.0.0.1"
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        expr = input("계산식 입력 (예: 20 + 17, 종료: q) ▶ ")
        if expr.lower() == "q":
            client_socket.send(expr.encode())
            print("연결 종료")
            break

        client_socket.send(expr.encode())
        result = client_socket.recv(1024).decode()
        print(f"결과: {result}")

    client_socket.close()

if __name__ == "__main__":
    main()