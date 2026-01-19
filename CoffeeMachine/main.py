from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

Coffeemaker = CoffeeMaker()
menu = Menu()
machine = MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        Coffeemaker.report()
        machine.report()
    else:
        drink = menu.find_drink(choice)
        if machine.make_payment(drink.cost) and Coffeemaker.is_resource_sufficient(drink):
            Coffeemaker.make_coffee(drink)
        