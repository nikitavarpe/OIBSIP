import random
import string

def generate_password(length, use_digits, use_special_chars):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    
    password = ""
    for i in range(length):
        random_character = random.choice(characters)
        password += random_character
    return password


length = int(input("Enter the desired password length: "))
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    
password = generate_password(length, use_digits, use_special_chars)
print(f"Generated Password: {password}")


