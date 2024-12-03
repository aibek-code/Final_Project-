import random
from chapter4 import chapter_4  # Import next chapter

def chapter_3():
    print("You climb the mountain.")
    while True:
        action = input("Choose an action: 1. Solve Puzzle, 2. Fight Enemy, 3. Look for Hidden Paths: ")
        if action == "1":
            solve_puzzle()
            break
        elif action == "2":
            fight_enemy()
            break
        elif action == "3":
            look_for_hidden_path()
            break
        else:
            print("Invalid choice. Please try again.")

def solve_puzzle():
    print("You solve the puzzle and proceed.")
    chapter_3()  # Go back to the action selection screen after solving puzzle

def fight_enemy():
    print("You fight an enemy on the mountain!")
    success = random.choice([True, False])
    if success:
        print("You defeated the enemy!")
        chapter_4()  # Proceed to chapter 4 if the player wins the fight
    else:
        print("You were defeated.")
        chapter_3()  # Return to the action selection screen if the player loses the fight

def look_for_hidden_path():
    print("You discover new secrets.")
    chapter_3()  # Go back to the action selection screen after searching