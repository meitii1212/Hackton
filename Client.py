import socket
import time

Client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
my_ip = '127.0.0.1'   #local computer
msg = "Hello UDP Server"
#Client_socket.sendto(msg.encode("utf-8"),('127.0.0.1', 12345))
#Client_socket.sendto(msg.encode("utf-8"),(my_ip, 12345)) #13117
#Client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
# Enable broadcasting mode
Client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
Client_socket.bind(("", 12345))
print("Client started, listening for offer requests...")
while True:
    data, addr = Client_socket.recvfrom(4096)
    print("received message: %s"%data.decode('utf-8'))



Client_socket.close()