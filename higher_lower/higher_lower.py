import random
import os

from game_data import data
from art import logo
from art import vs

# generate random value form data

def get_account():
    return random.choice(data)

def account_d(account):
    return f" {account['name']}, {account['description']}, from {account['country']}"

def check_follower(guess, follow_a, follow_b):
    if follow_a > follow_b:
        return guess == 'a'
    else:
        return guess == 'b'


def game():
    game_is_on = False 
    score = 0
    while game_is_on == False:
        print(logo)
        account_a = get_account()
        account_b = get_account()
        print(f"compare A: {account_d(account_a)}")
        print(vs)
        print(f"compare B: {account_d(account_b)}")
        guess = input("Who has more follower? Type 'A' or 'B'.")
        follow_a = account_a['follower_count']
        follow_b = account_b['follower_count']

        check_anwser = check_follower(guess, follow_a, follow_b)

        os.system('cls')
        print(logo)
        
        if check_anwser == True:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_is_on = True
            print(f"Sorry, that's wrong. Final score: {score}")

game()

    