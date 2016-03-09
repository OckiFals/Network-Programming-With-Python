#!/bin/python
# -*- coding: utf-8 -*-

"""
Ocki Bagus Pratama 135150207111060
"""

import os
import platform
import sys
import socket
import threading

import time


class UdpResourceMonitorSend:
    def __init__(self):
        self.os_detect = platform.system()
        self.targetip = '127.0.0.1' if len(sys.argv) is not 2 else sys.argv[1]
        self.targetport = '8080' if len(sys.argv) is not 3 else sys.argv[2]
        self.counter = 0

    def getresourceexecutor(self):
        if 'Linux' == self.os_detect:
            return {
                'message': 'Linux Ahoi!',
                'executor': {
                    'cpu': 'uptime',
                    'ram': 'free'
                }
            }
        elif 'Windows' == self.os_detect:
            return {
                'message': 'Noob!',
                'executor': {
                    'cpu': 'wmic cpu get loadpercentage',
                    'ram': 'wmic os get freephysicalmemory'
                }
            }

    def getresource(self):
        executor = self.getresourceexecutor()
        return " %s\n \t Captured: @%s\n \t CPU Status: \n \t    %s \t Memory Status: \n %s" % (
            executor['message'],
            time.strftime("%H:%M:%S", time.localtime()),
            os.popen(executor['executor']['cpu']).read(),
            os.popen(executor['executor']['ram']).read()
        )

    def send(self):
        udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            udpsock.sendto(self.getresource(), (self.targetip, int(self.targetport)))
        except KeyboardInterrupt:
            udpsock.close()
            print 'Interrupted'
            sys.exit(0)

    def run(self):
        threading.Timer(5.0, self.run).start()
        self.send()
        self.counter += 1
        print self.counter


sender = UdpResourceMonitorSend()
sender.run()
