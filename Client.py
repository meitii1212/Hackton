import socket
import time
from struct import *
import sys




Client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
my_ip = '127.0.0.1'   #local computer
my_port = 12350

msg = "Hello UDP Server"
#Client_socket.sendto(msg.encode("utf-8"),('127.0.0.1', 12345))
#Client_socket.sendto(msg.encode("utf-8"),(my_ip, 12345)) #13117
Client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
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
    try:

        # create a socket connection
        client_tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # let the client connect
        client_tcp_socket.connect((addr[0], message[2]))
        # send some data
        client_tcp_socket.send("SYN".encode('utf-8'))
        # get some data =ACK
        response = client_tcp_socket.recv(4096)
        print(response.decode('utf-8'))
        group_name = input()
        # sendin group name
        client_tcp_socket.send(group_name.encode('utf-8'))
        # get directions of the game from server
        game_directions = client_tcp_socket.recv(4096)
        print(game_directions.decode('utf-8'))

        #input for answer
        answer = sys.stdin.readline()[0]
        client_tcp_socket.send(answer.encode('utf-8'))

        break
    except:
        pass

#enter group name from keyboard
enter_name_ask = client_tcp_socket.recv(4096)
print(enter_name_ask.decode('utf-8'))
group_name = input()

# sendin group name
client_tcp_socket.send(group_name.encode('utf-8'))

#input for answer
answer = sys.stdin.readline()[0]
client_tcp_socket.send(answer.encode('utf-8'))


#Client_socket.close()