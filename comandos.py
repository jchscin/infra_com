import os.system

class comandos:

    ls (self, diretorio):
        os.system("ls " diretorio + " > retorno")
        ret = open("retorno")
        str = ret.read()
        return str

    ls (self):
        os.system("ls > retorno")
        ret = open("retorno

    cd (self, diretorio)
        self.diretorio = diretorio
        return ("Você está em " + self.diretorio)

    mkdir (self, diretorio)
    
