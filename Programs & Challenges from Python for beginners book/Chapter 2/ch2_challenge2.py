#Challenge 2 from CH2
#Favorite food masher program
#
#Takes a users favorite foods, and returns a string of those foods mashed together

favFood1 = input("What is your 1 of your favorite foods?")
favFood2 = input("\nWhat is another one of your favorite foods?")
favFood3 = input("\nWhat is another one of your favorite foods?")

mashedFavFoods = favFood1 + favFood2 + favFood3

print("\n\nAll together your 3 favorite are ", mashedFavFoods.strip())

input("\n\nPress enter to exit")
