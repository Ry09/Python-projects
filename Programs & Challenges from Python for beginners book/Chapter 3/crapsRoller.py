#This program simulates 2 dice being rolled. It returns the value of each die and their sum.
#Also shows 2 different ways to use the random number generator.

import random

die1 = random.randint(1,6)  # generates a random number from 1 - 6
die2 = random.randrange(6) + 1 # need to ass + 1 because it generates numbers from 0 - (num entered - 1)

total = die1 + die2

print("\nYou rolled a", die1, "and a", die2, "for a total of", total)

input("\n\nPress enter to exit")
