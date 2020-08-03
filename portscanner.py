#!/bin/python3

import socket #allows to connect to IPV4
import sys #allows command line arguments
from datetime import datetime

#defining the target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #translates hostname to IPV4
else:
    print("invalid")
    print("Syntax : python3 scanner.py <IP>, no ip given") # if a wrong ip is given it will print this error
    sys.exit()

#add a pretty banner
print("""
_________________________________________________________________________________________________

██████╗  ██████╗ ██████╗ ████████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██████╔╝██║   ██║██████╔╝   ██║       ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██╔═══╝ ██║   ██║██╔══██╗   ██║       ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██║     ╚██████╔╝██║  ██║   ██║       ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
__________________________________________________________________________________________________
very slow, v1.0


""")

print("scanning..."+target)
print("time initiated", str(datetime.now()))#prints the initiated time the program was run
print('_' * 50)

try:
    for port in range(50,85): #port range 50 - 85
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) # if port is closed it will move on after 1 second
        result = s.connect_ex((target, port)) # returns an error indicator
        print("analysing port{}".format(port)) #prints the port it is checking if open
        if result == 0: # if a port is open the program will return a 0 assigned to that port, the if statement shows that is a 0 is returned it will print the open port
            print("port {} is open".format(port)) #prints a return value if the port is open 
        s.close()
except KeyboardInterrupt:
    print("\nExit due to interupt")
    sys.exit()

except socket.gaierror:
    sys.exit()

except socket.error:
    print("server is down")
    sys.exit()
