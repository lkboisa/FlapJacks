#Tyler and Dad's python script
import os
print("Welcome to Tyler and Dad's lab at home")
name = input("What is your name?\n")

if name.lower() in ["ralph", "ryan", "tyler", "brandon" ""]:
    print("Your not allowed to play this game :(")
    exit()
else: 
    os.system('cls' if os.name == 'nt' else 'clear')    
    print("Hello " + name + ", Welcome to BublyTyler the game\n\nWould you like to play?") 
    
    
play_game = input("(Type yes or no)\n").lower()
if play_game == "yes":
    os.system('cls' if os.name == 'nt' else 'clear')
    math = input("what is the sum of three and two?\n").lower()
    if math in ["5", "five"]:
        print(":)")
    else: 
        print("retard")
        exit()
elif play_game == "no":
    print("exiting the game")
    exit()
