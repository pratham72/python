import random
import hangman_words
import hangman_art

print(hangman_art.logo)

stage = hangman_art.stages

chosen_word = random.choice(hangman_words.word_list)

print(chosen_word)
lives = 6

display = []


for letter in range(len(chosen_word)):
    display += "_"

end_game = False

while not end_game:
    guess = input("Guess a letter:").lower()
    
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if "_" not in display:
        end_game = True
        print("You win")

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_game = True
            print("You lose.")
    
    print(stage[lives])
    
    

    
    
    
