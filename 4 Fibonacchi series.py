# Program to calculate the nth element of fibonacchi series
from random import randint # Importing randint from random to get the value of n
n = randint(0,50)
first = 0
second = 1

if n == 0:
    nthTerm = 0
elif n == 1:
    nthTerm = 1
else:
    for i in range(n - 2):
        first, second = second, first + second
    nthTerm = second

print(n, nthTerm)
