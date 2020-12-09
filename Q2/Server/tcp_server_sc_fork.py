#########################################
#Import libraries
#########################################
import socket
import os
import time
import select
from time import sleep

#########################################
#Declaring Connection Variables
#########################################
BUFFER_SIZE = 1024                                   #Buffer Size for receiving file in chunks
BUFFER_FILENAME = 1024                              #Buffer size for receiving file name
SERVER_IP = 'localhost'                             #Server IP
SERVER_PORT = 12345                                 #Server Port Number
CLIENTS = 10

#########################################
#Initializing UDP Socket
#########################################
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Starting server on port ',SERVER_PORT)

#########################################
#Uncomment the line below for disabling Nagle's Algortihm
#########################################

# sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

#########################################
#Uncomment the line below for disabling Delayed Ack
#########################################

# sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_QUICKACK, 1)

sock.bind((SERVER_IP, SERVER_PORT))

sock.listen(1)    

def thread_worker(connection, client_addr):

    file_name = connection.recv(BUFFER_FILENAME).decode()                   #Receive file name
 
    while (file_name):                                                     

        fd = open(file_name, 'rb')                                          #Open file in read mode
        connection.send(b'sent')
        connection.recv(100)
        
        buf = fd.read(BUFFER_SIZE)                                          #Read from file equal to buffer size

        print('Sending Data')

        while(buf): 
            connection.send(buf)                                            #Send data to the client
            connection.recv(100)
            buf = fd.read(BUFFER_SIZE)

        fd.close()                                                          #Close file
        
        connection.send(b'EOF')

        file_name = connection.recv(BUFFER_FILENAME)                    #Receive file name
    
    connection.close()                                                  #Close connection

i = 0

while (i < CLIENTS):
    print('Waiting for connection')
    connection, client_addr = sock.accept()                             #Wait for connection
    print(client_addr,' connected')

    child_pid = os.fork()                                               #Fork

    if child_pid == 0:
        print('Forked Sucessfuly')
        thread_worker(connection, client_addr)                          #Child process
        break

    else:
        i = i+1
    
        
