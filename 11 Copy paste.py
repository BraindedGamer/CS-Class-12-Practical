#Program to read the content of file line by line and write it to another file except for the lines contains „a‟ letter in it.

f1 = open("See you again.txt","r")
f2 = open("File2","w")

for line in f1:
    if "a" not in line:
        f2.write(line)

f1.close()
f2.close()