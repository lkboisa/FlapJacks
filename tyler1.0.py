#Tyler and Dad's python script
import os

print("Welcome to Tyler and Dad's lab at home")
name = input("What is your name?\n")

if name.lower() in ["ralph", "ryan", "tyler", "brandon", ""]:
    print("Your not allowed to play this game :(")
    exit()
else: 
    os.system('cls' if os.name == 'nt' else 'clear')    
    print("Hello " + name + ", Welcome to BublyTyler the game\n\nWould you like to play?")
        
while True:   
    play_game = input("Type yes or no\n").strip().lower()
    if play_game == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
        questions = {
        "what is the sum of two and two": "4",
        "What planet is known as the Red Planet?": "Mars",
        "What is the capital of France": "Paris"
        }
        
        for question, answer in questions.items():          
            while True:
                user_answer = input(question + " ").strip().lower()
                if user_answer == answer.lower():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Correct!")
                    break
                else:
                    print("Woops, that's not right")
                    
        print("Thee End")
        exit()
                
    elif play_game == "no":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Maybe another time")
        exit()
    else:
        print("Yes or No questions are difficult, aren't they?")
        exit()
