# password generator

import random
import string

def generate_password(length):
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    
    # Combine all character sets
    all_chars = letters + digits + special_chars
    
    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

def main():
    print("Password Generator")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                print("Please enter a positive number.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        password = generate_password(length)
        print(f"Generated Password: {password}")
        
        another = input("Generate another password? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
