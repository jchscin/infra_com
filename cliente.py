#!/usr/bin/python2.7
#teste

import socket
import os

prompt = ">> "
porta = 2529
class Cliente:

    def __init__ (self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(('localhost', porta))

    def comunica (self, msg):
        self.s.send(msg)
        self.msg_r = self.s.recv(100)
#       print(msg_r)

    def chegada (self):
        self.comunica("oi, estou chegando...")
        msg = raw_input(self.msg_r + "... (s ou n)\n" +  prompt)
        self.comunica(msg)
        self.s.send("show...")
        print(self.msg_r)
        if msg == "n" :
            msg = raw_input(self.s.recv(100)+ "\n" + prompt)
            self.comunica(msg)
            print(self.msg_r+prompt)
            self.s.send("OK")
        else:
            msg = raw_input(self.s.recv(100) + "\n" + prompt)
            self.comunica(msg)            
    
    def saida (self):
        self.s.close()

    def comando (self):
        ##o servidor esta esperando umas mensagem / / o comando ##
        while 1:
            msg = raw_input()
            if msg != "q":
                self.s.send(msg)
                print("enviado")
            else:
                print("adeus: ")
                self.s.send(msg)
                break

##s.send(cmd)
##print s.recv(100)
os.system("clear")
cliente = Cliente()
cliente.chegada()
cliente.comando()
cliente.saida()
