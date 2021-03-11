#Program to get a number from a user and calculate it's factorial
print('Welcome to factorial finder')
run = True
while run: # main loop
    good_inp = False
    while not good_inp: # loop to get an input with fail-safes for dumb things a user can do
        try:
            num = int(input("Please enter a number:"))
            if num < 1: # Factorial doesn't exist for numbers below 1
                print("Error, bad input")
            else:
                good_inp = True
        except ValueError: # Fail-safe in case the user enters something other than a number
            print("I said number!!")
            
    fac = 1 # Default valur for factorial
    for i in range(1,num+1): # For loop to go over each number and multiply it to the factorial output
        fac *= i

    print("The factorial of "+str(num)+ " is:",fac)

    # code segment to prevent the program closing after just one input
    cont = input("Press enter to continue \nPress Q to quit ") 
    try:
        if cont.upper()[0] == 'Q':
            run = False
    except IndexError:
        run = True
