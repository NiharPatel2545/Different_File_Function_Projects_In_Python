f1=open("G:\\abc.txt")

while True:

    c=f1.read(1)

    if not c:
        break
    if c.isupper():
        print(c.lower(),end="")
    if c.islower():
        print(c.upper(),end="")

f1.close()