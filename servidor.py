#!/usr/bin/python2.7

import socket
import os

porta = 2529
prompt = ">> "
p2 = "<< "
class conexao:
    
    def __init__ (self, port):
        self.login = ""
        self.aceito = 0
        #create an INET, STREAMing socket
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #bind the socket to a public host,
        # and a well-known port
        self.s.bind(('localhost', port))
        #become a server socket
        self.s.listen(5)

    def comunica(self, msg):
        self.clisock.send(msg)
        self.msg_r = self.clisock.recv(100)

    def resposta(self):
        print(p2 + self.msg_r)

    def cad (self):
        self.comunica("Tem cad?")
        #[s / n]
        self.resposta()
        ##
        if self.msg_r == 'n':
            self.comunica("vou lhe cadastra, bb...")
            #Show...
            self.resposta()
            ##
            self.cadastra()
        else:
            self.comunica("fazer o login entao...")
            #Show...
            self.resposta()
            ##
            self.log()

    def log (self):
        ##########################################
        #############################  vars locais
        st = "0"
        achei = 0
        ##########################################
        ##########################################
        
        self.comunica("login?")
        #Login
        self.resposta()
        ##

        ##########################################
        #######################   CRITICO AJEITTAR
        ##########################################
        arq = open ("usrs.txt", "a+")
        arq.seek(0,0)
        
        while st != "":
            print ("login da vez >> " + st + "\n")
            print ("login procurado >> " + self.msg_r + "\n")
            st = arq.readline()
            st = st.replace("\n", "")
            if st == (self.msg_r):
                print ("Achei seu login")
                self.login = st
                os.system("cd " + st)
                achei = 1
                break
        if achei == 0:
            print("login nao achado")
            self.cad()
        arq.close()
#        self.desconecta()
        ##########################################


    def cadastra (self):
        self.comunica("login?")
        #Login...
        self.resposta()
        ##
        self.login = self.msg_r
        arq = open ("usrs.txt", "a+")
        arq.write(self.login)
        arq.write("\n.")
        arq.close()
        os.system("mkdir " + self.login)
        self.comunica("pasta raiz /USR/" + self.msg_r + " criada com sucesso.\nDigite seus comandos apos o prompt\n")
        ##Ok.
        self.resposta()
        ##
        #self.desconecta()
        self.cad()

    def espera(self):
        self.clisock, (self.remhost, self.remport) = self.s.accept()
        self.aceito += 1
        return self.clisock.recv(100)

    def desconecta(self):
        self.clisock.close()





    def comandos (self):
        print(prompt + self.msg_r)
        self.comunica(self.msg_r)
        while 1:
            print (self.s)
            print("recebi: " + self.msg_r)
            if self.msg_r == "q":
                print("adeus")
                break
            else:
                os.system(self.msg_r + "> retorno")
                arq = open("retorno", "r")
                self.comunica(arq.read())
                arq.close()

os.system("clear")
servidor = conexao(porta)
print(servidor.espera())
servidor.cad()
servidor.comandos()
servidor.desconecta()
