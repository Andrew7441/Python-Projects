#functions with inputs / Arguments & Parameters


def greet():
    print("Hello")
    print("Hola")
    print("3l3awaf")

greet()

def greetwithname(name):                                        # parameter is name
    print(f"Hello {name}")

greetwithname(input("Enter your name: "))                       # Argument is what gets passed in 


def greet_with(name, location):           
    print(f"Hello {name} from {location}")

greet_with(input("Enter Name: "), input("Enter Location: "))    # Positional Argument

greet_with(location=input("Enter Location:"), name="Andrew")    # Keyword Arguments



def calculate_love_score(name1, name2):
    name1 = name1.upper()
    name2 = name2.upper()
    res1 = 0 
    res2 = 0
    for letter in name1:
        if letter in "TRUE":
            res1+=1
    for letter in name2:
        if letter in "TRUE":
            res1+=1
    
    for letter in name1:
        if letter in "LOVE":
            res2+=1
    for letter in name2:
        if letter in "LOVE":
            res2+=1

    print(str(res1) + str(res2))
    
calculate_love_score(name1 = "Angela Yu", name2 = "Jack Bauer")