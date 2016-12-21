# Random Access program
# this program helps demonstrate how string indexing works

import random

word = "Gaming"
print("The word is: ", word, "\n")

high = len(word)
low = -len(word)

for i in range(10):
    position = random.randrange(low, high)
    print("word[", position, "]\t", word[position])

input("\n\n PRess the enter key to exit.")
