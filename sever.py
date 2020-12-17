import socket
import sqlalchemy 

host="0.0.0.0"
port=1054

with  socket.socket(socket.AF_INET,socket.SOCK_STREAM) as soc_server:
    soc_server.bind((host,port))
    soc_server.listen()
    conn, addr = soc_server.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
