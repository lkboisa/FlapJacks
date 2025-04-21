# Tyler and Dad's Python script
import os

print("Welcome to Tyler and Dad's lab at home")
name = input("What is your name?\n")

# Preventing certain players from accessing the game
if name.lower() in ["ralph", "ryan", "tyler", "brandon", ""]:
    print("You're not allowed to play this game :(")
    exit()
else:  
    os.system('cls' if os.name == 'nt' else 'clear')    
    print("Hello " + name + ", Welcome to BublyTyler the game\n\nWould you like to play?")

# Initialize player score
score = 0  

while True:   
    play_game = input("Type yes or no\n").strip().lower()
    if play_game == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
        questions = {
            "What is the tallest mountain in the world?": "Everest",
            "What does an electrical charge produce when it jumps from place to place?": "A Spark",
            "What is the capital of France?": "Paris",
            "What is the largest planet in are solar system?": "Jupiter",
            "Name one preset-day country where the Mayan culture flourished?": "Guatemala Mexico",
            "What planet is known as the Red Planet?": "Mars"
            
            
        }
        
        # Iterate through each question
        for question, answer in questions.items():
            attempts = 3  # Set attempt limit per question
            
            while attempts > 0:
                user_answer = input(question + " ").strip().lower()
                
                if user_answer == answer.lower():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Correct! You earned 5 points.\n")
                    score += 5  # Add points for correct answer
                    break  # Move to next question
                else:
                    attempts -= 1
                    score -= 2  # Deduct points for wrong answer
                    print(f"Woops, that's not right! {attempts} attempts left.")
            
            if attempts == 0:
                print(f"Out of attempts! The correct answer was: {answer}\n")
        
        print(f"The End! Your final score is: {score}")
        exit()
                
    elif play_game == "no":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Maybe another time")
        exit()
    else:
        print("Yes or No questions are difficult, aren't they?")
        exit()
