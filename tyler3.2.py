# Tyler and Dad's Python script
import os
import random
import time

print("Welcome to Tyler and Dad's lab at home")
name = input("What is your name?\n")

# Preventing certain players from accessing the game
if name.lower() in ["ralph", "ryan", "tyler", "brandon", ""]:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("You're not allowed to play this game :(")
    time.sleep(3)
    exit()
else:  
    os.system('cls' if os.name == 'nt' else 'clear')    
    print("Hello " + name + ", Welcome to BublyTyler the game\n\nTo play, answer 5 trivia questions!\nYou will have 3 attempts to land the correct answer.\nEach correct answer awards 5 points but each wrong answer will take away 2.\n\nWould you like to play?")

# Initialize player score
score = 0  

while True:   
    play_game = input("Type yes or no\n").strip().lower()
    if play_game == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
        questions = {
            "What is the tallest mountain in the world?": ("Mount Everest", "Everest"),
            "What does an electrical charge produce when it jumps from place to place?": ("A Spark", "Spark"),
            "What is the capital of France?": ("Paris",),
            "What is the largest planet in our solar system?": ("Jupiter",),
            "Name one preset-day country where the Mayan culture flourished?": ("Mesoamerica", "Guatemala", "Mexico", "Belize", "Honduras", "El Salvador"),
            "What planet is known as the Red Planet?": ("Mars",),
            "What vitamin is the same as ascorbic acid?": ("Vitamin C",),
            "What do you call the thinnest and smallest blood vessels?": ("Capillaries",),
            "What do meat, milk, and eggs provide in our diet?": ("Protein",),
            "It is 7 miles to the train, then 33 miles to town. How long is the round trip?": ("80 miles", "eighty miles", "eighty", "80"),
            "What is the highest rank in the U.S. Navy?": ("Admiral",),
            "What liquid food do bees get from flowers?": ("Nectar",),
            "Which has the most gravity: a supernova, a white dwarf, or a black whole?": ("A black whole", "black whole"),
            "Samurai were warriors in what country?": ("Japan",),
            "What do we call the galaxy that includes our solar system?": ("The Milky Way", "Milky Way"),
            "Victoria, Edmonton and Toronto are cities in what country?": ("Canada",)
    }
        questions_list = list(questions.items()) #convert dictionary to a list
        random.shuffle(questions_list)           #shuffle list
        select_questions = questions_list[:5]    #select first 5 questions
        
        for q, a in select_questions: # Iterate through each question
            attempts = 3  # Set attempt limit per question
            
            while attempts > 0:
                user_answer = input(q + " ").strip().lower()
                
                if user_answer.lower() in (answer.lower() for answer in a):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Correct! You earned 5 points.\n")
                    score += 5  # Add points for correct answer
                    break  # Move to next question
                else:
                    attempts -= 1
                    score -= 2  # Deduct points for wrong answer
                    print(f"Woops, that's not right! {attempts} attempts left.")
            
            if attempts == 0:
                print(f"Out of attempts! The correct answer was: {a[0]}\n")
        
        print(f"Thanks for playing {name}! Your final score is {score}/25")
        time.sleep(6)
        exit()
                
    elif play_game == "no":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Maybe another time")
        exit()
    else:
        print("Yes or No questions are difficult, aren't they?")
