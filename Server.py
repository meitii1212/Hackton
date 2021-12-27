import time
from struct import *
import socket
import random
import time
import threading

#FUNCTIONS:
def broadcast():
    while True:
        print(" server in broadcast")
        udp_format = 'LBh'
        tcp_port = 12351
        packed = pack(udp_format,0xabcddcba, 0x2, tcp_port)
        #packed= "offer".encode('utf-8')
        UDP_socket.sendto(packed, ('<broadcast>', my_port))
        time.sleep(1)

def searching_client():
    number_of_clients=0
    TCP_socket_server.listen(5)
    print("[*] Listening on %s:%d" % (my_ip, tcp_port))
    client_tcp, address_tcp = TCP_socket_server.accept()
    print("[*] Accepted connection from: %s:%d" % (address_tcp[0], address_tcp[1]))
    # show the data from the client
    request = client_tcp.recv(1024)
    print("[*] Received: %s" % request)
    # Return a packet
    client_tcp.send("ACK!".encode('utf-8'))
    number_of_clients += 1


    #tcp_socket_from_client.close()
    #if number_of_clients==2:

    #WAITING FOR 2 PLAYERS


def play():

    num1=random.randint(0,4)
    num2=random.randint(0,5)
    player1="Instinct"
    player2="Rocket"
    print("Welcome to Quick Maths.\nPlayer 1: "+player1+"\nPlayer 2: "+player2+"\n==\nPlease answer the following question as fast as you can:\nHow much is "+str(num1)+"+"+str(num2)+"?")


#initialing the UDP server
UDP_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,socket.IPPROTO_UDP)
my_ip = '127.0.0.1' #local computer
my_port = 12350

#to which network to connect
#TO DO
#my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

# broadcasting mode
UDP_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
UDP_socket.settimeout(0.2)
print("Server started, listening on IP address "+ my_ip)
UDP_socket.bind((my_ip,my_port))

#INITIALIZING TCP SOCKET

tcp_port = 12351
TCP_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCP_socket_server.bind((my_ip, tcp_port))



#data, addr = my_socket.recvfrom(4096)
#my_socket.sendto(message, addr)
#start threading
t_broadcast =threading.Thread(target=broadcast)
t_searching_client = threading.Thread(target=searching_client, args=())
t_broadcast.start()
t_searching_client.start()


#################################################################################










#num1=random.randint(0,4)
#num2=random.randint(0,5)

#print("Welcome to Quick Maths.\nPlayer 1: Instinct\nPlayer 2: Rocket\n==\nPlease answer the following question as fast as you can:\nHow much is "+str(num1)+"+"+str(num2)+"?")
