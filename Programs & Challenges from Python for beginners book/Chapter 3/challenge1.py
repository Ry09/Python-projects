#This challenge is about writing a program that simulates a fotune cookie

import random

print("\t\tFortune Cookie Simulator")

input("\nPress enter to open your fortune cookie!\n\n\n")

fortune = random.randint(1,5)

if fortune == 1:
    print("You will receive help from an unexpected source this afternoon.")

elif fortune == 2:
    print("Beware the woman with the red shoes, she has an agenda of her own that you will not like.")

elif fortune == 3:
    print("There is a pleasant surprise awaiting you this evening.")

elif fortune == 4:
    print("Today you will need to make an important choice. You will be drawn to choose one that benefits your superiors more. While this will gain their favor, it will take a toll on your conscience. Therefore make the decision that you know will be best for the group as a whole.")

elif fortune == 5:
    print("Today will be a good day for you!")


input("\n\nPress enter to exit.")
