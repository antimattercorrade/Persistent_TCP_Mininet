#########################################
#Import libraries
#########################################
import socket
import os
import time

#########################################
#Declaring Connection Variables
#########################################
BUFFER_SIZE = 1024                      #Buffer Size for receiving file in chunks
HOST = 'localhost'                      #Server IP
PORT = 12345                            #Server Port Number

#########################################
#Input Filename to Download
#########################################
print("Enter the number of books to download (1-5):")
size = int(input())

file_number = []

for i in range (0,size):
    print("Enter the corresponding number to download book:")
    print("1. Atlas Shrugged by Ayn Rand")
    print("2. Don Quixote by Miguel de Cervantes")
    print("3. Shogun by James Clavell")
    print("4. The Stand by Stephen King")
    print("5. War and Peace by Leo Tolstoy")

    file_number.append(int(input()))

#########################################
#Initializing UDP Socket
#########################################

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#########################################
#Uncomment the line below for disabling Nagle's Algortihm
#########################################

# sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

#########################################
#Uncomment the line below for disabling Delayed Ack
#########################################

# sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_QUICKACK, 1)

try:
    print('Connecting to ',HOST)
    conn_setup = time.time()
    sock.connect((HOST, PORT))                                        #Connect to server
    conn_end = time.time()
    print('Connected')

    total_start = time.time()
    agg_throughput = 0

    for i in range (0,size):

        if(file_number[i] == 1):
            file_name = "../novel/Atlas Shrugged.txt"
        elif(file_number[i] == 2):
            file_name = "../novel/Don Quixote.txt"
        elif(file_number[i] == 3):
            file_name = "../novel/Shogun.txt"
        elif(file_number[i] == 4):
            file_name = "../novel/The Stand.txt"
        elif(file_number[i] == 5):
            file_name = "../novel/War and Peace.txt"

        file = file_name.split('/')
        name = file[2].split('.')

        start = time.time()                                               #Start timer

        sock.send(file_name.encode())                                    #Send filename

        res = sock.recv(100)
        sock.send(b'sent')

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

        end = time.time()                                                 #End timer           
        print(f"Time taken to download: {end - start} sec")               #Print download time

        file_stat = os.stat(file_name)                                    #Get downloaded file size
        file_size = file_stat.st_size

        throughput = round((file_size*0.001)/(end - start), 3)            #Caculate throughput
        agg_throughput += throughput
        print("Downloaded ",file_name)
        print("Throughput: ",throughput,"kB/s")

    total_end = time.time()
    print(f"Total Time taken to download all files: {total_end - total_start} sec")       #Print download time

    print("Aggregate Throughput: ",agg_throughput,"kB/s")

    print(f"Time taken to setup connection: {conn_end - conn_setup} sec")                 #Print connection setup time
    
    
finally:
    sock.close()                                                      #Close connection to the server
    
    
