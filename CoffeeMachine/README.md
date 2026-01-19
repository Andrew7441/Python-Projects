## Overview
A small object-oriented Python program that simulates a coffee machine.
It supports three drinks (espresso, latte, cappuccino), a report command to show ingredients and money, and an off command to stop the machine.

This README documents how to run the project, explains the OOP design, and gives a few concrete suggestions/fixes so the program is robust and easy to maintain.

## Design and OOP summary
The program uses these classes:

#### MenuItem — Interface-like model for a drink

In your code MenuItem is used as a simple class that defines the data shape for menu items (name, cost, ingredients). This is effectively acting as an interface in the sense that other parts of the code expect any menu item to provide name, cost and an ingredients mapping.

Note: Python does not enforce interfaces like Java/C#. If you want an explicit interface-like guarantee, convert MenuItem to an abstract base class (from abc) or use a dataclass. Example options are shown below.

#### Menu — Concrete

Holds MenuItem objects and provides:

get_items() — returns available items (for prompt)

find_drink(name) — returns the MenuItem or None

#### CoffeeMaker — Concrete

Tracks resources (water, milk, coffee) and includes:

report() — prints current resources

is_resource_sufficient(drink) — checks if a drink can be made

make_coffee(drink) — deducts ingredients and prints the completion message

#### MoneyMachine — Concrete

Handles payment:

process_coins() — asks user for coins and sums them

make_payment(cost) — verifies payment and updates profit

report() — prints current profit

### Quick Start
python main.py

### Instructions
'''python
Run the coffee_machine.py script in your Python environment.

Follow the on-screen prompts to place your order:
    Type 'espresso' for a shot of espresso.
    Type 'latte' for a delicious latte.
    Type 'cappuccino' for a frothy cappuccino.

Use the following commands for additional functionalities:
    Type 'report' to view the current status of ingredients.
    Type 'off' to turn off the coffee machine and end the script.
'''
Enjoy your virtual coffee experience!
