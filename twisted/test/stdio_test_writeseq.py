# -*- test-case-name: twisted.test.test_stdio.StandardInputOutputTestCase.testWriteSequence -*-
# Copyright (c) 2006 Twisted Matrix Laboratories.
# See LICENSE for details.

"""
Main program for the child process run by
L{twisted.test.test_stdio.StandardInputOutputTestCase.testWriteSequence} to test that
ITransport.writeSequence() works for process transports.
"""

from twisted.internet import stdio, protocol, reactor

class WriteSequenceChild(protocol.Protocol):
    def connectionMade(self):
        self.transport.writeSequence(list('ok!'))
        self.transport.loseConnection()


    def connectionLost(self, reason):
        reactor.stop()


if __name__ == '__main__':
    stdio.StandardIO(WriteSequenceChild())
    reactor.run()