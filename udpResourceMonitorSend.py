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
                'executor': 'uptime; free'
            }
        elif 'Windows' == self.os_detect:
            return {
                'message': 'Noob!',
                'executor': 'Tasklist.exe!'
            }

    def getresource(self):
        executor = self.getresourceexecutor()
        return "%s \n %s" % (executor['message'], os.popen(executor['executor']).read())

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