#!/bin/python3
from socket import socket ,AF_INET,SOCK_STREAM
import logging
from concurrent.futures import ThreadPoolExecutor
class ChatServer:
    def __init__(self,host,port):
        self.logger=self._setup_logger(self)
        self.sock=self._setup_socket(host,port)  
        self.connections=[]

    def run (self):
        self.logger.info("chat server is running")

        with ThreadPoolExecutor() as executer:
            while True:
                #block and wait for incoming connections
                conn,addr= self.sock.accept()
                self.logger.debug(f"new connection:{addr}") 
            
                self.connections.append(conn)
                self.logger.debug(f"connections:{self.connections}")

                executer.submit(self.relay_messages,conn,addr)    


    def relay_messages(self,conn,host):
        while True:
            data= conn.recv(4096)
            
            for connection in self.connections:
                connection.send(data)

            if not data:
                self.logger.warning("no data exiting")
                break


    @staticmethod
    def _setup_socket(host,port):
        sock=socket(AF_INET,SOCK_STREAM)
        sock.bind((host,port))
        sock.listen()
        return sock

    @staticmethod
    def _setup_logger(self):
        logger=logging.getLogger("chat server")
        logger.addHandler(logging.StreamHandler())
        logger.setLevel(logging.DEBUG)
        return logger
if __name__ == "__main__":
    from composetest.settings import SERVER_PORT, SERVER_HOST
    server=ChatServer(SERVER_HOST,SERVER_PORT)
    server.run()
#def is_added(addrs,clientsocket):
#    for x in addrs:
#        if x==clientsocket:
#            return False
#    return True
#
#def get_ip(socket):
#    hostname =socket.gethostname()
#    return socket.gethostbyname(hostname)
#
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind((socket.gethostname(), 5005))
#s.listen(5)
#addrs=[]
#while True:
#    # now our endpoint knows about the OTHER endpoint.
#    clientsocket, address = s.accept()
#    print(f"Connection from {address} has been established.")
#    msg=clientsocket.recv(1024)
#    if len(addrs)==0:
#        addrs.append(clientsocket)
#    else:
#       if is_added(addrs,clientsocket):
#            addrs.append(clientsocket)
#    for x in addrs:
#        if x!=clientsocket:
#            x.send(msg)
