# Persistent TCP Transfer over Mininet ⭐

Implementation of persistent TCP connection using python. The folders contain persistent TCP clients and servers using thread or fork models for multiple connection requests. The servers and clients are run on mininet using the scripts provided on custom or pre-defined topology of mininet.

## Codebase Directory Architecture: 📁

```
persistent_tcp_mininet
├─ Fork_and_Thread
│  ├─ Client
│  │  ├─ files_received
│  │  ├─ run_concurrent.sh
│  │  ├─ tcp_client.py
│  │  └─ tcp_client_np.py
│  ├─ novel
│  │  ├─ Atlas Shrugged.txt
│  │  ├─ Don Quixote.txt
│  │  ├─ Shogun.txt
│  │  ├─ The Stand.txt
│  │  └─ War and Peace.txt
│  ├─ README.md
│  └─ Server
│     ├─ tcp_server_sc_fork.py
│     └─ tcp_server_sc_thread.py
├─ Mininet_Custom_Topology
│  ├─ client
│  │  └─ tcp_client.py
│  ├─ mininet_scripts
│  │  ├─ part_k.py
│  │  ├─ part_l.py
│  │  └─ part_m.py
│  ├─ novel
│  │  ├─ Atlas Shrugged.txt
│  │  ├─ Don Quixote.txt
│  │  ├─ Shogun.txt
│  │  ├─ The Stand.txt
│  │  └─ War and Peace.txt
│  ├─ README.md
│  └─ server
│     └─ tcp_server_sc_thread.py
├─ Persistent_TCP
│  ├─ Client
│  │  ├─ files_received
│  │  └─ tcp_client.py
│  ├─ novel
│  │  ├─ Atlas Shrugged.txt
│  │  ├─ Don Quixote.txt
│  │  ├─ Shogun.txt
│  │  ├─ The Stand.txt
│  │  └─ War and Peace.txt
│  ├─ README.md
│  └─ Server
│     └─ tcp_server.py
├─ README.md
└─ TCP_Mininet
   ├─ client
   │  └─ tcp_client.py
   ├─ mininet_scripts
   │  ├─ part_e.py
   │  ├─ part_f.py
   │  ├─ part_g.py
   │  ├─ part_h.py
   │  ├─ part_i.py
   │  └─ part_j.py
   ├─ novel
   │  ├─ Atlas Shrugged.txt
   │  ├─ Don Quixote.txt
   │  ├─ Shogun.txt
   │  ├─ The Stand.txt
   │  └─ War and Peace.txt
   ├─ README.md
   └─ server
      └─ tcp_server_sc_thread.py

```

## Features checklist ✅

```
✅ File transfer over Persistent TCP
✅ Multithreaded Server using forking and threading 
✅ Multirequest client 
✅ Mininet scripts for running the servers and clients. 

```

## Instructions to Run :runner:

- Each folder contains the specific instructions to run the servers and clients.
