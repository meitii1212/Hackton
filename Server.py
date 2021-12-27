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
        offer= "offer".encode('utf-8')
        my_socket.sendto(offer, ('<broadcast>', 12345))
        time.sleep(1)

#initialing the server
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,socket.IPPROTO_UDP)
my_ip = '127.0.0.1'   #local computer

#to which network to connect
#TO DO
#my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

# broadcasting mode
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
my_socket.settimeout(0.2)
print("Server started, listening on IP address "+ my_ip)
my_socket.bind((my_ip,12345))



#data, addr = my_socket.recvfrom(4096)
#my_socket.sendto(message, addr)

#start threading
t_broadcast =threading.Thread(target=broadcast)

t_broadcast.start()


#################################################################################










#num1=random.randint(0,4)
#num2=random.randint(0,5)

#print("Welcome to Quick Maths.\nPlayer 1: Instinct\nPlayer 2: Rocket\n==\nPlease answer the following question as fast as you can:\nHow much is "+str(num1)+"+"+str(num2)+"?")
