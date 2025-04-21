import socket				
				
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)				
s.connect(('localhost', 9000))				
print('Connected to server.')				
				
while True:				
    msg = input("Message (type 'quit' to exit): ")				
    s.send(msg.encode())				
    if msg == 'quit':				
        break				
    data = s.recv(1024)				
    print('Echo from server:', data.decode())				