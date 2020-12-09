#########################################
#Import libraries
#########################################

import socket
import os
from time import time,sleep
import sys
from threading import Thread

#########################################
#Declaring Connection Variables
#########################################

IP = sys.argv[1]                                    #Get IP from prompt

BUFFER_SIZE = 1024                                  #Buffer Size for receiving file in chunks
BUFFER_FILENAME = 1024                              #Buffer size for receiving file name
SERVER_IP = IP                                      #Server IP
SERVER_PORT = 12345                                 #Server Port Number

#########################################
#Initializing UDP Socket
#########################################
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Starting server on port ',SERVER_PORT)

sock.bind((SERVER_IP, SERVER_PORT))

sock.listen(1)

class thread_worker(Thread):
    def __init__(self, connection):
        Thread.__init__(self)
        self.connection = connection
    
    def run(self):
        connection = self.connection
        
        file_name = connection.recv(BUFFER_FILENAME).decode()                   #Receive file name
 
        while (file_name):                                                      #Start timer

            fd = open(file_name, 'rb')                                          #Open file in read mode
            connection.send(b'sent')                                            #Send ack
            connection.recv(100)                                                #Receive ack
            
            buf = fd.read(BUFFER_SIZE)                                          #Read from file equal to buffer size

            print('Sending Data')

            while(buf): 
                connection.send(buf)                                            #Send data to the client
                connection.recv(100)
                buf = fd.read(BUFFER_SIZE)

            fd.close()                                                          #Close file
            
            connection.send(b'EOF')

            file_name = connection.recv(BUFFER_FILENAME)              #Receive file name
        
        connection.close()
        exit()

while True:
    print('Waiting for connection') 
    connection,client_addr = sock.accept()
    print(client_addr,' connected')

    new_thread = thread_worker(connection)
    new_thread.start()
