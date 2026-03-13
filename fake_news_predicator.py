"""
Fake News Generator
This program randomly generates funny fake news headlines.
The user can keep generating headlines until they choose to stop.
"""

import random


# ---------------------------
# List of possible subjects
# ---------------------------
subjects = [
    "Aditya",
    "Virat Kohli",
    "Elon Musk",
    "Donald Trump",
    "Joe Biden",
    "Delhi Government",
    "Automobile Industry",
    "Technology Sector",
    "NASA",
    "Indian Cricket Team",
    "Artificial Intelligence",
]


# ---------------------------
# List of actions
# ---------------------------
actions = [
    "is planning to",
    "has announced plans to",
    "is going to",
    "is considering",
    "is expected to",
    "is rumored to",
    "has secretly decided to",
    "has ordered teams to",
]


# ---------------------------
# List of places or events
# ---------------------------
places_or_things = [
    "launch a revolutionary product",
    "build a new city",
    "start a mission to Mars",
    "at the Red Fort",
    "in the next 5 years",
    "during IPL matches",
    "create the world's fastest car",
    "introduce flying taxis",
    "change the internet forever",
]


# ---------------------------
# Function to generate headline
# ---------------------------
def generate_headline():
    """Generate a random fake news headline."""

    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}."
    return headline


# ---------------------------
# Main program loop
# ---------------------------
def main():
    print("\n📰 Welcome to the Fake News Generator!\n")

    while True:
        # Generate and print a headline
        print(generate_headline())

        # Ask user if they want another headline
        user_input = input("\nDo you want another news headline? (yes/no): ").strip().lower()

        if user_input in ["no", "n"]:
            break

    print("\nThank you for using the Fake News Generator! Stay informed and have a great day! 🚀")


# Run the program
if __name__ == "__main__":
    main()
