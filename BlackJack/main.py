from art import logo
import random

def dealcards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw!"
    elif c_score == 0:
        return "Lose, opponent has Blackjack!"
    elif u_score == 0:
        return "Win, BlackJack!"
    elif u_score > 21:
        return "You went over, You lose!"
    elif c_score > 21:
        return "Opponent went over, You Win!"
    elif u_score > c_score:
        return "You Win!"
    else:
        return "You Lose!"

def play_game():
    user_cards = []
    comp_cards = []
    computer_score = -1
    user_score = -1
    game_over = False

    print(logo)

    for _ in range(2):
        user_cards.append(dealcards())
        comp_cards.append(dealcards())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(comp_cards)

        print(f"\nYour cards: {user_cards}, current score: {user_score}")
        print(f"Computer first card: {comp_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_deal = input("\nType 'y' to hit. Type 'n' to pass: ")
            if user_deal == 'y':
                user_cards.append(dealcards())
            else:
                game_over = True
        
    while computer_score != 0 and computer_score < 17:
        comp_cards.append(dealcards())
        computer_score = calculate_score(comp_cards)

    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer final hand: {comp_cards}, Computer final score: {computer_score}\n")
    print(compare(user_score, computer_score))


while input("Do you want to play a gam of blackjack? Type 'y' or 'n': ").lower() == 'y':
    print("\n" * 20)
    play_game()