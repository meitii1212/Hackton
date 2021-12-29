
from struct import *
import socket
import random
from time import *
import threading
import select
import sys
from datetime import datetime

#FUNCTIONS:
def broadcast():
    while True:
        print(" server in broadcast")
        udp_format = 'LBh'
        tcp_port = 12351
        packed = pack(udp_format,0xabcddcba, 0x2, tcp_port)
        #packed= "offer".encode('utf-8')
        UDP_socket.sendto(packed, ('<broadcast>', my_port))
        sleep(1)

def searching_client():
    global number_of_clients
    global my_clients 
    global now

    while  number_of_clients[0]< 2:
        TCP_socket_server.listen(2)
        print("[*] Listening on %s:%d" % (my_ip, tcp_port))
        client_tcp, address_tcp = TCP_socket_server.accept()
        print("[*] Accepted connection from: %s:%d" % (address_tcp[0], address_tcp[1]))
        # show the data from the client =SYN
        request = client_tcp.recv(1024)
        print("[*] Received: %s" % request)
        # Return a packet
        client_tcp.send('ACK!'.encode('utf-8'))
        client_name = client_tcp.recv(1024)
        lock.acquire()
        number_of_clients[0] += 1
        my_clients += [(client_tcp,address_tcp,client_name.decode('utf-8'))]
        lock.release()
   
    print("GOT TWO CONNECTIONS START GAME")
    
    now = time()


def start_game(*args):
    global my_clients
    global answer_list
    
    num1=args[0][1]
    num2=args[0][2]
    player1 = my_clients[0][2]
    player2 = my_clients[1][2]
    game_directions = "Welcome to Quick Maths.\nPlayer 1: "+player1+"\nPlayer 2: "+player2+"\n==\nPlease answer the following question as fast as you can:\nHow much is "+str(num1)+"+"+str(num2)+"?"
    my_clients[args[0][0]][0].send(game_directions.encode('utf-8'))
    answer = my_clients[args[0][0]][0].recv(1024)
    answer1 = (my_clients[args[0][0]][2],int(answer.decode('utf-8'))) #(group name, answer)

    #ADDING THE ANSWER TO THE FINAL LIST 
    lock_answers.acquire()
    answer_list += answer1
    lock_answers.release()
    #client_tcp.sendall(game_directions.encode('utf-8'))

def finish_game(*args):
    finish_message = args[0][3]
    my_clients[args[0][0]][0].send(finish_message.encode('utf-8'))
    print("server sent a finishing game")



#initialing the UDP server
UDP_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,socket.IPPROTO_UDP)
my_ip = '127.0.0.1' #local computer
my_port = 12350
#to which network to connect
#TO DO
UDP_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# broadcasting mode
UDP_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
UDP_socket.settimeout(0.2)
print("Server started, listening on IP address "+ my_ip)
UDP_socket.bind((my_ip,my_port))

#INITIALIZING TCP SOCKET
number_of_clients=[]
number_of_clients.append(0)
my_clients = [] 
clients_names=[]
lock = threading.Lock()
tcp_port = 12351
TCP_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCP_socket_server.bind((my_ip, tcp_port))



#data, addr = my_socket.recvfrom(4096)
#my_socket.sendto(message, addr)

#start broadcasting &listening to clients concurrently
t_broadcast =threading.Thread(target=broadcast)
t_searching_client = threading.Thread(target=searching_client, args=())
t_broadcast.start()
t_searching_client.start()

#waiting for two connections
t_searching_client.join()


global answer_list
answer_list =[]
global lock_answers

lock_answers = threading.Lock()


#start playing with two players

num11 = random.randint(0, 4)
num22 = random.randint(0, 5)
list_player1 = [0,num11,num22]
list_player2 = [1,num11,num22]
t_player_1 = threading.Thread(target=start_game,args=(list_player1,))
t_player_2 = threading.Thread(target=start_game ,args=(list_player2,))
t_player_1.start()
t_player_2.start()


future = now+10
while  time() < future and len(answer_list)<1:
#while len(answer_list) <1:
    sleep(0.01)

#print("Answer ")
#checkin the answer of the first client in list 
if time() < future:
    if(answer_list[1]==(num11+num22)):
        winner = answer_list[0]
    else:
        #second player won 
        if my_clients[0][2] == answer_list[0]: #loser
            winner = my_clients[1][2]
        else:
            winner = my_clients[0][2]

    
    final_message = ("Game over!\n" + "The correct answer was "+str(num11+num22)+"!\n"+"Congratulations to the winner: "+ winner+"\n")
    
else:
    final_message = "There is a draw!"

list_player11 = [0,num11,num22,final_message]
list_player22 = [1,num11,num22,final_message]

t_send_end_1 = threading.Thread(target=finish_game ,args=(list_player11,))
t_send_end_2 = threading.Thread(target=finish_game ,args=(list_player22,))
t_send_end_1.start()
t_send_end_1.join()
t_send_end_2.start()
t_send_end_2.join()







#################################################################################










#num1=random.randint(0,4)
#num2=random.randint(0,5)

#print("Welcome to Quick Maths.\nPlayer 1: Instinct\nPlayer 2: Rocket\n==\nPlease answer the following question as fast as you can:\nHow much is "+str(num1)+"+"+str(num2)+"?")
