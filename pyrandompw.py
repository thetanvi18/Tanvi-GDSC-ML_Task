import random
import string

def generate_password():
    # Define character sets for different password components
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = '!@#$%^&*_'

    lowercase = random.choice(lowercase_letters)
    uppercase = random.choice(uppercase_letters)
    digit = random.choice(digits)
    special = random.choice(special_characters)

    # Combine all characters
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Set the password length between 6 and 15 characters
    length = random.randint(6, 15)
    
# Generate and print the password
password = generate_password()
print("Generated Password:", password)
