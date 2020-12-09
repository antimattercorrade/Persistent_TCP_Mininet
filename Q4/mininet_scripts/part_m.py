from mininet.net import Mininet
from mininet.topo import Topo
from mininet.log import lg, info
from mininet.link import TCLink
from time import time, sleep
from mininet.util import custom, pmonitor
from mininet.node import Controller

import sys
sys.stdout.flush()

class CustomTopo( Topo ):
    
    #Build custom topo
    def build( self, **params ):
        hosts = []
        switches = []

        # Create switches and hosts
        hosts.append(self.addHost( 'S' ))
        hosts.append(self.addHost( 'H' ))
        hosts.append(self.addHost( 'I' ))
        hosts.append(self.addHost( 'J' ))
        hosts.append(self.addHost( 'K' ))
        hosts.append(self.addHost( 'L' ))
        hosts.append(self.addHost( 'M' ))
        hosts.append(self.addHost( 'N' ))
        hosts.append(self.addHost( 'O' ))

        #PART B
        hosts.append(self.addHost( 'S1' ))
        hosts.append(self.addHost( 'S2' ))
                  
        switches.append(self.addSwitch( 's1'  ))
        switches.append(self.addSwitch( 's2'  ))
        switches.append(self.addSwitch( 's3'  ))
        switches.append(self.addSwitch( 's4'  ))
        switches.append(self.addSwitch( 's5'  ))
        switches.append(self.addSwitch( 's6'  ))
        switches.append(self.addSwitch( 's7'  ))

        # Wire up switches
        self.addLink(switches[0], switches[1],cls=TCLink, bw = 1000)
        self.addLink(switches[0], switches[2],cls=TCLink, bw = 1000)
        self.addLink(switches[1], switches[3],cls=TCLink, bw = 500)
        self.addLink(switches[1], switches[4],cls=TCLink, bw = 500)
        self.addLink(switches[2], switches[5],cls=TCLink, bw = 500)
        self.addLink(switches[2], switches[6],cls=TCLink, bw = 500)

        self.addLink(switches[1], switches[2],cls=TCLink, bw = 500)

        # Wire up hosts
        self.addLink( hosts[ 0 ], switches[ 0 ],cls=TCLink, bw = 1000 )
        self.addLink( hosts[ 1 ], switches[ 3 ],cls=TCLink, bw = 250 )
        self.addLink( hosts[ 2 ], switches[ 3 ],cls=TCLink, bw = 250 )
        self.addLink( hosts[ 3 ], switches[ 4 ],cls=TCLink, bw = 250 )
        self.addLink( hosts[ 4 ], switches[ 4 ],cls=TCLink, bw = 250 )
        self.addLink( hosts[ 5 ], switches[ 5 ],cls=TCLink, bw = 250 )
        self.addLink( hosts[ 6 ], switches[ 5 ],cls=TCLink, bw = 250 )
        self.addLink( hosts[ 7 ], switches[ 6 ],cls=TCLink, bw = 250 )
        self.addLink( hosts[ 8 ], switches[ 6 ],cls=TCLink, bw = 250 )

        #PART B
        self.addLink( hosts[ 9 ], switches[ 5 ],cls=TCLink, bw = 1000 )
        self.addLink( hosts[ 10 ], switches[ 6 ],cls=TCLink, bw = 1000 )


def main():

    topo = CustomTopo()

    net = Mininet( topo=topo)

    net.start()
    
    #Get hosts
    S = net.get('S')
    H = net.get('H')
    I = net.get('I')
    J = net.get('J')
    K = net.get('K')
    L = net.get('L')
    M = net.get('M')
    N = net.get('N')
    O = net.get('O')

    S1 = net.get('S1')
    S2 = net.get('S2')

    popens = {}

    #Start Servers
    popens[S] = S.popen('python3 -u ../server/tcp_server_sc_thread.py %s & ' %S.IP())
    popens[S1] = S1.popen('python3 -u ../server/tcp_server_sc_thread.py %s & ' %S1.IP())
    popens[S2] = S2.popen('python3 -u ../server/tcp_server_sc_thread.py %s & ' %S2.IP())

    #PART A

    # sleep(0.25)
    # print(H.cmd('python3 ../client/tcp_client.py 1 %s' %S.IP()))
    # print(I.cmd('python3 ../client/tcp_client.py 1 %s' %S.IP()))
    # print(J.cmd('python3 ../client/tcp_client.py 1 %s' %S1.IP()))
    # print(K.cmd('python3 ../client/tcp_client.py 1 %s' %S2.IP()))
    
    #PART B

    print(H.cmd('python3 ../client/tcp_client.py 1 %s' %S.IP()))
    print(K.cmd('python3 ../client/tcp_client.py 1 %s' %S.IP()))
    print(M.cmd('python3 ../client/tcp_client.py 1 %s' %S1.IP()))
    print(N.cmd('python3 ../client/tcp_client.py 1 %s' %S2.IP()))

    #Set timeout for pmonitor
    timeout = time() + 15

    for host, line in pmonitor(popens):
        if host:
            info( "<%s>: %s" % ( host.name, line ) )
        if time() > timeout:
            break
    
    net.stop()

    
if __name__ == '__main__':
    lg.setLogLevel( 'info' )
    main()