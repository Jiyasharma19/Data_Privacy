import itertools
import string

# Function to perform a brute-force attack
def brute_force_attack(target_password, max_length=4):
    # Characters to use in the brute-force attempt
    characters = string.ascii_lowercase + string.digits + string.ascii_uppercase
    
    # Iterate through all possible lengths from 1 to max_length
    for length in range(1, max_length + 1):
        # Generate all possible combinations 
        for combination in itertools.product(characters, repeat=length):
            attempt = ''.join(combination)
            if attempt == target_password:
                return attempt
    return None

# Main function to take user input and initiate the brute-force attack
def main():
    target_password = input("Enter the password to simulate brute-force attack: ")
    max_length = int(input("Enter the maximum length for brute-force attempts: "))
    
    # Start the brute-force attack and get the result
    result = brute_force_attack(target_password, max_length)
    
    if result:
        print(f"Password found: {result}")
    else:
        print("Password not found within the given length.")

if __name__ == "__main__":
    main()
