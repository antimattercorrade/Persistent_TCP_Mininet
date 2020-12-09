from time import sleep, time
from mininet.cli import CLI
from mininet.log import lg, info
from mininet.topo import SingleSwitchTopo
from mininet.net import Mininet
from mininet.util import custom, pmonitor

def main():
    lg.setLogLevel( 'info')
    topo = SingleSwitchTopo(6)

    #Create topology
    net = Mininet(topo=topo)

    net.start()

    #Get hosts
    h1 = net.get('h1')
    h2 = net.get('h2')
    h3 = net.get('h3')
    h4 = net.get('h4')
    h5 = net.get('h5')
    h6 = net.get('h6')

    popens = {}

    #Start Server
    popens[h1] = h1.popen('python3 -u ../server/tcp_server_sc_thread.py %s & ' %h1.IP())

    #Start Clients
    popens[h2] = h2.popen('python3 ../client/tcp_client.py 1 %s & ' %h1.IP())
    popens[h3] = h3.popen('python3 ../client/tcp_client.py 2 %s & ' %h1.IP())
    popens[h4] = h4.popen('python3 ../client/tcp_client.py 3 %s & ' %h1.IP())
    popens[h5] = h5.popen('python3 ../client/tcp_client.py 4 %s & ' %h1.IP())
    popens[h6] = h6.popen('python3 ../client/tcp_client.py 5 %s & ' %h1.IP())

    #Set timeout for pmonitor
    timeout = time() + 5

    for host, line in pmonitor(popens):
        if host:
            info( "<%s>: %s" % ( host.name, line ) )
        if time() > timeout:
            break

    net.stop()

main()