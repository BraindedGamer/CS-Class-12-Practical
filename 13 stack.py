#Program to implement Stack in Python using List

def push(S,item):
    global top
    S.append(item)
    top = len(S) - 1

def pull(S):
    global top
    if len(S) != 0:
        val = S.pop()
    else:
        return None
    if len(S) == 0:
        top = None
    else:
        top = len(S)-1
    return val

def peek(S):
    if len(S) == 0:
        return None
    return S[top]

def show(S,top):
    if len(S) == 0:
        print("Stack is empty")
    else:
        print("(TOP) <== ",end = "")
        while top >= 0:
            print(S[top],"<== ",end="")
            top -= 1
        print()

stack = []
top = None
while True:
    print("::Stack Demonstration::")
    print("1. PUSH")
    print("2. PULL")
    print("3. PEEK")
    print("4. SHOW")
    print("0. EXIT")
    try:
        usr = int(input())
        if usr == 1:
            item = input("Enter item to push: ")
            push(stack,item)
            print(item,"successfully pushed")
        elif usr == 2:
            val = pull(stack)
            if val == None:
                print("Stack is empty")
            else:
                print(val,"removed from stack")
        elif usr == 3:
            val = peek(stack)
            if val == None:
                print("Stack is empty")
            else:
                print("The topmost value in the stack is",val)
        elif usr == 4:
            show(stack,top)
        elif usr == 0:
            break
        else:
            print("Invalid input")
    except ValueError:
        print("Invalid input")