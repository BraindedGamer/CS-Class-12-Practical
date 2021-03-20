#creating a list of binary multiples of numbers using list comprehension
num = [i for i in range(0,20)]
mul = [2**i for i in range(0,20)]

for i in range(0,20):
    print(num[i]," : ",mul[i])