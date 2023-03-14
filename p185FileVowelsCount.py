f1=open("G:\\abc.txt","r")
vc=0
while True:
    c=f1.read(1)
    if not c:
        break
    if c=="a" or  c=="e" or c=="i" or c=="o" or c=="u":
        vc=vc+1
f1.close()
print("Count=",vc)