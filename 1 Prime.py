def isPrime(number):
    if number == 1:
        return False
    for i in range (2,number):
        if number%i == 0:
            return False
    else:
        return True

num = int(input("Please enter a number: "))
if isPrime(num):
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")
