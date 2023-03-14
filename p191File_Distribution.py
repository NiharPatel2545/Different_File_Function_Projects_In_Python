f1=open("G:\\test.txt","r")
f2=open("G:\\No_Vowels.txt","w")
f3=open("G:\\Vowels.txt","w")
while True:
    c=f1.read(1)
    if not c:
        break

    if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
        f3.write(c)
    else:
        f2.write(c)

f1.close()
f2.close()
f3.close()