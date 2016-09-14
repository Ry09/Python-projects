#This program flips a coin 100 times and then tells you the number of heads and
#tails.

import random

counter = 0
heads = 0
tails = 0

while counter < 100:
    flip = random.randint(1,2)

    if flip == 1:
        heads += 1
        counter += 1

    elif flip == 2:
        tails += 1
        counter += 1

print("\n\nAfter 100 flips there were "+ str(heads)+" heads, and "+ str(tails)+", tails!")

input("\n\nPress enter to exit.")
