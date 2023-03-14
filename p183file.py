f1=open("G:\\abc.txt","r")
cnt=0
while True:
    c=f1.read(1)
    if not c:
        break
    if c==" ":
        cnt=cnt+1
f1.close()
print("total spaces = ",cnt)