import json
import sys
import socket
import struct
import threading
import time
from subprocess import Popen, PIPE

MYPORT = 40100
MYGROUP_4 = '239.255.43.21'
MYTTL = 1 # Increase to reach other networks

'''def run_tester():
    location = "C:\\Users\\Eraslan\\PycharmProjects\\mdtProject1\\fwdSimpleMert-v2\\Tester\\ExternalInterfaceTester.exe"

    p= Popen(location,stdin=PIPE,stdout=PIPE,stderr=PIPE, encoding="UTF8")
    command='START\n'
    p.stdin.write(command)
    p.stdin.flush()  # important
    response=p.stdout.read()'''


def main():

    group = MYGROUP_4
    if "-s" in sys.argv[1:]:
        sender(group)
    else:
        receiver(group)


def sender(group):
    addrinfo = socket.getaddrinfo(group, None)[0]

    s = socket.socket(addrinfo[0], socket.SOCK_DGRAM)

    # Set Time-to-live (optional)
    ttl_bin = struct.pack('@i', MYTTL)
    if addrinfo[0] == socket.AF_INET: # IPv4
        s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl_bin)
    else:
        s.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_MULTICAST_HOPS, ttl_bin)

    while True:
        data = repr(time.time())
        s.sendto(data + '\0', (addrinfo[4][0], MYPORT))
        time.sleep(1)


def receiver(group):
    # Look up multicast group address in name server and find out IP version
    addrinfo = socket.getaddrinfo(group, None)[0]

    # Create a socket
    s = socket.socket(addrinfo[0], socket.SOCK_DGRAM)

    # Allow multiple copies of this program on one machine
    # (not strictly needed)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind it to the port
    s.bind(('', MYPORT))

    group_bin = socket.inet_pton(addrinfo[0], addrinfo[4][0])
    # Join group
    if addrinfo[0] == socket.AF_INET: # IPv4
        mreq = group_bin + struct.pack('=I', socket.INADDR_ANY)
        s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    else:
        mreq = group_bin + struct.pack('@I', 0)
        s.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_JOIN_GROUP, mreq)

    # Loop, printing any data we receive
    while True:
        data, sender = s.recvfrom(150000)
        while data[-1:] == '\0':
            data = data[:-1] # Strip trailing \0's

        data_string = str(data)
        data_string = eval(data_string)
        data_json = json.loads(data_string)
        print(json.dumps(data_json, indent=4))

        '''if list(data_json.keys())[0] == 'event_localization':
            #print(json.dumps(data_json['event_localization']['location'], indent = 4))
            print('Localisation')
        elif list(data_json.keys())[0] == 'event_detection':
            #print(json.dumps(data_json['event_detection']['location'], indent = 4))
            print('Detection')
        elif list(data_json.keys())[0] == 'node_info':
            #print(json.dumps(data_json['node_info']['node']['position'], indent = 4))
            print('Node_Info')
        else:
            pass'''


if __name__ == '__main__':
    main()



