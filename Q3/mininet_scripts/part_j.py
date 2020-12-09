from time import sleep, time
from mininet.log import lg, info
from mininet.net import Mininet
from mininet.util import custom, pmonitor
from mininet.link import TCLink
from mininet.topo import Topo

class LinearTopo( Topo ):
    
    #Build custom topo
    def build( self, **params ):
        hosts = []
        switches = []

        # Create switches and hosts
        hosts.append(self.addHost( 'h1' ))
        hosts.append(self.addHost( 'h2' ))
                  
        switches.append(self.addSwitch( 's1'  ))
        switches.append(self.addSwitch( 's2'  ))
        switches.append(self.addSwitch( 's3'  ))
        switches.append(self.addSwitch( 's4'  ))
        switches.append(self.addSwitch( 's5'  ))
        switches.append(self.addSwitch( 's6'  ))
        switches.append(self.addSwitch( 's7'  ))
        switches.append(self.addSwitch( 's8'  ))

        #Wire up switches
        self.addLink( switches[ 0 ], switches[ 1 ],cls=TCLink, bw = 1000)
        self.addLink( switches[ 1 ], switches[ 2 ],cls=TCLink, bw = 1000)
        self.addLink( switches[ 2 ], switches[ 3 ],cls=TCLink, bw = 1000)
        self.addLink( switches[ 3 ], switches[ 4 ],cls=TCLink, bw = 1000)
        self.addLink( switches[ 4 ], switches[ 5 ],cls=TCLink, bw = 1000)
        self.addLink( switches[ 5 ], switches[ 6 ],cls=TCLink, bw = 1000)
        self.addLink( switches[ 6 ], switches[ 7 ],cls=TCLink, bw = 1000)

        # Wire up hosts
        self.addLink( hosts[ 0 ], switches[ 0 ],cls=TCLink, bw = 1000)
        self.addLink( hosts[ 1 ], switches[ 7 ],cls=TCLink, bw = 1000)


def main():
    lg.setLogLevel( 'info')
    topo = LinearTopo()

    net = Mininet(topo=topo)

    net.start()

    #Get hosts
    h1 = net.get('h1')
    h2 = net.get('h2')

    popens = {}

    #Start Server
    popens[h1] = h1.popen('python3 ../server/tcp_server_sc_thread.py %s & ' %h1.IP())

    #Start Client
    print(h2.cmd('python3 ../client/tcp_client.py 3 %s ' %h1.IP()))

    net.stop()

main()