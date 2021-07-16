import socket

HOST = "127.0.0.1"
SERVER_PORT = 65432
FORMAT = "utf8"


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("CLIENT SIDE")
client.connect( (HOST, SERVER_PORT) )
print("client address:",client.getsockname())


li = [1,2,2]

for item in li:
    client.sendall(item)
    client.recv(1024)

endMessage = "end"
client.sendall(endMessage.encode(FORMAT))



input()
