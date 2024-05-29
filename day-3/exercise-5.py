print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
\n
      ''')

# Print welcome message.
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

# Prompt the user for the first choice.
choice = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()

# Check the first choice.
if choice == "left":
    # Prompt the user for the second choice if they chose "left".
    choice = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    
    # Check the second choice.
    if choice == "wait":
        # Prompt the user for the third choice if they chose to "wait".
        choice = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
        
        # Check the third choice.
        if choice == "red":
            print("It's a room full of fire. Game Over.")
        elif choice == "yellow":
            print("You found the treasure! You Win!")
        elif choice == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        # Outcome if the user chose to "swim" in the second choice.
        print("You get attacked by an angry trout. Game Over.")
else:
    # Outcome if the user chose "right" in the first choice.
    print("You fell into a hole. Game Over.")
