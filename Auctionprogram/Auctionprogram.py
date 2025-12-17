from art import logo

print(logo)


diction = {}
auction = True

while auction:

    name = input("What is your name: ")
    bid = int(input("What is your bid: "))

    diction[name] = bid

    more = input("Are there any other bidders: Type 'yes' or 'no'").lower()
    if more == "no":
        auction = False


winner_name = ""
winner_bid = 0
for i in diction:
    if diction[name] > winner_bid:
        winner_name = name
        winner_bid = diction[name]

print(f"The winner is {winner_name} with a bid of ${winner_bid}")
