import socket				
				
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)				
s.bind(('', 9000))				
s.listen(5)				
print('TCP Echo Server is running...')				
				
while True:				
    client, addr = s.accept()				
    print(f'Connected by {addr}')				
				
    while True:				
        data = client.recv(1024).decode()				
        if not data:				
            break				
        if data == 'quit':				
            print('Client requested to quit.')				
            break				
        print('Received:', data)				