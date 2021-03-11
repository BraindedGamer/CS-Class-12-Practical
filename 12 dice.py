import random

while True:
    try:
        input("Press enter to generate a number")
        print(random.randint(1,6))
    except KeyboardInterrupt:
        print('Goodbye')
        break