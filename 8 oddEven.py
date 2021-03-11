def isEven(number):
    if number%2 == 0:
            return True
    else:
        return False

num = int(input("Please enter a number: "))
if isEven(num):
    print(num,"is an even number")
else:
    print(num,"is an odd number")
