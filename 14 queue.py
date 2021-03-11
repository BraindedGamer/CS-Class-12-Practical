#program to implement queue in python

def isEmpty(q):
    return not bool(len(q))

def add(q,item):
    q.append(item)
    print(item, "successfully added.")

def remove(q):
    if not isEmpty(q):
        val = q.pop(0)
        return val

def peek(q):
    if not isEmpty(q):
        return q[0]

def show(q):
    if not isEmpty(q):
        print("Front <= ",end="")
        for i in q:
            print(i,"<= ",end="")
        print("Rear")
        return 0

Q=[]
while True:
    print("::Queue::")
    print("1. Add to Queue")
    print("2. Progress Queue")
    print("3. Show Next")
    print("4. Show Queue")
    print("0. Exit")
    try:
        usr = int(input())
        if usr == 1:
            item = input("Enter item to add: ")
            add(Q, item)
        elif usr == 2:
            val = remove(Q)
            if val == None:
                print("Queue is empty")
            else:
                print(val,"removed successfully")
        elif usr == 3:
            next = peek(Q)
            if next != None:
                print("Next in queue:",next)
            else:
                print("Queue is empty")
        elif usr == 4:
            temp = show(Q)
            if temp == None:
                print("Queue is empty")
        elif usr == 0:
            break
        else:
            print("Invalid input")
    except ValueError:
        print("Invalid input")
