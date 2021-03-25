# Program to read content from a file and print it with spaces replaced with # symbol
file = open('Text file') # opening the file
content = file.read() # saving the content of the file into a variable
words = content.split() # splitting the content by whitespaces using the builtin split() function

# Code to print the content
print(words[0], end='')
for i in words[1:]:
    print('#'+i, end='')
