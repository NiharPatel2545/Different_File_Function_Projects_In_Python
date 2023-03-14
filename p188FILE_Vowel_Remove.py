f1=open("G:\\abc.txt")

while True:

    c=f1.read(1)

    if not c:
        break
    if c=="a" or c=="e" or c=="i" or c=="o" or c=="u":
        pass
    else:
        print(c,end="")

f1.close()