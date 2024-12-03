import random
from chapter3 import chapter_3  # Import next chapter

def chapter_2():
    print("You reach an old temple with monsters guarding it.")
    while True:
        action = input("Choose an action: 1. Fight Monsters, 2. Search Temple, 3. Talk to Son: ")
        if action == "1":
            fight_monsters()
            break
        elif action == "2":
            search_temple()
            break
        elif action == "3":
            talk_to_son()
            break
        else:
            print("Invalid choice. Please try again.")

def fight_monsters():
    print("You fight the monsters! Be brave!!!")
    success = random.choice([True, False])
    if success:
        print("You defeated the monsters!")
        chapter_3()  # Proceed to chapter 3 if the player wins the fight
    else:
        print("You were defeated by the monsters.")
        chapter_2()  # Return to the action selection screen if the player loses the fight

def search_temple():
    print("You search the temple and find some treasure.")
    chapter_2()  # Go back to the action selection screen after searching

def talk_to_son():
    print("My son shares his worries about the journey.")
    chapter_2()  # Go back to the action selection screen after talking to son