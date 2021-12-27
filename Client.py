import socket
import time
from struct import *




Client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
my_ip = '127.0.0.1'   #local computer
my_port = 12350

msg = "Hello UDP Server"
#Client_socket.sendto(msg.encode("utf-8"),('127.0.0.1', 12345))
#Client_socket.sendto(msg.encode("utf-8"),(my_ip, 12345)) #13117
#Client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
# Enable broadcasting mode
Client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
Client_socket.bind(("", my_port))
print("Client started, listening for offer requests...")
while True:

    #ACCEPTING UDP MESSAGES FROM SERVERS
    data, addr = Client_socket.recvfrom(4096)
    udp_format='LBh'
    message = unpack(udp_format,data)
   # print("received message: %s"%data.decode('utf-8'))
    print(message)
    print("Received offer from " + addr[0] +", attempting to connect...")

    #INVITING SERVER TO TCP CONNECTION

    # create a socket connection
    client_tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # let the client connect
    client_tcp_socket.connect((addr[0], message[2]))
    # send some data
    client_tcp_socket.send("SYN".encode('utf-8'))
    # get some data
    response = client_tcp_socket.recv(4096)
    print(response)





Client_socket.close()