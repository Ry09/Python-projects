#Challenge 3 from Chapter 2 of the book Python Programming for the absolute beginner by Michael Dawson
#
#This is a tipper program. Where the user enters the total of a restaurant bill and it returns both the 15% and 20% tip
#Need to fix so that the tips return with just 2 decimal places.

bill = float(input("Enter the amount of the restaurant bill to calculate tip: "))

tip15 = bill * 0.15
tip20 = bill * 0.2

print("\nThe 15% tip is: ", tip15)
print("\nThe 20% tip is: ", tip20)

input("\n\nPress enter to exit")
