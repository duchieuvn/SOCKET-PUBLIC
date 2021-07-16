import socket 

#192.168.1.119
HOST = "127.0.0.1" #loopback
SERVER_PORT = 65432 
FORMAT = "utf8"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

s.bind((HOST, SERVER_PORT))
s.listen()

print("SERVER SIDE")
print("server:", HOST, SERVER_PORT)
print("Waiting for Client")

conn, addr = s.accept()

print("client address:",addr)
print("conn:",conn.getsockname())

li = []

msg = None 
while msg != "end":
    msg = conn.recv(1024)
    conn.sendall(msg)
    li.append(msg)
    

print(li)

input()
