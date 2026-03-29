# Our imports
import random

# Tell and get user input
print("Lets make you a cool codename...")
first_name, last_name = str(input("What's your first and last name? ").upper()).split() 

# Get the first letter for both first/last names
letter_firstname = first_name[0]
letter_lastname = last_name[0]


# Now we can do 28 if checks for both letter which would work but be VERY slow
# you would have to check through EVERY single iteration
# So we use a dictonary that we can grab our keys with list containing in them

letter_dict = {
    "A": [
        "Apple", "Arms", "Ample", "Awe", "Ape", "Astronaut",
        "Applaud", "Appease", "Agree", "Anterior", "Abandon",
        "Apron", "Animal", "Atmosphere", "Army"
    ],

    "B": [
        "Baby", "Back", "Background", "Bacon", "Bad", "Bag",
        "Bait", "Bake", "Balance", "Bald", "Ball", "Ballet",
        "Ballot", "Banana", "Band", "Bank", "Banner", "Battle"
    ],

    "C": [
        "Cat", "Camera", "Camp", "Candle", "Candy", "Canvas",
        "Captain", "Car", "Carbon", "Card", "Care", "Carpet",
        "Carry", "Castle", "Catch", "Cause"
    ],

    "D": [
        "Dance", "Danger", "Daring", "Dark", "Dash", "Data",
        "Dawn", "Day", "Deal", "Death", "Deck", "Deep",
        "Defend", "Delay", "Deliver"
    ],

    "E": [
        "Eagle", "Early", "Earth", "Ease", "Echo", "Edge",
        "Edit", "Effect", "Effort", "Egg", "Eight", "Either",
        "Elastic", "Elder", "Element"
    ],

    "F": [
        "Face", "Fact", "Fade", "Fail", "Fair", "Fall",
        "False", "Fame", "Family", "Famous", "Fan", "Fancy",
        "Fast", "Fate", "Fear", "Feather"
    ],

    "G": [
        "Gain", "Game", "Gap", "Garage", "Garden", "Gas",
        "Gate", "Gather", "Gear", "General", "Genius", "Gentle",
        "Ghost", "Giant", "Gift"
    ],

    "H": [
        "Habit", "Hair", "Half", "Hall", "Hand", "Handle",
        "Hang", "Happy", "Harbor", "Hard", "Harmony", "Hat",
        "Hawk", "Head", "Health"
    ],

    "I": [
        "Ice", "Icon", "Idea", "Ideal", "Image", "Impact",
        "Import", "Improve", "Include", "Index", "Inner",
        "Input", "Iron", "Island"
    ],

    "J": [
        "Jack", "Jam", "Jar", "Jazz", "Jeep", "Jelly",
        "Jewel", "Job", "Join", "Joke", "Journey", "Joy",
        "Judge", "Jump"
    ],

    "K": [
        "Keen", "Keep", "Key", "Kick", "Kid", "Kill",
        "Kind", "King", "Kite", "Knife", "Knight", "Knock",
        "Know"
    ],

    "L": [
        "Label", "Labor", "Lack", "Lady", "Lake", "Land",
        "Lane", "Large", "Laser", "Last", "Late", "Laugh",
        "Layer", "Lead", "Leaf"
    ],

    "M": [
        "Machine", "Magic", "Main", "Major", "Make", "Manage",
        "Map", "March", "Mark", "Market", "Master", "Match",
        "Matter", "Mean", "Measure"
    ],

    "N": [
        "Name", "Nation", "Nature", "Near", "Neat", "Need",
        "Nerve", "Nest", "Net", "New", "Next", "Night",
        "Noise", "Normal"
    ],

    "O": [
        "Oak", "Object", "Ocean", "Offer", "Office", "Oil",
        "Old", "Open", "Operate", "Opinion", "Option",
        "Order", "Origin"
    ],

    "P": [
        "Pack", "Page", "Paint", "Pair", "Panel", "Paper",
        "Park", "Part", "Pass", "Path", "Pattern", "Peace",
        "Peak", "Pen", "People"
    ],

    "Q": [
        "Quick", "Quiet", "Quilt", "Quit", "Quiz",
        "Quote", "Quest", "Queue", "Quirk", "Quiver",
        "Quake", "Quality"
    ],

    "R": [
        "Race", "Radio", "Rain", "Raise", "Range", "Rapid",
        "Rate", "Reach", "Read", "Ready", "Real", "Reason",
        "Record", "Red", "Region"
    ],

    "S": [
        "Safe", "Sail", "Salt", "Same", "Sand", "Save",
        "Scale", "Scan", "Scene", "School", "Science",
        "Score", "Search", "Season", "Seat"
    ],

    "T": [
        "Table", "Take", "Talk", "Tall", "Tank", "Tape",
        "Target", "Task", "Taste", "Teach", "Team",
        "Tech", "Tell", "Temple", "Test"
    ],

    "U": [
        "Ultra", "Umbra", "Uncle", "Under", "Unit",
        "Unique", "United", "Unity", "Update",
        "Upper", "Urban", "Use"
    ],

    "V": [
        "Value", "Vast", "Vector", "Vehicle", "Venture",
        "Version", "Very", "View", "Village",
        "Vision", "Visit", "Voice"
    ],

    "W": [
        "Wait", "Wake", "Walk", "Wall", "Want", "Warm",
        "Warn", "Wash", "Watch", "Water", "Wave",
        "Way", "Weak", "Wealth", "Weapon"
    ],

    "X": [
        "Xenon", "Xylo", "Xray", "Xenial", "Xyst",
        "Xenolith", "Xerox", "Xylem", "Xiphoid",
        "Xenodochial"
    ],

    "Y": [
        "Yard", "Year", "Yellow", "Yield", "Young",
        "Youth", "Yummy", "Yawn", "Yoke",
        "Yonder", "Yearn"
    ],

    "Z": [
        "Zero", "Zone", "Zoom", "Zebra", "Zest",
        "Zinc", "Zigzag", "Zip", "Zodiac",
        "Zenith", "Zephyr"
    ]
}

# Big lines, we grab a random number in list, from 0 to 
# the last digits *remeber not all of them have the same amount*, so
# we len to get the total amount and -1 because python don't like
# you grabbing the nth item in your string, out of index 

# Oh we do this for both first and last names
random_firstletter = random.randint(0,(len(letter_dict[letter_firstname])-1))
random_lastletter = random.randint(0,(len(letter_dict[letter_lastname])-1))

# now after the crazy stuff above, we just grab that random word from there
final_first = (letter_dict[letter_firstname][random_firstletter]) 
final_last = (letter_dict[letter_lastname][random_lastletter])

# and we print it!
print("")
print(f"Your new code name is >{final_first}, {final_last.lower()}<")
