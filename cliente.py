#!/usr/bin/python2.7
#teste

import socket
import os

prompt = ">> "
porta = 25252
class Cliente:

    def __init__ (self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(('localhost', porta))

    def comunica (self, msg):
        self.s.send(msg)

    def chegada (self):
        self.comunica("oi, estou chegando...")
        self.recebe()
        msg = raw_input(self.msg_r + "... (s ou n)\n" +  prompt)
        self.comunica(msg)
        self.recebe()
        self.s.send("show...")
        print(self.msg_r)
        if msg == "n" :
            msg = raw_input(self.s.recv(100)+ "\n" + prompt)
            self.comunica(msg)
            self.recebe()
            print(self.msg_r+prompt)
            self.s.send("OK")
        else:
            msg = raw_input(self.s.recv(100) + "\n" + prompt)
            self.comunica(msg)  
            self.recebe()          
    
    def saida (self):
        self.s.close()

    def recebe(self):
        self.msg_r = self.s.recv(100)

    def resp(self):
        print(self.msg_r)

    def comando (self):
        ##o servidor esta esperando umas mensagem / / o comando ##
        while 1:
            msg = raw_input(prompt)

            if (msg == "ls"):
                self.s.send(msg)
                print("enviado")
                self.msg_r = self.s.recv(100)
                print(self.msg_r)
            elif (msg == "mkdir"):
                ##
                self.comunica(msg)
                self.recebe()
                self.comunica(raw_input(self.msg_r))

            elif (msg == "rename"):
                ##
                self.comunica(msg)
                self.recebe()
                self.comunica(raw_input(self.msg_r))
                self.recebe()
                self.comunica(raw_input(self.msg_r))

            elif (msg == "rm"):
                ##
                self.comunica(msg)
                self.recebe()
                self.comunica(raw_input(self.msg_r))                
      ##      elif (msg == "upload"):
                ##
        ##    elif (msg == "download"):
                ##
          ##  elif (msg == "share"):
                ##



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
