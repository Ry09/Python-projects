#This program is a guessing game where the computer chooses a random number and the user tries to guess it
#Shows use of random number generator and a loop

#This has been modified from the previous version to complete the challenge

import random

print("\t\t\tWelcome to the Guess My Number Game!")

print("\nI'm thinking of a number between 1 and 100")
print("Try to guess it in less than 10 attempts. Good Luck!")

# I use 101 because randrange(<num>) goes from 0 to (num you entered -1) 
goal = random.randrange(101)

userGuess = 102
totalGuesses = 0

print("\n")
while(userGuess != goal and totalGuesses < 10):
    userGuess = int(input("Take a guess: "))
    
    if(userGuess > goal):
        print("Lower...")
        totalGuesses += 1
    elif(userGuess < goal):
        print("Higher...")
        totalGuesses += 1
    else:
        totalGuesses += 1
    
if userGuess == goal:
    print("you guessed it! The number was ", goal)
    print("And it only took you ",totalGuesses, " tries!")
else:
    print("Oh too bad, guess your are not as good as you thought.")

input("\n\nPress enter to exit")

