import random 
import string

def password_generator(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special
    
    password = ""

    while len(password) < min_length:
        password += random.choice(characters)

    return password


min_length = int(input("Enter the minimum length you want your password to be: "))
password = password_generator(10)
print(password)



