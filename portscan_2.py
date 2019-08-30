#!/usr/bin/python

# allows us to connect to target ports
import socket

# creates socket object
# socket.AF_INET = ipv4 address
# socket.SOCK_STREAM = use TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# times out if response takes longer than two seconds
socket.setdefaulttimeout(2)

# ip address of target
host = raw_input("[+] Enter the host to scan: ")

# port to be scanned
port = int(raw_input("[+] Enter the port to scan: "))


def port_scanner(port):
    # if function returns an error
    if sock.connect_ex((host, port)):
        print "Port %d is closed." % (port)
    else:
        print "Port %d is open" % (port)


port_scanner(port)
