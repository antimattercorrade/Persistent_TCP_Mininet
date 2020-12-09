## Fork and Thread Model

- To run the client, run `python3 tcp_client.py`. It will ask for the number of books to download from the server. Then it will ask for a number corresponding to which will be the book to download. 

- To run the fork model server, run `python3 tcp_server_sc_fork.py` or to run the thread model server, run `python3 tcp_server_sc_thread.py`.

- After the input is received, the client will connect to the server and download the respective books in the "files_received" folder.

- The buffer size in the client and server can be set by changing the value corresponding to variable "BUFFER_SIZE" in "tcp_client.py" and "tcp_server_sc_thread.py" or "tcp_server_sc_fork.py" files.

- The client displays the connection setup time, calculated throughput and download time for each file as well as the aggregate throughput and total download time.

- To run the non persistent clients concurrently, run `./run_concurrent.sh` in bash or run `bash run_concurrent.sh` in any other terminal. It will start all the clients in background and print the output of all the clients. 
