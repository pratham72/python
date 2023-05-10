import random

print("Welcome to the Number Guessing Game !")
print("I'm thinking of a number between 1 to 100.")

chosen_number = random.randint(1, 101)
print(chosen_number)

level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if level == 'easy':
    attempt = 10
if level == 'hard':
    attempt = 5
while attempt > 0:
    attempt = attempt - 1
    print(f"you have {attempt} attempts remaining to guess the number.")
    guess = int(input("make a guess: "))
    if guess == chosen_number:
        print(f"you got it!, The answer was {guess}.")
    if guess > chosen_number:
        print(f"Too high.")
    if guess < chosen_number:
        print(f"Too low.")
    if attempt == 0 and guess != chosen_number:
        print("you've run out of guesses, you lose.")