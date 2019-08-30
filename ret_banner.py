#!/usr/bin/python

import socket


# returns banner from given ip and port
def return_banner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024).strip("\n")
        return banner
    except:
        return


def main():
    ip = raw_input("[*] Enter target IP: ")

    for port in range(1,1000):
        banner = return_banner(ip, port)
        if banner:
            print "[+] {}:{} - {}".format(ip, port, banner)


main()

