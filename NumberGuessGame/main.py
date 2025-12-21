from art import logo
import random

print(logo)
print("Welcome to the number Guessing Game")
print("Im thinking of a number between 1 and 100")

difficulty = input("Type 'easy' or 'hard': ").lower()
attempts = 0

if difficulty ==  "easy":
    attempts = 10
else:
    attempts = 5

number = random.randint(1, 100)

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")

    guess = int(input("\nMake a guess: "))

    if guess == number:
        print(f"\nYou got it! The answer was {number}")
        break
    elif guess < number:
        print("\nToo low\nGuess again")
        attempts -= 1
    elif guess > number:
        print("\nToo High\nGuess again")
        attempts  -= 1
    else:
        print("\nInvalid input")


if attempts == 0:
    print("You have run out of guesses. Game over!")