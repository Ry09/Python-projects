# This is a program to run the Collatz Sequence. It will
# take a number from the user and then divide it by 2 if
# it is even, or multiply by 3 and add 1 if it is odd. It
# will loop through this until it reaches the value of 1.

def collatz(num):
    try:
        num = int(num)
        print(num)
        if num == 1:
            print("Cannot begin with 0 or 1.")
            return 0
        while(num != 1):
            if num == 0:
                print("Cannot begin with 0 or 1.")
                return 0
            elif num % 2 == 0:
                num = num / 2
                print(num)
                continue
            else:
                num = num * 3 + 1
                print(num)
                continue
        return num
    except ValueError:
        print("Incorrect value entered. Please input a number.")
        return 0

while True:
    x = input("Please enter a number to begin the Collatz Sequnce. Also note that it cannot begin with 0 or 1: ")
    if collatz(x) == 1:
        print("And there you have the Collatz Sequence!")
        break
    else:
        continue
input("\n\n\nPress enter to exit.")
