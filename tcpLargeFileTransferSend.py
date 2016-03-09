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
        self.sendfile()


sender = TcpLargeFileTransferSend()
sender.run()
