#!/usr/bin/python

from socket import *

def SendMagicPacket(ip,mac):
    packet = [255,255,255,255,255,255]
    packet_bytes = bytes(packet)
    mac = mac.replace("\n","")
    mac = mac.strip()
    mac = mac.split('-')
    mac = mac * 16

    for i in range(0,len(mac)) :
        mac[i] = int(mac[i],16)
    mac_bytes = bytes(mac)

    data = packet_bytes + mac_bytes

    subnet = ip.split('.')
    subnet[3] = "255"

    network = '.'.join(subnet)

    s = socket(AF_INET,SOCK_DGRAM)
    address1 = (network,9)

    ret =s.sendto(data,address1)
    address2 = (ip,9)
    s.sendto(data,address2)
    s.close()
    return ret

