#########################################
#Import libraries
#########################################

import socket
import os
import time 
import sys 

#########################################
#Declaring Connection Variables
#########################################

file_number = int(sys.argv[1])          #Get file number to download from prompt
IP = sys.argv[2]                        #Get IP from prompt

BUFFER_SIZE = 1024                      #Buffer Size for receiving file in chunks
HOST = IP                               #Server IP
PORT = 12345                            #Server Port Number

#########################################
#Initializing TCP Socket
#########################################

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

if(file_number == 1):
    file_name = "../novel/Atlas Shrugged.txt"
elif(file_number == 2):
    file_name = "../novel/Don Quixote.txt"
elif(file_number == 3):
    file_name = "../novel/Shogun.txt"
elif(file_number == 4):
    file_name = "../novel/The Stand.txt"
elif(file_number == 5):
    file_name = "../novel/War and Peace.txt"

file = file_name.split('/')
name = file[2].split('.')

print('Connecting to ',HOST)
sock.connect((HOST, PORT))                                        #Connect to server
print('Connected')

start = time.time()                                               #Start timer

sock.send(file_name.encode())                                     #Send filename

res = sock.recv(100)                                              #Receive ack
sock.send(b'sent')                                                #Send ack

file_name = "files_received/" + name[0] + "+Protocol=TCP" + "+" + str(os.getpid()) + "." + name[1]

with open(file_name, 'wb') as f:                                  #Open file in write mode
    print('Receiving Data')
    while True:
        byte = sock.recv(BUFFER_SIZE)                             #Recieve data from server
    
        if not byte or byte == b'EOF':
            break

        f.write(byte)                                             #Write to file
        sock.send(b'sent')

f.close()
sock.close()                                                      #Close connection to the server

end = time.time()                                                 #End timer           
print(f"Time taken to download: {end - start} sec")               #Print download time

file_stat = os.stat(file_name)                                    #Get downloaded file size
file_size = file_stat.st_size

throughput = round((file_size*0.001)/(end - start), 3)            #Caculate throughput
print("Downloaded ",file_name)
print("Throughput: ",throughput,"kB/s")
