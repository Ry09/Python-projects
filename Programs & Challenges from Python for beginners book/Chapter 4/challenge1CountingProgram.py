# Challenge 1
# the challenge requires a program that lets the user enter a starting number,
#  the ending number, and the amount by which to count. The program will then
#  count for the user.

# Note this program has not been designed for error handling or type checks

print("\t\tWelcome To Your Personal Counting Program!\n")

startingNum = int(input("Enter the number you wish to start counting from: "))

endingNum = int(input("\nEnter the number you wish to end at: "))

countBy = int(input("\nNow enter how you want to count by (ie 1, 2, 5, for backwards enter -1):"))

for i in range(startingNum,endingNum,countBy):
    print(i)

input("\t\t\n\nPress Enter to Exit.")
