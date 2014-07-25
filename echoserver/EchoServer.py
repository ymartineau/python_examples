import socket
from echoserver.EchoThread import EchoThread
class EchoServer:

    def __init__(self):
        print("instanciating EchoServer")

    def start(self):
        print("starting EchoServer")
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind(("", 1234))
        serversocket.listen(5)
        while True:
            (clientsocket, address) = serversocket.accept()
            echoThread = EchoThread(clientsocket)
            echoThread.start()
# TODO