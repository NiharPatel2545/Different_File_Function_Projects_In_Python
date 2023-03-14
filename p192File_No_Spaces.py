f1=open("G:\\test.txt","r")
f2=open("G:\\No_Spaces.txt","w")

while True:

    c=f1.read(1)

    if not c:
        break
    if c==" ":
        pass
    else:
        f2.write(c)

f1.close()
f2.close()