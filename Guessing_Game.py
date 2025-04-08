import random
from art import logo
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
def check_answer(guess, x, turns):
    """Checks answers against the guess and returns the number of turns remaining"""
    if guess < x:
        print(f"Too high.")
        print("Guess again")
        return turns-1
    elif guess > x:
        print(f"Too low.") 
        print("Guess again")
        return turns-1
    else:
        print(f"You got it. The answer is {guess}")  
        
def set_difficulty():
    dif=input("Choose a difficulty. Type 'easy' or 'hard': ")
    if dif== "easy":        
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
def game():
    print(logo)
    print(f"Welcome to the guessing game! ")
    print("I am thinking of a number between 1 to 100.")
    numbers = list(range(1, 101))
    guess = random.choice(numbers)
    print(f"Psst, the correct answer is {guess}")

    turns=set_difficulty()
    x=0
    while x!= guess:
        print(f"You have {turns} attempts left.")
        x=int(input("Make a guess: "))
        turns = check_answer(guess, x, turns)
        if turns == 0:
            print("You run out of guesses. You lose.")
            return

game()
