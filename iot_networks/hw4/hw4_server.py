import socket

def calculate(expression):
    try:
        result = eval(expression)
        if isinstance(result, float):
            return f"{result:.1f}"  
        return str(result)
    except Exception:
        return "Error"

def main():
    host = "127.0.0.1" 
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"[*] 서버가 {host}:{port}에서 대기 중...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"[+] {addr}에서 연결됨")

        while True:
            data = client_socket.recv(1024).decode().strip()
            if not data or data.lower() == "q":
                print("[!] 클라이언트 종료")
                break
            print(f"[받음] {data}")

            result = calculate(data)
            client_socket.send(result.encode())

        client_socket.close()

if __name__ == "__main__":
    main()
