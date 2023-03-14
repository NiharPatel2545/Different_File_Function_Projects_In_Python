f1=open("G:\\abc.txt")
UCC=0
LCC=0

while True:

    c=f1.read(1)

    if not c:
        break
    if c.isupper():
        UCC=UCC+1
    if c.islower():
        LCC=LCC+1

f1.close()

print("UpperCases=",UCC)
print("LowerCases=",LCC)