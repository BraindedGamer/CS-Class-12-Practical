# Program to find sum of element of a list
from random import randint # Importing randint from random to help make the list
num_list = [randint(0,50) for i in range (10)] # Making the list using list comprehesion

sum = 0
for num in num_list:
    sum += num

print("The sum of all elements of",num_list,'is',sum)

