# Password Generator

import random
import string

def generate_password(length=12, use_digits=True, use_special_chars=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        raise ValueError("No character set selected for password generation.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_password_length():
    try:
        length = int(input("Enter the password length (default is 12): "))
        return length if length > 0 else 12
    except ValueError:
        return 12

def main():
    print("Password Generator")
    length = get_password_length()
    
    use_digits = input("Include digits in the password? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters in the password? (y/n): ").lower() == 'y'
    
    password = generate_password(length, use_digits, use_special_chars)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
