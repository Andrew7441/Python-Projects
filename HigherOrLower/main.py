import art
import random
import data

game = True

print(art.logo)
points = 0

while game:

    guess1 = random.choice(data.data)
    name1 = guess1["name"]
    description1 = guess1["description"]
    country1 = guess1["country"]
    followers1 = guess1["follower_count"]


    print(f"Compare A: {name1}, {description1}, from {country1}")

    print(art.vs)

    guess2 = random.choice(data.data)
    name2 = guess2["name"]
    description2 = guess2["description"]
    country2 = guess2["country"]
    followers2 = guess2["follower_count"]

    print(f"Against B: {name2}, {description2}, from {country2}")

    choice = input("Who has more followers? Type 'A' or 'B': ")

    if choice == "A" and followers1 > followers2:
        points+=1
        print(art.logo)
        print(f"Youre right! Current Score: {points}")
    elif choice == "B" and followers2 > followers1:
        points+=1
        print(art.logo)
        print(f"Youre right! Current Score: {points}")
    else:
        print("\n" * 20)
        print(art.logo)
        print(f"Sorry thats wrong. Final Score: {points}")
        game = False

    





    
    