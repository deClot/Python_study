from twisted.internet import protocol, reactor, endpoints


class Echo(protocol.Protocol):
    def connectionMade(self):
        print("new client connected")

    # recieved data write back
    def dataReceived(self, data):
        self.transport.write(data)


class EchoFactory(protocol.Factory):
    # implement this method when new user comes
    def buildProtocol(self, addr):   # or protocol = Echo()
        return Echo()

# create point on whiche will be started server
endpoints.serverFromString(reactor, "tcp:1234").listen(EchoFactory())
reactor.run()


