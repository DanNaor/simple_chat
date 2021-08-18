#!/bin/python3
from socket import socket ,AF_INET,SOCK_STREAM
import logging
from threading import Thread



class ChatClient:
    def __init__(self,host,port):
        self.logger=self._setup_logger()
        self.sock=self._setup_socket(host,port)
        thread= Thread(target=self.send_message)
        thread.deamon=True
        thread.start()

        while True:
            data=self.sock.recv(4096)
            if not data: 
                break
            self.logger.info(data.decode())
            
    def send_message(self):
        while True:
            user_message= input()
            self.sock.send(user_message.encode('utf-8','backslashreplace'))


    @staticmethod
    def _setup_socket(host,port):
        sock=socket(AF_INET,SOCK_STREAM)
        sock.connect((host,port))
        return sock
    @staticmethod
    def _setup_logger():
        logger=logging.getLogger('chat_client')
        logger.addHandler(logging.StreamHandler())
        logger.setLevel(logging.DEBUG)
        return logger
if __name__ == "__main__":
    from .settings import SERVER_PORT, SERVER_HOST
    client=ChatClient(SERVER_HOST,SERVER_PORT)
##s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##s.connect(("server", 5005))
##msg2="X"
##while(msg2!="quit"):
##    msg = input("type...")
##    s.sendall(bytes(msg,"utf-8"))
##    data= s.recv(2000)
##    print(data.decode())
#    msg2= input(" enter quit to continue")
