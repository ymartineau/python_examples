'''
Created on 25 juil. 2014

@author: EMMANUELLE
'''
import threading

BUFFER_SIZE = 4096

class EchoThread(threading.Thread):
    '''
    classdocs
    '''
    def __init__(self, clientsocket):
        '''
        Constructor
        '''
        threading.Thread.__init__(self)
        self.clientsocket = clientsocket
        
        
    def run(self):
        while True:
            message = self.clientsocket.recv(BUFFER_SIZE)
            messageString = message.decode("utf-8")
            if messageString == "close":
                self.clientsocket.close()
                return
            self.clientsocket.send(message)