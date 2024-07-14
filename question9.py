# Write a Python function that generates a random password. The password should contain a mix of uppercase letters, lowercase letters, digits, and special characters.
import string
import random

def generate_random_password(length=12):
    # Define characters to choose from
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation  # includes !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    # Combine all characters
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

# Example usage:
password = generate_random_password()
print(f"Generated password: {password}")
