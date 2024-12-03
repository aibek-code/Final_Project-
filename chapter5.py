import random

def chapter_5():
    print("You face a huge enemy in the final battle.")
    while True:
        action = input("Choose an action: 1. Fight Bravely, 2. Train With Special Items: ")
        if action == "1":
            fight_bravely()
            break
        elif action == "2":
            train_with_special_items()
            break
        else:
            print("Invalid choice. Please try again.")

def train_with_special_items():
    print("You train with special items to defeat the enemy!")
    chapter_5()  # Go back to the action selection screen after training with special items

def fight_bravely():
    print("You fight bravely against the huge enemy!")
    success = random.choice([True, False])
    if success:
        print("You defeated the huge enemy!")
        end_game()  # Receive success message and end the game
    else:
        print("You were defeated.")
        chapter_5()  # Return to the action selection screen if the player loses the fight

def end_game():
    print("Congratulations! You've completed your journey.")
    print("Thank you for playing!")