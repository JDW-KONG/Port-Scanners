#!/usr/bin/python3

# allows us to connect to target ports
import socket

# allows us to add colors to our script
from termcolor import colored

# creates socket object
# socket.AF_INET = ipv4 address
# socket.SOCK_STREAM = use TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# times out if response takes longer than two seconds
socket.setdefaulttimeout(2)

# ip address of target
host = input("[+] Enter the host to scan: ")


def port_scanner(port):
    # if function returns an error
    if sock.connect_ex((host, port)):
        print(colored("[-] Port %d is closed." % (port), "red"))
        
    else:
        print(colored("[+] Port %d is open." % (port), "green"))


# scans first 100 ports
for port in range(1, 1000):
    port_scanner(port)
