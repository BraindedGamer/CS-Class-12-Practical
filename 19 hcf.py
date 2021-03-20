#program to finf highest common factor of two functions recursively

def hcf(a,b):
    if (b==0):
        return a
    else:
        return hcf(b, a%b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("HCF of",num1,"&",num2,"is",hcf(num1,num2))
