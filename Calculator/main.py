from art import logo

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+" : add, # not triggering the functions because im storing it as variables, not using it 
    "-" : sub,
    "*" : mul,
    "/" : div,
}

def calculator():
    print(logo)
    accumulate = True

    num1 = float(input("Type the first number: "))

    while accumulate:
        for i in operations:
            print(i)

        op = input("Pick an operation from the above: ")

        num2 = float(input("What is the next number: "))
        
        answer = operations[op](num1, num2)

        print(f"{num1} {op} {num2} = {answer}")
        
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == 'y':
            num1 = answer
        else:
            accumulate = False
            print("\n" * 20)
            calculator()



calculator()

    