#!/bin/python
# -*- coding: utf-8 -*-

"""
Ocki Bagus Pratama 135150207111060
"""

import sys
import socket


class TcpLargeFileTransferRecv:
    def __init__(self):
        self.targetip = '127.0.0.1' if len(sys.argv) is not 2 else sys.argv[1]
        self.targetport = '8080' if len(sys.argv) is not 3 else sys.argv[2]

    def createconnection(self):
        tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpsock.bind(('', int(self.targetport)))
        return tcpsock

    def receivefile(self):
        sock = self.createconnection()
        sock.listen(1)
        f = open('Fedora-Live-Workstation-x86_64-23-10 2.iso', 'w')
        while 1:
            sockconn, fromaddr = sock.accept()
            l = sockconn.recv(1024)
            while l:
                print "Receiving..."
                f.write(l)
                l = sockconn.recv(1024)
            f.close()
            sockconn.close()

    def run(self):
        self.receivefile()


sender = TcpLargeFileTransferRecv()
sender.run()
