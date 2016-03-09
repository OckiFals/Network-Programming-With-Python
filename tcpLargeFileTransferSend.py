#!/bin/python
# -*- coding: utf-8 -*-

"""
Ocki Bagus Pratama 135150207111060
"""

import sys
import socket


class TcpLargeFileTransferSend:
    def __init__(self):
        self.targetip = '127.0.0.1' if len(sys.argv) is not 2 else sys.argv[1]
        self.targetport = '8080' if len(sys.argv) is not 3 else sys.argv[2]
        self.filetotransport = 'Fedora-Live-Workstation-x86_64-23-10.iso'

    def createconnection(self):
        tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpsock.connect((self.targetip, int(self.targetport)))
        return tcpsock

    def sendfile(self):
        sock = self.createconnection()

        with open('Fedora-Live-Workstation-x86_64-23-10.iso', 'rb') as infile:
            print "Opening file"
            for line in infile:
                sock.send(line)

        print "Done Sending"
        sock.shutdown(socket.SHUT_WR)
        print sock.recv(1024)
        sock.close()

    def run(self):
        with open(self.filetotransport, 'rb') as infile:
            infile.seek(0, 2)
            size = infile.tell()

        if 1024000 > size:
            raise Exception('file must larger than 1GB')

        self.sendfile()


sender = TcpLargeFileTransferSend()
sender.run()
