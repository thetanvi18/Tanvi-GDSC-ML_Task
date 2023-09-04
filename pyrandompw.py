import random
import string

def generate_password():
    # Define character sets for different password components
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = '!@#$%^&*_'

    # Create a pool of characters for each category
    pool_lowercase = random.choice(lowercase_letters)
    pool_uppercase = random.choice(uppercase_letters)
    pool_digit = random.choice(digits)
    pool_special = random.choice(special_characters)

    # Combine all character pools
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Set the password length between 6 and 15 characters
    length = random.randint(6, 15)

    # Calculate the number of characters needed from each pool
    remaining_length = length - 4  # We've already chosen 4 characters
    chars_per_pool = [1, 1, 1, remaining_length - 3]  # Subtract 3 for the 3 pools already chosen

    # Randomly select characters from each pool
    password = random.choice(pool_lowercase) + random.choice(pool_uppercase) + random.choice(pool_digit) + random.choice(pool_special)
    password += ''.join(random.choice(all_characters) for _ in range(remaining_length))

    # Shuffle the password to make it more random
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

# Generate and print the password
password = generate_password()
print("Generated Password:", password)
