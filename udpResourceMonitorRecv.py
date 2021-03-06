#!/bin/python
# -*- coding: utf-8 -*-

"""
Ocki Bagus Pratama 135150207111060
"""

import platform
import socket
import sys


class UdpResourceMonitorRecv:
    def __init__(self):
        self.os_detect = platform.system()
        self.serverip = '0.0.0.0' if len(sys.argv) is not 2 else sys.argv[1]
        self.serverport = '8080' if len(sys.argv) is not 3 else sys.argv[2]

    def receive(self):
        udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sockadd = (self.serverip, int(self.serverport))
        udpsock.bind(sockadd)
        while 1:
            data, fromsockadd = udpsock.recvfrom(2048)
            print "From %s:%s\nCurrent Status:%s " % (fromsockadd[0], fromsockadd[1], data)

    def run(self):
        self.receive()


receiver = UdpResourceMonitorRecv()
receiver.run()