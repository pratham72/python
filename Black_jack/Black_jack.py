import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

def deal_card():
    card = random.choice(cards)
    return card

def calculate_score(l_cards):
    if l_cards == 21 and  len(l_cards) == 2:
        return 0
    if 11 in l_cards and sum(l_cards) > 21:
        l_cards.remove(11)
        l_cards.append(1)
    return sum(l_cards)
    
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has blackjack"
    elif user_score == 0:
        return "win with a blackjack"
    elif user_score > 21:
        return "you went over. you lose."
    elif computer_score > 21:
        return "Opponent went over. you win."
    elif user_score > computer_score:
        return "you win"
    else:
        return "you lose"

def play():   
    
    print(logo)

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_ends = False

    while not game_ends:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"user cards = {user_cards} , user_score = {user_score}")
        print(f"computer's first card = {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_ends = True
        else:
                con_play = input("Type 'y' to draw other card and 'n' to pass: ")
                if con_play == 'y':
                    user_cards.append(deal_card())
                else:
                    game_ends = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"user cards = {user_cards} , user score = {user_score}")
    print(f"computer's card = {computer_cards}, computer score = {computer_score}")

    print(compare(user_score, computer_score))

while input("Type 'y' to play blackjack game again else type 'n' : ") == 'y':
    play()

