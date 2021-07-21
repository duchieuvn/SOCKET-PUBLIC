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

print("Client", addr, "connected")

msg = None
while msg != "x":
    try:
        msg = int(conn.recv(1024))
        print("client ",addr, "says", msg)
        print("conn:",conn.getsockname())
    
    except:
        print("Error")



input()
conn.close()



