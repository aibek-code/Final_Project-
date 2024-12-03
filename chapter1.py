import random
from chapter2 import chapter_2  # import next chapter

# global variables
player_name = ""

# start game
def start_game():
    global player_name
    player_name = input("Enter your name: ")
    print(f"Hello, {player_name}!")
    ready = input("Ready to start the adventure? (y/n): ")
    if ready.lower() == 'y':
        chapter_1()  # start chapter 1
    elif ready.lower() == 'n':
        print("Goodbye!") 
    else:
        print("Wrong selection. Please select another option! (y/n)")
        start_game()
# chapter 1: actions at the forest edge
def chapter_1():
    print("You are at the edge of the forest with your son.")
    while True:
        action = input("Choose an action: 1. Explore, 2. Talk to Son, 3. Fight Animal: ")
        if action == "1":
            explore_forest()
            break
        elif action == "2":
            talk_to_son()
            break
        elif action == "3":
            fight_wild_animal()
            break
        else:
            print("Invalid choice. Please try again.")

# explore eorest
def explore_forest():
    print("You explore the forest and find useful items.")
    chapter_1()  # return to the action selection screen after exploring

# talk to son
def talk_to_son():
    print("Your son shares his worries about the journey.")
    chapter_1()  # return to the action selection screen after talking to son

# fight wild animal
def fight_wild_animal():
    print("A wild animal appears!")
    success = random.choice([True, False])

    if success:
        print("You defeated the wild animal!")
        chapter_2()  # proceed to chapter 2 if the player wins the fight
    else:
        print("You were injured!")
        chapter_1()  # return to the action selection screen if the player loses the fight