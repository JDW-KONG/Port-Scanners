#!/usr/bin/python3

# allows us to connect to target ports
from socket import *

# allows us to add colors to our script
from termcolor import colored

# allows us to create help options for the user
import optparse

# allows us to create multiple threads
from threading import *


# connects to target host and port
def conn_scan(targHost, targPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((targHost, targPort))
        print(colored('[+] %d/tcp: Open' % (targPort), "green"))
    except:
        print(colored('[-] %d/tcp: Closed' % (targPort), "red"))
    finally:
        sock.close()


# scans target ports at target host
def port_scanner(targHost, targPorts):
    try:
        # converts hostname to ip
        targIP = gethostbyname(targHost)
    except:
        print('Unknown Host %s' %targHost)

    try:
        # converts ip to hostname
        targName = gethostbyaddr(targIP)
        print(colored('[?] Scan Results for: ' + targName[0], "yellow"))
    except:
        print(colored('[?] Scan Results for: ' + targIP, "yellow"))
    setdefaulttimeout(1)

    # for each port
    for targPort in targPorts:
        # create a new thread and run conn_scan
        t = Thread(target=conn_scan, args=(targHost, int(targPort)))
        t.start()


# define help options and program usage
def main():
    parser = optparse.OptionParser("Usage of program: " + "-H <target host> -p <target ports>")
    parser.add_option("-H", dest="targHost", type="string", help="specify target host")
    parser.add_option("-p", dest="targPorts", type="string", help="specify target ports separated by comma")
    (options, args) = parser.parse_args()
    targHost = options.targHost
    targPorts = str(options.targPorts).split(",")

    if (targHost == None) | (targPorts[0] == None):
        print(colored(parser.usage, "yellow"))
        exit(0)

    port_scanner(targHost, targPorts)


if __name__ == '__main__':
    main()
