arq = open("login", "a+")
arq.write("dsaohafn;la\n")
arq.write("sdanj")
#st = "0"
arq.seek (0,0)
while st != "":
    st = arq.read()
    print (st)

