# Imports
import random

# Ask user
amount_words = int(input("How many words should your password have? "))
amount_numbs = int(input("How many numbers should your password have? "))

# Our very long list got this online 
word_list = [
    "Apple",
    "Bird",
    "Book",
    "Bottle",
    "Box",
    "Bridge",
    "Brush",
    "Building",
    "Bus",
    "Button",
    "Camera",
    "Candle",
    "Car",
    "Carpet",
    "Cat",
    "Chair",
    "Child",
    "City",
    "Clock",
    "Cloud",
    "Coffee",
    "Computer",
    "Country",
    "Cow",
    "Cup",
    "Desk",
    "Dog",
    "Door",
    "Dress",
    "Drum",
    "Egg",
    "Engine",
    "Eye",
    "Farm",
    "Feather",
    "Film",
    "Finger",
    "Fire",
    "Fish",
    "Flower",
    "Food",
    "Foot",
    "Forest",
    "Fork",
    "Friend",
    "Garden",
    "Glass",
    "Glove",
    "Guitar",
    "Hair",
    "Hammer",
    "Hand",
    "Hat",
    "Heart",
    "Helmet",
    "Hill",
    "Horse",
    "Hospital",
    "House",
    "Island",
    "Key",
    "King",
    "Kitchen",
    "Knife",
    "Lamp",
    "Laptop",
    "Leaf",
    "Lemon",
    "Light",
    "Lion",
    "Map",
    "Mirror",
    "Mountain",
    "Mouse",
    "Mouth",
    "Music",
    "Newspaper",
    "Nose",
    "Ocean",
    "Orange",
    "Painting",
    "Paper",
    "Pen",
    "Phone",
    "Picture",
    "Pillow",
    "Plane",
    "Plant",
    "Plate",
    "Pocket",
    "Pond",
    "Queen",
    "Radio",
    "River",
    "Road",
    "School",
    "Screen",
    "Shoe",
    "Soap",
    "Spoon",
    "Note"
]

password = ""

# Loop through the amount the user put in earlier
for i in range(amount_words):
    password += random.choice(word_list)

for i in range(amount_numbs):
    password += str(random.randint(0,10))
print(password)



