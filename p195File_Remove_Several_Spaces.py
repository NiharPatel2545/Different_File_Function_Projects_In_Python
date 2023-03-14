f1=open("G:\\many_spaces.txt",'r')
f2=open("G:\\not_many_spaces",'w')
x=0
while True:

    c=f1.read(1)

    if not c:
        break
    if c==" ":
        x=x+1
        if x==1:
            f2.write(c)
    else:
        f2.write(c)
        x=0

f1.close()
f2.close()