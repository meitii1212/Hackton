from struct import *
import socket
import random

#from scapy.all import *
#initialing the server
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

my_ip = '127.0.0.1'   #local computer
my_socket.bind((my_ip,80))
#to which network to connect
#if(get_if_addr('eth1') is not null):
 #   my_ip_1= get_if_addr('eth1')
#if(get_if_addr('eth2') is not null):
 #   my_ip_2 = get_if_addr('eth2')

#my_socket.bind(('127.0.0.1', 12345))
while True:
    data, addr = my_socket.recvfrom(4096)
    print(str(data))
    message = "hello".encode("utf-8")
    my_socket.sendto(message, addr)

#num1=random.randint(0,4)
#num2=random.randint(0,5)

#print("Welcome to Quick Maths.\nPlayer 1: Instinct\nPlayer 2: Rocket\n==\nPlease answer the following question as fast as you can:\nHow much is "+str(num1)+"+"+str(num2)+"?")
Client_socket.close()
