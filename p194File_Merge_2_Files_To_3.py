f1=open("G:\\test.txt","r")
f2=open("G:\\new.txt","r")
f3=open("G:\\third_file.txt","w")

while True:

    c=f1.read(1)

    if not c:
        break

    f3.write(c)

while True:

    v=f1.read(1)

    if not v:
        break

    f3.write(v)

f3.close()