# Program to read the content of file and display the total number of consonats vovels and uppercase letters
file = open('Text file') # opening the file
content = file.read() # saving the content of the file into a variable
vovels = ['A', 'E', 'I', 'O', 'U'] # list defining what are vovels
consonats = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X',' Y', 'Z'] # list defining what are consonats

# Default values for the counting
num_vovels = 0
num_consonats = 0
num_upper = 0

# For loop for counting
for letter in content:
    if letter.isupper():
        num_upper += 1
    if letter.upper() in consonats:
        num_consonats += 1
    if letter.upper() in vovels:
        num_vovels += 1

# Printing result
print("Vovels =", num_vovels)
print("Consonats =", num_consonats)
print("Uppercase =", num_upper)

