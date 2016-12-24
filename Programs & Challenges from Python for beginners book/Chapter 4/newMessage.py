# No Vowel program
# this program demonstrates how to  create a new string
# through the use of a loop

message = input("Enter a message:")

newMessage = ""
vowels = 'aeiou'

print()
for letter in message:
    if letter.lower() not in vowels:
        newMessage += letter
        print("A new message has been created: ", newMessage)

print("Your original message without vowels is: ", newMessage)

input("Press enter to exit.")
