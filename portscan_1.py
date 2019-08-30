#!/usr/bin/python

# allows us to connect to target ports
import socket

# creates socket object
# socket.AF_INET = ipv4 address
# socket.SOCK_STREAM = use TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ip address of target
host = "10.1.10.6"

# port to be scanned
port = 80


def port_scanner(port):
    # if function returns an error
    if sock.connect_ex((host, port)):
        print "Port %d is closed." % (port)
    else:
        print "Port %d is open" % (port)


port_scanner(port)
