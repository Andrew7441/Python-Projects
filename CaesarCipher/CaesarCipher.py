from art import logo

print(logo)

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    new_word = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    
    for letter in original_text:
        if letter not in alphabets:
            new_word += letter
        else:
            shifted = alphabets.index(letter) + shift_amount
            shifted %= len(alphabets)
            new_word += alphabets[shifted]
    
    print(f"The {encode_or_decode}d result: {new_word}")


choice = True
while choice:
    direction = input("Type 'encode' to encrypt. 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    ask = input("Do you want to go again? yes/no:").lower()
    if ask == "no":
        choice = False
        print("Thank you")

