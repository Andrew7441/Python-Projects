from machine import MENU, resources

is_on = True
profit = 0

def is_resource_sufficient(order_ingredients):
    """Return true when order can be made and false if resources are insufficent"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        
    return True

def process_coins():
    """returns total calculated from inserted coins"""

    print("Insert Coins:")
    total = int(input("Quarters:")) * 0.25
    total += int(input("Dimes:")) * 0.10
    total += int(input("Nickels:")) * 0.05
    total += int(input("Pennies:")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return true when payment accepted or
       Return false if money is insufficient"""
    
    if money_received >= drink_cost:
        global profit
        change = round(money_received - drink_cost, 2)
        print(f"Change: ${change}")
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

def make_coffee(drink_name, order_ingredients):
        """Deduct required ingredients from resources"""
        for item in order_ingredients:
            resources[item] -= order_ingredients[item]
        print(f"Here is your {drink_name}! Enjoy!")

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml") 
        print(f"Milk: {resources['milk']}ml") 
        print(f"Coffee: {resources['coffee']}g") 
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])