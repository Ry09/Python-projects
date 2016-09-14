#Challenge 4 from Chapter 2 of the book Python Programming for the absolute beginner by Michael Dawson
#
#Car price program.
#User enters the amount of a car and the program adds on the other various fees and returns the total cost.

carPrice = int(input("Enter the amount of a car (in dollars only,no cents)"))

tax = 0.07
fees = 0.03
hiddenFees = 0.01
grandTotal = int(carPrice*tax) + int(carPrice*fees) + int(carPrice*hiddenFees) + carPrice

print("\nTax is: ", int(carPrice*tax))
print("fees are: ", int(carPrice*fees))
print("Hidden fees are: ", int(carPrice*hiddenFees))

print("\n\nGrand Total is: ", grandTotal)

input("\n\nPress enter to exit")
