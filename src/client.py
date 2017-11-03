#!/usr/bin/env python
 
import socket
 
def recv_until(conn, str):
    buf = ''
    while not str in buf:
        buf += conn.recv(1)
    return buf
 
def getValidSubnet(host):
    return host+'/0'
 
def countHosts(subnet):
    mask = int(subnet.partition('/')[2])
    return str(2**(32-mask))
 
def isSubnetValid(subnet, host):
    a1 = int(subnet.partition('.')[0])
    ar1 = subnet.partition('.')[2]
    a2 = int(ar1.partition('.')[0])
    ar2 = ar1.partition('.')[2]
    a3 = int(ar2.partition('.')[0])
    ar3 = ar2.partition('.')[2]
    a4 = int(ar3.partition('/')[0])
    a = ''
    a = a + '{0:08b}'.format(a1)  + '{0:08b}'.format(a2)  + '{0:08b}'.format(a3)  + '{0:08b}'.format(a4)
 
    b1 = int(host.partition('.')[0])
    br1 = host.partition('.')[2]
    b2 = int(br1.partition('.')[0])
    br2 = br1.partition('.')[2]
    b3 = int(br2.partition('.')[0])
    b4 = int(br2.partition('.')[2])
    b = ''
    b = b + '{0:08b}'.format(b1)  + '{0:08b}'.format(b2)  + '{0:08b}'.format(b3)  + '{0:08b}'.format(b4)
 
    i = int(subnet.partition('/')[2])
    if (a[:i] == b[:i]) :
            return 'T'
    else:
            return 'F'
       
   
   
   
TCP_IP = 'hmif.cf'
TCP_PORT = 9999
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
 
data = recv_until(s, 'NIM: ')
nim = raw_input(data)
s.send(nim + '\n')
 
data = recv_until(s, 'Verify NIM: ')
nim = raw_input(data)
s.send(nim + '\n')
 
print recv_until(s, '\n')[:-1]
 
# Phase 1
for i in range(100):
    recv_until(s, 'Host: ')
    host = recv_until(s, '\n')[:-1]
    recv_until(s, 'Subnet: ')
    s.send(getValidSubnet(host) + '\n')
print recv_until(s, '\n')[:-1]
 
# Phase 2
for i in range(100):
    recv_until(s, 'Subnet: ')
    subnet = recv_until(s, '\n')[:-1]
    recv_until(s, 'Number of Hosts: ')
    s.send(countHosts(subnet) + '\n')
print recv_until(s, '\n')[:-1]
 
# Phase 3
for i in range(100):
    recv_until(s, 'Subnet: ')
    subnet = recv_until(s, '\n')[:-1]
    recv_until(s, 'Host: ')
    host = recv_until(s, '\n')[:-1]
    s.send(isSubnetValid(subnet, host) + '\n')
print recv_until(s, '\n')[:-1]
 
s.close()
