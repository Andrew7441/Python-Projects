import random
from hangmanart import stages
from hangmanart import logo
from hangmanwords import word_list

print(logo)

chosen_word = random.choice(word_list)

placeholder = ""
for i in chosen_word:
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []
lives = 6

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    
    if guess not in chosen_word:
        print(stages[lives])
        lives-=1
        if lives < 0:
            print("You Lose")
            game_over = True

    if "_" not in display:
        print("You Win!")
        game_over = True
    
    print(display)

print(f"The word was: {chosen_word}")