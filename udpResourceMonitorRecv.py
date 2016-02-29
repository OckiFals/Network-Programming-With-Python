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
        self.serverip = '127.0.0.1' if len(sys.argv) is not 2 else sys.argv[1]
        self.serverport = '8080' if len(sys.argv) is not 3 else sys.argv[2]

    def receive(self):
        udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sockadd = (self.serverip, int(self.serverport))
        udpsock.bind(sockadd)
        while 1:
            data, fromsockadd = udpsock.recvfrom(2048)
            print 'From: ', fromsockadd, '\n Current status:', data

    def run(self):
        self.receive()


receiver = UdpResourceMonitorRecv()
receiver.run()