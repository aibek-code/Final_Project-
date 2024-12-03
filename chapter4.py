import random
from chapter5 import chapter_5  # Import next chapter

def chapter_4():
    print("You meet a strange figure who knows about your past.")
    while True:
        action = input("Choose an action: 1. Listen, 2. Fight, 3. Ignore: ")
        if action == "1":
            listen_to_figure()
            break
        elif action == "2":
            fight_figure()
            break
        elif action == "3":
            ignore_figure()
            break
        else:
            print("Invalid choice. Please try again.")

def listen_to_figure():
    print("You listen to the figure and learn about your past.")
    chapter_4()  # Go back to the action selection screen after listening

def ignore_figure():
    print("You ignore the figure and move forward.")
    chapter_4()  # Go back to the action selection screen after ignoring

def fight_figure():
    print("You fight the figure.")
    success = random.choice([True, False])
    if success:
        print("You defeated the figure!")
        chapter_5()  # Proceed to chapter 5 if the player wins the fight
    else:
        print("You were defeated.")
        chapter_4()  # Return to the action selection screen if the player loses the fight