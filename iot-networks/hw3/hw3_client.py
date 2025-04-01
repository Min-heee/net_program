import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9006)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())

my_name = "Byounghee Min"
sock.send(my_name.encode())

student_id = sock.recv(1024).decode()
print(student_id)


sock.close()


