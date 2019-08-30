#!/usr/bin/python3

# import modules
import socket
import os
import sys
from termcolor import colored


# returns a banner from the target host and port
def ret_banner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner.decode('utf-8').strip("\n")
    except:
        return


# compares banner to list of vulnerabilities
def check_vulns(banner, filename, ip, port):

    # opens file for reading
    f = open(filename, "r")

    # for each line in file
    for line in f.readlines():
        
        # strips newline char from banner
        # if line from file matches banner
        if line.strip("\n") in banner:
            print(colored('[!] {}/{} - Server is vulnerable: {}'.format(ip, port, banner), "red"))


def main():
    # if two arguments are passed in
    if len(sys.argv) == 2:
        filename = sys.argv[1]

        # if file cannot be found
        if not os.path.isfile(filename):
            print('[-] File does not exist!')
            exit(0)

        # if user lacks file permissions
        if not os.access(filename, os.R_OK):
            print('[-] Access Denied.')

    # if two arguments are not passed in
    else:
        print('[-] Usage: ' + str(sys.argv[0]) + ' <vuln filename>')
        exit(0) 

    ip = input("Please enter the host to be scanned: ")
    
    ports = input("Please enter the range of ports to be scanned ([start port]-[end port]): ").split("-")
    
    # for port in given range
    for port in range(int(ports[0]), int(ports[1])):
        banner = ret_banner(ip, port)
        
        # if banner is returned
        if banner:
            print(colored('[+] {}/{} - {}'.format(ip, port, banner), "green"))

            # compare banner to list in vulnfile
            check_vulns(banner, filename, ip, port)

main()
