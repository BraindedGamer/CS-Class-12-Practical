def draw(n):
    print("o "*n)
    print("| "*n)
    print("| "*n)
    print("| "*n)
    print("| "*n)

total = 21
pick = 0
player = True
win = False

print("Welcome To Stick Picking Game : Computer Vs User")
print("Rule: 1) Both User and Computer can pick sticks between 1 to 4 at a time")
print("      2) Whosoever picks the last stick will be the looser")
print("++ Lets Begin ++")


draw(total)
while not win:
    if player:
        pick = 0
        print("++ User Turn ++")
        while pick not in [1,2,3,4]:
            pick = int(input("User pick the number of sticks you want to remove: "))
        total -= pick
        draw(total)
        player = False
    else:
        print("++ Computer Turn ++") 
        comp = 5-pick
        print("Computer removed",comp,"sticks")
        total -= comp
        draw(total)
        if total == 1:
            win = True
            print("Winner -- Computer")
            print("Better luck next time'")
        player = True