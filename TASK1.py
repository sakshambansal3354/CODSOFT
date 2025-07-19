import random
import string

def generate_password(length):
    # Define possible characters: letters, digits, and symbols
    chars = string.ascii_letters + string.digits + string.punctuation
    # Generate a password by randomly choosing 'length' characters
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    try:
        # Prompt user for password length
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Password length must be a positive integer.")
            return
        # Generate and display the password
        pwd = generate_password(length)
        print("Generated Password:", pwd)
    except ValueError:
        print("Please enter a valid number for password length.")

if __name__ == "__main__":
    main()
