#Program to create binary file to store Rollno and Name, Search any Rollno and display name if Rollno found otherwise “Rollno not found”
import pickle

def enter(file):
    f = open(file,'wb')
    try:
        student = pickle.load(open(file,'rb'))
    except EOFError:
        student = []

    try:
        rollNo =  input('Please enter the rollnumber: ')
        name = input("Please enter the name: ")
        student.append([rollNo,name])
        pickle.dump(student,f)
    except KeyboardInterrupt:
        print("cancelled")

def reader(file):
    f = open(file,'rb')
    student = pickle.load(f)
    try:
        r = input("Please enter roll number to search: ")
        for data in student:
            if data[0] == r:
                print("Name is",data[1])
                break
        else:
            print("Roll number not found")
    except KeyboardInterrupt:
        print("cancelled")

while True:
    usr = input("Press r to read and w to write information: ")
    if usr.lower() == "r":
        print("Press ctrl + c to cancel")
        reader("student.dat")
    elif usr.lower() == "w":
        print("Press ctrl + c to cancel")
        enter("student.dat")
    else:
        print("Error: Wrong input")
